import requests
import json
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

url = "http://127.0.0.1:8000/api/chat"

test_queries = [
    {
        "description": "English query (Name Change Gazette)",
        "payload": {
            "messages": [{"role": "user", "content": "what is the timeline for name change gazette?"}],
            "language": "en"
        }
    },
    {
        "description": "Hindi query (Marriage Registration Fee)",
        "payload": {
            "messages": [{"role": "user", "content": "विवाह पंजीकरण के लिए आवेदन शुल्क कितना है?"}],
            "language": "hi",
            "selected_sno": "1"
        }
    },
    {
        "description": "Hinglish query (Domicile Certificate Documents)",
        "payload": {
            "messages": [{"role": "user", "content": "domicile certificate banwane ke liye kya document chahiye?"}],
            "language": "en"
        }
    }
]

for idx, t in enumerate(test_queries):
    print(f"\n==================================================")
    print(f"Test {idx+1}: {t['description']}")
    print(f"Payload: {t['payload']}")
    print(f"==================================================")
    try:
        res = requests.post(url, json=t['payload'], timeout=60)
        print(f"Status Code: {res.status_code}")
        print("Response JSON:")
        print(json.dumps(res.json(), indent=2, ensure_ascii=False))
    except Exception as e:
        print("Error:", e)
