import os
import sys
import requests
from dotenv import load_dotenv

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

load_dotenv()

api_key = os.getenv("SARVAM_API_KEY")
api_url = os.getenv("SARVAM_API_URL", "https://api.sarvam.ai/v1/chat/completions")
model = os.getenv("SARVAM_MODEL", "sarvam-30b")

query = "domicile certificate banwane ke liye kya document chahiye?"
prompt = (
    "Identify the language of the following user query.\n"
    "The language can be English, Hindi (in Devanagari script), or Hinglish (Hindi written in Roman/Latin script).\n\n"
    f"Query: '{query}'\n\n"
    "Instructions:\n"
    "- Respond with EXACTLY one of these three strings: 'english', 'hindi', or 'hinglish'.\n"
    "- Do not explain your answer. Do not include formatting or markdown. Only return the lowercase word.\n\n"
    "Language:"
)

headers = {
    "api-subscription-key": api_key,
    "Content-Type": "application/json"
}
payload = {
    "model": model,
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.0,
    "stream": False,
    "max_tokens": 128
}

print("Calling Sarvam for language detection...")
res = requests.post(api_url, headers=headers, json=payload, timeout=30)
print("Status Code:", res.status_code)
print("Response Text:")
print(res.text)
