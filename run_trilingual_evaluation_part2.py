import os
import sys
import json
import time
import requests

# Ensure stdout uses UTF-8
sys.stdout.reconfigure(encoding='utf-8')

API_URL = "http://localhost:8000/api/chat"
OUTPUT_FILE = "trilingual_test_results_part2.md"

# Import queries list from test_50_trilingual_queries_part2.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
try:
    from test_50_trilingual_queries_part2 import TRILINGUAL_QUERIES_PART2
except ImportError as e:
    print("Error: Could not import TRILINGUAL_QUERIES_PART2 from test_50_trilingual_queries_part2.py:", e)
    sys.exit(1)

CATEGORIES = [
    {"name": "1. Domicile Certificate (Chhattisgarh Domicile Criteria)", "range": range(0, 8)},
    {"name": "2. Marriage Registration & Certificate", "range": range(8, 16)},
    {"name": "3. Scheduled Castes & Scheduled Tribes Order 1950", "range": range(16, 24)},
    {"name": "4. Social Status Act (Caste Certificate Rules)", "range": range(24, 32)},
    {"name": "5. Other Backward Classes (OBC) Certificate", "range": range(32, 40)},
    {"name": "6. Ordinary Gazette Notification for Name Change", "range": range(40, 46)},
    {"name": "7. Out of Scope Queries", "range": range(46, 50)}
]

def query_chat_api(query_text):
    payload = {
        "messages": [
            {"role": "user", "content": query_text}
        ]
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
    print(f"=== Starting Trilingual Evaluation Runner - Part 2 ===")
    print(f"Total query triplets (EN, HI, Hinglish): {len(TRILINGUAL_QUERIES_PART2)}")
    print(f"Output markdown file will be written to: {OUTPUT_FILE}")
    print("-" * 60)
    
    # Initialize output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# SewaSetu RAG Chatbot Trilingual Evaluation Report - Part 2\n\n")
        f.write("This report presents the second batch of testing results of the chatbot in three languages: **English**, **Hindi**, and **Hinglish** across all citizen services and out-of-scope scenarios. Queries were executed globally without specifying service serial numbers.\n\n")
        f.write("## Test Configuration\n")
        f.write(f"- **API Server:** `{API_URL}`\n")
        f.write("- **Date & Time:** " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write(f"- **Total Query Runs:** {len(TRILINGUAL_QUERIES_PART2) * 3} (50 English + 50 Hindi + 50 Hinglish)\n\n")
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
            if idx >= len(TRILINGUAL_QUERIES_PART2):
                continue
            item = TRILINGUAL_QUERIES_PART2[idx]
            q_num = idx + 1
            
            # --- 1. Query in English ---
            print(f"  [{q_num}.1] Querying EN: \"{item['en']}\"")
            ans_en, time_en = query_chat_api(item["en"])
            total_time += time_en
            count += 1
            
            # --- 2. Query in Hindi ---
            print(f"  [{q_num}.2] Querying HI: \"{item['hi']}\"")
            ans_hi, time_hi = query_chat_api(item["hi"])
            total_time += time_hi
            count += 1

            # --- 3. Query in Hinglish ---
            print(f"  [{q_num}.3] Querying Hinglish: \"{item['hinglish']}\"")
            ans_hinglish, time_hinglish = query_chat_api(item["hinglish"])
            total_time += time_hinglish
            count += 1
            
            # Write to Markdown
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(f"### Q{q_num}: {item['en']}\n\n")
                f.write(f"**Hindi:** *{item['hi']}*\n\n")
                f.write(f"**Hinglish:** *{item['hinglish']}*\n\n")
                
                f.write("#### 🇬🇧 English Response:\n")
                f.write("> " + ans_en.replace("\n", "\n> ") + "\n\n")
                f.write(f"*Latency: {time_en:.2f} seconds*\n\n")
                
                f.write("#### 🇮🇳 Hindi Response:\n")
                f.write("> " + ans_hi.replace("\n", "\n> ") + "\n\n")
                f.write(f"*Latency: {time_hi:.2f} seconds*\n\n")

                f.write("#### 💬 Hinglish Response:\n")
                f.write("> " + ans_hinglish.replace("\n", "\n> ") + "\n\n")
                f.write(f"*Latency: {time_hinglish:.2f} seconds*\n\n")
                f.write("---\n\n")
            
            print(f"  Completed Q{q_num} (EN: {time_en:.1f}s | HI: {time_hi:.1f}s | Hinglish: {time_hinglish:.1f}s)")
            time.sleep(1.0)
            
    avg_time = total_time / count if count > 0 else 0.0
    
    # Write summary
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write("## Evaluation Summary & Metrics\n\n")
        f.write(f"- **Total Executed Queries:** {count}\n")
        f.write(f"- **Total Time Taken:** {total_time:.2f} seconds\n")
        f.write(f"- **Average Latency:** {avg_time:.2f} seconds/query\n")
        
    print("\n=== Trilingual Evaluation Suite Part 2 Completed Successfully! ===")
    print(f"Results written to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
