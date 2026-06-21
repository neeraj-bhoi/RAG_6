import os
import sys
import re
from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

from backend.llm_router import detect_query_language, translate_query_to_english
from backend.rag import retrieve_context

query = "क्या छत्तीसगढ़ में मूल निवासी प्रमाण पत्र प्राप्त करने के लिए मानदंड A और B दोनों आवश्यक हैं, और क्या इसके कोई अपवाद हैं?"

print(f"--- Debugging Query 3: '{query}' ---")
lang = detect_query_language(query)
print("Detected Language:", lang)

translated = translate_query_to_english(query)
print("Translated Query:", translated)

context, meta = retrieve_context(query=query, service_id=None, top_k=6, english_query=translated)
print("\nRetrieved Context:")
print(context)
