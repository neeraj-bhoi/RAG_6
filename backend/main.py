import os
import sys
import json
import re
import requests
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional, Any
from dotenv import load_dotenv

try:
    from backend.rag import retrieve_context
    from backend.llm_router import generate_answer, classify_service, detect_query_language, translate_query_to_english
except ImportError:
    from rag import retrieve_context
    from llm_router import generate_answer, classify_service, detect_query_language, translate_query_to_english


# Ensure stdout uses UTF-8 to prevent Windows-specific print emoji/char crashes
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# App paths
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(WORKSPACE_DIR, "data", "rag_kb_manifest.json")

# 1. Initialize FastAPI app
app = FastAPI(title="SewaSetu RAG API Server")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Load Services Manifest
if not os.path.exists(MANIFEST_PATH):
    raise FileNotFoundError(f"Manifest file not found at: {MANIFEST_PATH}")

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest_data = json.load(f)

services_list = manifest_data.get("services", [])

# Map sno to service_id and vice-versa
sno_to_sid = {s["sno"]: int(s["service_id"]) for s in services_list}

# 3. Modular imports are now used instead of global model initialization.



# Pydantic schemas
class Message(BaseModel):
    role: str  # 'user', 'assistant' or 'system'
    content: str

class ChatRequest(BaseModel):
    query: Optional[str] = None
    lang: Optional[str] = None
    service_id: Optional[Any] = None
    conversation_history: Optional[List[Message]] = None
    
    # Frontend support schemas
    messages: Optional[List[Message]] = None
    selected_sno: Optional[str] = None
    language: Optional[str] = None

class SearchRequest(BaseModel):
    query: str
    language: Optional[str] = "en"


# Endpoints

@app.get("/api/services")
def list_services():
    """
    Returns the list of the 5 in-scope services from the manifest.
    """
    # Keep the response model clean for the frontend, return target fields
    result = []
    for s in services_list:
        result.append({
            "sno": s["sno"],
            "service_id": s["service_id"],
            "name_en": s["name_en"],
            "name_hi": s["name_hi"],
            "dept_en": s["dept_en"],
            "dept_hi": s["dept_hi"],
            "is_internal": s.get("is_internal", True)
        })
    return result


@app.get("/api/services/{sno}")
def get_service_details(sno: str, lang: str = "en"):
    """
    Retrieves the detailed JSON profile of a specific service from the profiles directory.
    """
    target_service = None
    for s in services_list:
        if str(s["sno"]) == str(sno):
            target_service = s
            break

    if not target_service:
        raise HTTPException(status_code=404, detail=f"Service with serial number {sno} not found.")

    # Determine profile path
    path_key = f"path_{lang}"
    rel_path = target_service.get(path_key) or target_service.get("path_en")
    if not rel_path:
        raise HTTPException(status_code=404, detail="Service profile path not configured in manifest.")

    filepath = os.path.join(WORKSPACE_DIR, rel_path)
    if not os.path.exists(filepath):
        # Fallback to English profile
        rel_path_en = target_service.get("path_en")
        if rel_path_en:
            filepath = os.path.join(WORKSPACE_DIR, rel_path_en)

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail=f"Profile JSON details not found at {rel_path}.")

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        fees_obj = data.get("fees", {})
        kiosk_fee = fees_obj.get("kiosk_fee", "30.0")
        online_fee = fees_obj.get("online_fee", "30.0")
        raw_fees_text = fees_obj.get("raw_text", "")

        req_docs_structured = data.get("required_documents_structured", [])
        req_docs = data.get("required_documents", [])

        details_payload = {
            "sno": str(sno),
            "service_id": str(target_service["service_id"]),
            "name": data.get("name"),
            "department": data.get("department"),
            "time_limit": data.get("time_limit") or data.get("sla"),
            "contact_details": data.get("contact_details", "Sewa Setu Kendra"),
            "fees": {
                "online_fee": online_fee,
                "kiosk_fee": kiosk_fee,
                "raw_text": raw_fees_text
            },
            "details_link": data.get("details_link"),
            "required_documents_structured": req_docs_structured,
            "required_documents": req_docs,
            "form_fields": data.get("form_fields", [])
        }
        return details_payload
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading service details profile: {str(e)}")


@app.post("/api/chat")
def chat_with_bot(request: ChatRequest):
    """
    RAG Chat endpoint returning Server-Sent Events (SSE) stream.
    """
    print("\n" + "=" * 80)
    print("[DEBUG] /api/chat INCOMING REQUEST PAYLOAD:")
    try:
        print(request.model_dump_json(indent=2))
    except Exception as e:
        print(f"Error printing payload: {e}")
    print("=" * 80 + "\n")

    # 1. Resolve query
    query = request.query
    if not query and request.messages:
        query = request.messages[-1].content

    if not query:
        raise HTTPException(status_code=400, detail="Query text is required.")

    # 2. Detect query language using LLM (English, Hindi, or Hinglish)
    query_lang = detect_query_language(query)
    print(f"[API Chat] Detected language for query '{query}': '{query_lang}'")

    english_query = query
    if query_lang in ["hi", "hinglish"]:
        try:
            english_query = translate_query_to_english(query)
        except Exception as e:
            print(f"[API Chat] Failed to translate query: {e}")

    # 3. Resolve service_id / sno
    service_id = None
    sno = request.selected_sno or request.service_id
    if sno:
        sno_str = str(sno)
        if sno_str in sno_to_sid:
            service_id = sno_to_sid[sno_str]
        elif sno_str in ["3", "4", "5", "7", "201"]:
            service_id = int(sno_str)

    # 4. Resolve history
    history = request.conversation_history
    if not history and request.messages:
        history = request.messages[:-1]

    # 5. Embed query and search language-agnostic ChromaDB via RAG module
    context_string, metadata_list = retrieve_context(
        query=query,
        service_id=service_id,
        top_k=6,
        english_query=english_query
    )

    # 6. Resolve fallback message and handle early exit for out-of-scope
    if query_lang == "en":
        fallback_msg = "Information not available."
    elif query_lang == "hi":
        fallback_msg = "जानकारी उपलब्ध नहीं है।"
    else:  # hinglish
        fallback_msg = "Jaankari uplabhd nahi hai."

    if not context_string:
        print(f"[API Chat] Context is empty (low similarity score). Returning early fallback message in language '{query_lang}': '{fallback_msg}'")
        return {"response": fallback_msg}

    if query_lang == "en":
        lang_label = "English"
        lang_instruction = (
            "You MUST respond ENTIRELY in English using only the Roman alphabet. "
            "Do NOT write in Devanagari script (Hindi characters) and do NOT use Hinglish words. "
            "Every single word must be standard English."
        )
    elif query_lang == "hi":
        lang_label = "Hindi"
        lang_instruction = (
            "You MUST respond ENTIRELY in Hindi using Devanagari script (देवनागरी लिपि). "
            "Do NOT write in English or use Roman alphabet/Latin characters. "
            "Every single word must be written in Devanagari."
        )
    else:  # hinglish
        lang_label = "Hinglish"
        lang_instruction = (
            "You MUST respond ENTIRELY in Hinglish (Hindi language written in Roman alphabet script). "
            "Do NOT use Devanagari script (Hindi characters) and do NOT write in pure English. "
            "All characters must be Roman/Latin letters. (Example: 'Aapka domicile certificate 7 din me banega')"
        )

    system_instruction = (
        "You are a helpful government services assistant for Sewa Setu Chhattisgarh portal.\n"
        "Answer the citizen's question using ONLY the provided context.\n"
        f"- The user's query language is {lang_label}.\n"
        f"- LANGUAGE AND SCRIPT RULES:\n"
        f"  {lang_instruction}\n"
        "- Translate the facts in the context into the target language specified above. Do not mix scripts or write in a script different from the target language rule.\n"
        "- Write a natural, conversational, and user-friendly answer. Do not just dump or copy-paste large blocks of raw text, page numbers, or metadata tags.\n"
        "- Avoid repetition: Do not repeat sentences, paragraphs, list items, or divisions. If the context has duplicate or redundant information, summarize it uniquely.\n"
        "- Be concise and factual. Do not hallucinate or make assumptions.\n"
        "- Do NOT output any thought process or intermediate reasoning inside <think> tags. Respond directly with the answer.\n"
        f"- FALLBACK RULE: If the answer is not in the context, you MUST output exactly: \"{fallback_msg}\"\n"
        "  Do not add any greetings, signatures, or extra words. Output only that exact fallback string.\n"
        "- Always mention the service name and department at the end of your answer in a natural way.\n\n"
        f"Relevant Context:\n{context_string}\n\n"
        f"FINAL REMINDER: {lang_instruction}"
    )

    messages_for_llm = [{"role": "system", "content": system_instruction}]
    if history:
        for msg in history:
            messages_for_llm.append({"role": msg.role, "content": msg.content})
    messages_for_llm.append({"role": "user", "content": query})

    # 7. Call Sarvam AI completions via LLM Router
    try:
        clean_reply = generate_answer(messages_for_llm)
        if not clean_reply.strip():
            # If the response is empty (e.g. stripped completely), fallback to default message
            clean_reply = fallback_msg
        return {"response": clean_reply}
    except Exception as e:
        print(f"[LLM] Exception occurred during generation: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/search")
async def search_services(request: SearchRequest):
    """
    Service classification mapping matching query to correct serial number 'sno'.
    Uses Sarvam AI to classify.
    """
    query = request.query.strip()
    if not query:
        return {"sno": None, "service_id": None}

    return classify_service(query, services_list)


@app.get("/health")
def health_check():
    """
    Returns API health status.
    """
    return {"status": "ok", "llm": "sarvam"}


@app.post("/api/ingest")
def trigger_ingestion(background_tasks: BackgroundTasks):
    """
    Simplified ingest endpoint.
    """
    return {"message": "Ingestion is already complete and vector database contains 282 chunks."}
