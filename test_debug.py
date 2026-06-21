import os
import sys
from dotenv import load_dotenv

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

load_dotenv()

# Import logic
from backend.rag import retrieve_context
from backend.llm_router import generate_answer, classify_service, detect_query_language

print("--- Step 1: Testing language detection ---")
queries = [
    "what is the timeline for name change gazette?",
    "विवाह पंजीकरण के लिए आवेदन शुल्क कितना है?",
    "domicile certificate banwane ke liye kya document chahiye?"
]

for q in queries:
    try:
        lang = detect_query_language(q)
        print(f"Query: '{q}' | Detected Lang: '{lang}'")
    except Exception as e:
        print(f"Query: '{q}' | Detection Failed: {e}")

print("\n--- Step 2: Testing RAG context retrieval ---")
for q in queries:
    try:
        ctx, meta = retrieve_context(query=q, service_id=None, top_k=6)
        print(f"Query: '{q}' | Retrieved Chunks: {len(meta)}")
    except Exception as e:
        print(f"Query: '{q}' | Retrieval Failed: {e}")

print("\n--- Step 3: Full pipeline test for Hindi query ---")
q_hi = "विवाह पंजीकरण के लिए आवेदन शुल्क कितना है?"
try:
    lang = detect_query_language(q_hi)
    print("Detected lang:", lang)
    ctx, meta = retrieve_context(query=q_hi, service_id=None, top_k=6)
    print("Context retrieved length:", len(ctx))
    
    if lang == "en":
        lang_label = "English"
        lang_instruction = "Respond ONLY in English. Do not mix languages."
        fallback_msg = "Information not available."
    elif lang == "hi":
        lang_label = "Hindi"
        lang_instruction = "Respond ONLY in Hindi (Devanagari script). Do not mix languages."
        fallback_msg = "जानकारी उपलब्ध नहीं है।"
    else:
        lang_label = "Hinglish"
        lang_instruction = "Respond ONLY in Hinglish (Hindi language written in Roman script). Do not mix languages."
        fallback_msg = "Jaankari uplabhd nahi hai."

    system_instruction = (
        "You are a helpful government services assistant for Sewa Setu Chhattisgarh portal.\n"
        "Answer the citizen's question using ONLY the provided context.\n"
        f"- The user's question is in {lang_label}. {lang_instruction}\n"
        "- Be concise and factual. Do not hallucinate.\n"
        "- Do NOT output any thought process or intermediate reasoning inside <think> tags. Respond directly with the answer.\n"
        f"- If the answer is not in the context, say exactly: \"{fallback_msg}\"\n"
        "- For document lists, format as a numbered list.\n"
        "- Always mention the service name and department at the end of your answer.\n\n"
        f"Relevant Context:\n{ctx}\n"
    )
    
    messages = [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": q_hi}
    ]
    
    print("Calling generate_answer...")
    ans = generate_answer(messages)
    print("Answer:")
    print(ans)
except Exception as e:
    import traceback
    traceback.print_exc()
