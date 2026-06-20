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

query = "sla for obs"
lang = "en"
service_id = 3
top_k = 8

context_string, metadata_list = retrieve_context(
    query=query,
    lang=lang,
    service_id=service_id,
    top_k=top_k
)

lang_label = "English" if lang == "en" else "Hindi"
system_instruction = (
    "You are a helpful government services assistant for Sewa Setu Chhattisgarh portal.\n"
    "Answer the citizen's question using ONLY the provided context.\n"
    f"- The user's question is in {lang_label}. Respond ONLY in {lang_label}. Do not mix languages.\n"
    "- Be concise and factual. Do not hallucinate.\n"
    "- Do NOT output any thought process or intermediate reasoning inside <think> tags. Respond directly with the answer.\n"
    f"- If the answer is not in the context, say exactly: \"{'Information not available.' if lang == 'en' else 'जानकारी उपलब्ध नहीं है।'}\"\n"
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

print("Sending request to Sarvam...")
try:
    response = requests.post(api_url, headers=headers, json=payload, timeout=60)
    print("Status Code:", response.status_code)
    print("Full Response JSON:")
    print(response.text)
except Exception as e:
    print("Error:", e)
