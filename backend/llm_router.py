import os
import sys
import re
import json
import requests
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# Ensure stdout uses UTF-8 to prevent Windows-specific print crashes
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

# Sarvam AI API Configurations
sarvam_api_key = os.getenv("SARVAM_API_KEY", "")
sarvam_api_url = os.getenv("SARVAM_API_URL", "https://api.sarvam.ai/v1/chat/completions")
sarvam_model = os.getenv("SARVAM_MODEL", "sarvam-30b")


class ThinkStripper:
    def __init__(self):
        self.buffer = ""
        self.inside_think = False

    def feed(self, token: str) -> str:
        if token is None:
            token = ""
        self.buffer += token
        output = ""
        
        while True:
            if not self.inside_think:
                # Look for "<think>"
                idx = self.buffer.find("<think>")
                if idx != -1:
                    output += self.buffer[:idx]
                    self.buffer = self.buffer[idx + 7:]
                    self.inside_think = True
                else:
                    # Check for partial "<think" at the end of the buffer
                    partial_found = False
                    for i in range(1, min(len(self.buffer), 7)):
                        suffix = self.buffer[-i:]
                        if "<think>".startswith(suffix):
                            output += self.buffer[:-i]
                            self.buffer = suffix
                            partial_found = True
                            break
                    if not partial_found:
                        output += self.buffer
                        self.buffer = ""
                    break
            else:
                # Inside think, look for "</think>"
                idx = self.buffer.find("</think>")
                if idx != -1:
                    self.buffer = self.buffer[idx + 8:]
                    self.inside_think = False
                else:
                    # Check for partial "</think" at the end of the buffer
                    partial_found = False
                    for i in range(1, min(len(self.buffer), 8)):
                        suffix = self.buffer[-i:]
                        if "</think>".startswith(suffix):
                            self.buffer = suffix
                            partial_found = True
                            break
                    if not partial_found:
                        self.buffer = ""
                    break
        return output

    def flush(self) -> str:
        if not self.inside_think:
            res = self.buffer
            self.buffer = ""
            return res
        return ""


def generate_answer(messages: List[Dict[str, str]]) -> str:
    """
    Calls Sarvam AI completions (non-streaming, max_tokens=2048) and strips thinking blocks.
    """
    if not sarvam_api_key:
        print("[LLM Router] Warning: SARVAM_API_KEY is not set.")

    headers = {
        "api-subscription-key": sarvam_api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "model": sarvam_model,
        "messages": messages,
        "temperature": 0.0,
        "stream": False,
        "max_tokens": 4096
    }
    
    print(f"[LLM Router] Calling Sarvam AI completions...")
    response = requests.post(sarvam_api_url, headers=headers, json=payload, timeout=180)
    
    if response.status_code != 200:
        print(f"[LLM Router] Sarvam AI returned status {response.status_code}: {response.text}")
        raise ValueError(f"Sarvam AI returned status {response.status_code}")

    res_json = response.json()
    choices = res_json.get("choices", [])
    reply_content = ""
    if choices:
        message_obj = choices[0].get("message", {})
        reply_content = message_obj.get("content") or ""
    
    # Strip reasoning tags
    stripper = ThinkStripper()
    clean_reply = stripper.feed(reply_content) + stripper.flush()
    return clean_reply.strip()


def detect_query_language(query: str) -> str:
    """
    Calls Sarvam AI to detect if the query is in English, Hindi, or Hinglish.
    Returns: 'en', 'hi', or 'hinglish'.
    """
    if not query:
        return 'en'
        
    prompt = (
        "Identify the language of the following user query.\n"
        "The language can be English, Hindi (in Devanagari script), or Hinglish (Hindi written in Roman/Latin script).\n\n"
        f"Query: '{query}'\n\n"
        "Instructions:\n"
        "- Respond with EXACTLY one of these three strings: 'english', 'hindi', or 'hinglish'.\n"
        "- Do not explain your answer. Do not include formatting or markdown. Only return the lowercase word.\n\n"
        "Language:"
    )

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 2048
        }
        
        print(f"[LLM Router] Calling language detection endpoint...")
        res = requests.post(sarvam_api_url, headers=headers, json=payload, timeout=45)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            reasoning = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
                reasoning = message_obj.get("reasoning_content") or ""
            
            print(f"[LLM Router] Language detection raw reply: '{reply}'")
            print(f"[LLM Router] Language detection raw reasoning: '{reasoning}'")
            reply_lower = reply.strip().lower()
            reasoning_lower = reasoning.strip().lower()
            
            # Strip reasoning tags if present in reply
            stripper = ThinkStripper()
            reply_clean = stripper.feed(reply_lower) + stripper.flush()
            reply_clean = reply_clean.strip()

            print(f"[LLM Router] Language detection stripped reply: '{reply_clean}'")
            
            # 1. Check stripped response
            if 'hinglish' in reply_clean:
                return 'hinglish'
            elif 'hindi' in reply_clean:
                return 'hi'
            elif 'english' in reply_clean or 'en' in reply_clean:
                return 'en'
                
            # 2. Fallback: check raw content response
            if 'hinglish' in reply_lower:
                return 'hinglish'
            elif 'hindi' in reply_lower:
                return 'hi'
            elif 'english' in reply_lower or 'en' in reply_lower:
                return 'en'

            # 3. Fallback: check reasoning_content
            if 'hinglish' in reasoning_lower:
                return 'hinglish'
            elif 'hindi' in reasoning_lower:
                return 'hi'
            elif 'english' in reasoning_lower or 'en' in reasoning_lower:
                return 'en'
    except Exception as e:
        print(f"[LLM Router] Language detection failed: {e}")
        
    # Basic unicode fallback
    for char in query:
        if '\u0900' <= char <= '\u097F':
            return 'hi'
            
            
    return 'en'


def translate_query_to_english(query: str) -> str:
    """
    Translates a Hindi or Hinglish query to English using Sarvam's translation API.
    """
    if not query:
        return ""

    try:
        url = "https://api.sarvam.ai/translate"
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "input": query,
            "source_language_code": "hi-IN",
            "target_language_code": "en-IN",
            "model": "sarvam-translate:v1"
        }
        
        print(f"[LLM Router] Calling Sarvam Translation API for: '{query}'...")
        res = requests.post(url, headers=headers, json=payload, timeout=30)
        if res.status_code == 200:
            translated_text = res.json().get("translated_text", "").strip()
            if translated_text:
                print(f"[LLM Router] Translated query to: '{translated_text}'")
                return translated_text
        else:
            print(f"[LLM Router] Sarvam Translation API returned status {res.status_code}: {res.text}")
    except Exception as e:
        print(f"[LLM Router] Query translation failed: {e}")
        
    return query


def classify_service(query: str, services_list: List[Dict[str, Any]]) -> Dict[str, Optional[str]]:
    """
    Service classification mapping matching query to correct serial number 'sno'.
    Uses Sarvam AI to classify and maps to catalog services.
    """
    if not query:
        return {"sno": None, "service_id": None}

    services_catalog_desc = "\n".join([
        f"{s['sno']}. Serial Number {s['sno']} (Service ID: {s['service_id']}): {s['name_en']} | {s['name_hi']}"
        for s in services_list
    ])

    prompt = (
        "You are an expert service mapping assistant for the SewaSetu Chhattisgarh portal.\n"
        "Your task is to identify which specific service from the catalog is the closest match to the user query.\n"
        "The query could be in English, Hindi, or Hinglish.\n\n"
        "Here is the catalog of services:\n"
        f"{services_catalog_desc}\n\n"
        f"User Query: '{query}'\n\n"
        "Instructions:\n"
        "- Match the query to a service ONLY if the query explicitly mentions or clearly targets that specific service.\n"
        "- If the query is generic, ambiguous, or does not clearly map to a specific service, return {\"sno\": null, \"service_id\": null}.\n"
        "- Return ONLY a JSON object containing the mapped 'sno' and 'service_id' as strings. For example: {\"sno\": \"1\", \"service_id\": \"3\"}\n"
        "- Do not explain your choice. Do not output markdown, only raw JSON.\n\n"
        "Output JSON:"
    )

    try:
        headers = {
            "api-subscription-key": sarvam_api_key,
            "Content-Type": "application/json"
        }
        payload = {
            "model": sarvam_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0,
            "stream": False,
            "max_tokens": 512
        }
        
        print(f"[LLM Router] Calling classification endpoint...")
        res = requests.post(sarvam_api_url, headers=headers, json=payload, timeout=30)
        if res.status_code == 200:
            choices = res.json().get("choices", [])
            reply = ""
            if choices:
                message_obj = choices[0].get("message", {})
                reply = message_obj.get("content") or ""
            reply = reply.strip()
            
            # Strip reasoning tags
            stripper = ThinkStripper()
            reply = stripper.feed(reply) + stripper.flush()
            reply = reply.strip()

            json_match = re.search(r'\{.*?\}', reply, re.DOTALL)
            if json_match:
                json_data = json.loads(json_match.group(0))
                sno_val = json_data.get("sno")
                sid_val = json_data.get("service_id")
                if sno_val and str(sno_val).lower() != "null":
                    # Validate that the sno matches a valid sno in services
                    valid_snos = {str(s["sno"]) for s in services_list}
                    if str(sno_val) in valid_snos:
                        return {
                            "sno": str(sno_val),
                            "service_id": str(sid_val) if sid_val else None
                        }
    except Exception as e:
        print(f"[LLM Router] Service mapping classification failed: {e}")

    return {"sno": None, "service_id": None}
