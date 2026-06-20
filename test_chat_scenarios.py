import requests
import json
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

url = "http://127.0.0.1:8000/api/chat"

scenarios = [
    # Scenario 1: Simple query with no selected_sno, language 'en'
    {"messages": [{"role": "user", "content": "sla for obs"}], "language": "en", "selected_sno": None},
    # Scenario 2: Simple query with selected_sno '5' (OBC)
    {"messages": [{"role": "user", "content": "sla for obs"}], "language": "en", "selected_sno": "5"},
    # Scenario 3: Simple query with selected_sno '7' (Domicile)
    {"messages": [{"role": "user", "content": "sla for obs"}], "language": "en", "selected_sno": "7"},
    # Scenario 4: Hindi query
    {"messages": [{"role": "user", "content": "sla for obs"}], "language": "hi", "selected_sno": None},
]

for idx, payload in enumerate(scenarios):
    print(f"\n--- Scenario {idx+1}: {payload} ---")
    try:
        res = requests.post(url, json=payload, timeout=45)
        print("Status code:", res.status_code)
        print("Response:", res.json())
    except Exception as e:
        print("Error:", e)
