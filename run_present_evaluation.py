import os
import sys
import json
import time
import requests

# Ensure stdout uses UTF-8
sys.stdout.reconfigure(encoding='utf-8')

API_URL = "http://localhost:8000/api/chat"
OUTPUT_FILE = "presentable_test_results.md"

# Import queries list from test_50_queries.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from test_50_queries import QUERIES
except ImportError as e:
    print("Error: Could not import QUERIES from test_50_queries.py:", e)
    sys.exit(1)

CATEGORIES = [
    {"name": "1. Domicile Certificate (Chhattisgarh Domicile Criteria)", "range": range(0, 8)},
    {"name": "2. Marriage Registration & Certificate", "range": range(8, 18)},
    {"name": "3. Scheduled Castes (SC) Order 1950", "range": range(18, 26)},
    {"name": "4. Scheduled Tribes (ST) Order 1950", "range": range(26, 34)},
    {"name": "5. Social Status Act (Caste Certificate Rules)", "range": range(34, 44)},
    {"name": "6. Ordinary Gazette Notification for Name Change", "range": range(44, 52)},
    {"name": "7. Out of Scope Queries", "range": range(52, 60)}
]

def query_chat_api(query_text, lang):
    payload = {
        "messages": [
            {"role": "user", "content": query_text}
        ],
        "language": lang
    }
    try:
        start_time = time.time()
        res = requests.post(API_URL, json=payload, timeout=90)
        elapsed = time.time() - start_time
        
        if res.status_code == 200:
            return res.json().get("response", "").strip(), elapsed
        else:
            return f"Error: API returned status {res.status_code} - {res.text}", elapsed
    except Exception as e:
        return f"Error connecting to API: {str(e)}", 0.0

def main():
    print(f"=== Starting Presentable Evaluation Suite ===")
    print(f"Total query pairs (EN & HI): {len(QUERIES)}")
    print(f"Output markdown file will be written to: {OUTPUT_FILE}")
    print("-" * 60)
    
    # Initialize output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# SewaSetu RAG Chatbot Evaluation Report\n\n")
        f.write("This report presents the testing results of the chatbot in both English and Hindi across all 5 in-scope citizen services and out-of-scope scenarios. Queries were executed globally without specifying service serial numbers.\n\n")
        f.write("## Test Configuration\n")
        f.write(f"- **API Server:** `{API_URL}`\n")
        f.write("- **Date & Time:** " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write(f"- **Total Query Runs:** {len(QUERIES) * 2} (60 English + 60 Hindi)\n\n")
        f.write("## Table of Contents\n")
        for cat in CATEGORIES:
            f.write(f"- [{cat['name']}](#{cat['name'].lower().replace(' ', '-').replace('(', '').replace(')', '').replace('.', '').replace('&', 'and')})\n")
        f.write("\n---\n\n")

    count = 0
    total_time = 0.0
    
    for cat in CATEGORIES:
        category_name = cat["name"]
        print(f"\n>>> Running Category: {category_name} ...")
        
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(f"## {category_name}\n\n")
        
        for idx in cat["range"]:
            if idx >= len(QUERIES):
                continue
            item = QUERIES[idx]
            q_num = idx + 1
            
            # --- 1. Query in English ---
            print(f"  [{q_num}.1] Querying EN: \"{item['en']}\"")
            ans_en, time_en = query_chat_api(item["en"], "en")
            total_time += time_en
            count += 1
            
            # --- 2. Query in Hindi ---
            print(f"  [{q_num}.2] Querying HI: \"{item['hi']}\"")
            ans_hi, time_hi = query_chat_api(item["hi"], "hi")
            total_time += time_hi
            count += 1
            
            # Write to Markdown
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(f"### Q{q_num}: {item['en']}\n\n")
                f.write(f"**Hindi Version:** *{item['hi']}*\n\n")
                
                f.write("#### 🇬🇧 English Response:\n")
                f.write("> " + ans_en.replace("\n", "\n> ") + "\n\n")
                f.write(f"*Latency: {time_en:.2f} seconds*\n\n")
                
                f.write("#### 🇮🇳 Hindi Response:\n")
                f.write("> " + ans_hi.replace("\n", "\n> ") + "\n\n")
                f.write(f"*Latency: {time_hi:.2f} seconds*\n\n")
                f.write("---\n\n")
            
            print(f"  Completed Q{q_num} (EN: {time_en:.1f}s | HI: {time_hi:.1f}s)")
            time.sleep(1.0)
            
    avg_time = total_time / count if count > 0 else 0.0
    
    # Write summary
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write("## Evaluation Summary & Metrics\n\n")
        f.write(f"- **Total Executed Queries:** {count}\n")
        f.write(f"- **Total Time Taken:** {total_time:.2f} seconds\n")
        f.write(f"- **Average Latency:** {avg_time:.2f} seconds/query\n")
        
    print("\n=== Evaluation Suite Completed Successfully! ===")
    print(f"Results written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
