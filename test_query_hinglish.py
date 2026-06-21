import os
import sys
import requests
from dotenv import load_dotenv
from backend.rag import retrieve_context

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

load_dotenv()

api_key = os.getenv("SARVAM_API_KEY")
api_url = os.getenv("SARVAM_API_URL", "https://api.sarvam.ai/v1/chat/completions")
model = os.getenv("SARVAM_MODEL", "sarvam-30b")

query = "domicile certificate banwane ke liye kya document chahiye?"
lang = "hinglish"
service_id = None
top_k = 6

context_string, metadata_list = retrieve_context(
    query=query,
    service_id=service_id,
    top_k=top_k
)

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
    f"Relevant Context:\n{context_string}\n"
)

messages = [
    {"role": "system", "content": system_instruction},
    {"role": "user", "content": query}
]

headers = {
    "api-subscription-key": api_key,
    "Content-Type": "application/json"
}

payload = {
    "model": model,
    "messages": messages,
    "temperature": 0.0,
    "stream": False,
    "max_tokens": 2048
}

print("Calling Sarvam for Hinglish RAG query...")
res = requests.post(api_url, headers=headers, json=payload, timeout=90)
print("Status Code:", res.status_code)
print("Response Text:")
print(res.text)
