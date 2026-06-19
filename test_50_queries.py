import os
import sys
import json
import time
import requests

# Set stdout encoding to UTF-8 to prevent console printing crashes on Windows
sys.stdout.reconfigure(encoding='utf-8')

API_URL = "http://localhost:8000/api/chat"
RESULTS_FILE = "test_results.md"

QUERIES = [
    # 1. Marriage Registration & Certificate
    {
        "id": 1,
        "category": "Marriage Certificate",
        "en": "What are the required documents for marriage certificate?",
        "hi": "विवाह प्रमाण पत्र के लिए आवश्यक दस्तावेज क्या हैं?"
    },
    {
        "id": 2,
        "category": "Marriage Certificate",
        "en": "How much is the fee for marriage registration?",
        "hi": "विवाह पंजीकरण के लिए शुल्क कितना है?"
    },
    {
        "id": 3,
        "category": "Marriage Certificate",
        "en": "What is the time limit or SLA for marriage certificate?",
        "hi": "विवाह प्रमाण पत्र के लिए समय सीमा (SLA) क्या है?"
    },
    {
        "id": 4,
        "category": "Marriage Certificate",
        "en": "Who is the issuing authority for marriage certificate?",
        "hi": "विवाह प्रमाण पत्र के लिए जारीकर्ता प्राधिकारी कौन है?"
    },
    {
        "id": 5,
        "category": "Marriage Certificate",
        "en": "Where can I apply for marriage registration?",
        "hi": "मैं विवाह पंजीकरण के लिए कहाँ आवेदन कर सकता हूँ?"
    },
    {
        "id": 6,
        "category": "Marriage Certificate",
        "en": "Is there any offline application mode for marriage certificate?",
        "hi": "क्या विवाह प्रमाण पत्र के लिए कोई ऑफलाइन आवेदन मोड है?"
    },
    # 2. SC/ST Certificate
    {
        "id": 7,
        "category": "SC/ST Certificate",
        "en": "What documents are required to apply for SC/ST certificate?",
        "hi": "अनुसूचित जाति/जनजाति प्रमाण पत्र के लिए आवेदन करने के लिए कौन से दस्तावेज आवश्यक हैं?"
    },
    {
        "id": 8,
        "category": "SC/ST Certificate",
        "en": "What is the fee for SC/ST certificate application?",
        "hi": "अनुसूचित जाति/जनजाति प्रमाण पत्र आवेदन के लिए शुल्क क्या है?"
    },
    {
        "id": 9,
        "category": "SC/ST Certificate",
        "en": "How many days does it take to process an SC/ST certificate?",
        "hi": "अनुसूचित जाति/जनजाति प्रमाण पत्र को संसाधित करने में कितने दिन लगते हैं?"
    },
    {
        "id": 10,
        "category": "SC/ST Certificate",
        "en": "Who is eligible for SC/ST certificate in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में अनुसूचित जाति/जनजाति प्रमाण पत्र के लिए कौन पात्र है?"
    },
    {
        "id": 11,
        "category": "SC/ST Certificate",
        "en": "Who is the contact person or authority for SC/ST certificate?",
        "hi": "अनुसूचित जाति/जनजाति प्रमाण पत्र के लिए संपर्क व्यक्ति या प्राधिकारी कौन है?"
    },
    # 3. OBC Certificate
    {
        "id": 12,
        "category": "OBC Certificate",
        "en": "What documents are needed for OBC certificate?",
        "hi": "अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए कौन से दस्तावेज आवश्यक हैं?"
    },
    {
        "id": 13,
        "category": "OBC Certificate",
        "en": "What is the processing time or SLA for OBC certificate?",
        "hi": "ओबीसी प्रमाण पत्र के लिए प्रसंस्करण समय या SLA क्या है?"
    },
    {
        "id": 14,
        "category": "OBC Certificate",
        "en": "What is the application fee for OBC certificate?",
        "hi": "ओबीसी प्रमाण पत्र के लिए आवेदन शुल्क क्या है?"
    },
    {
        "id": 15,
        "category": "OBC Certificate",
        "en": "What are the rules for OBC certificate eligibility?",
        "hi": "ओबीसी प्रमाण पत्र पात्रता के लिए क्या नियम हैं?"
    },
    {
        "id": 16,
        "category": "OBC Certificate",
        "en": "Where to apply for OBC certificate online?",
        "hi": "ओबीसी प्रमाण पत्र के लिए ऑनलाइन आवेदन कहाँ करें?"
    },
    # 4. Income Certificate
    {
        "id": 17,
        "category": "Income Certificate",
        "en": "What is the required documents list for Income Certificate?",
        "hi": "आय प्रमाण पत्र के लिए आवश्यक दस्तावेजों की सूची क्या है?"
    },
    {
        "id": 18,
        "category": "Income Certificate",
        "en": "How long does it take to get an Income Certificate?",
        "hi": "आय प्रमाण पत्र प्राप्त करने में कितना समय लगता है?"
    },
    {
        "id": 19,
        "category": "Income Certificate",
        "en": "What are the application fees for income certificate?",
        "hi": "आय प्रमाण पत्र के लिए आवेदन शुल्क क्या है?"
    },
    {
        "id": 20,
        "category": "Income Certificate",
        "en": "Who is the competent authority to issue income certificate?",
        "hi": "आय प्रमाण पत्र जारी करने के लिए सक्षम प्राधिकारी कौन है?"
    },
    {
        "id": 21,
        "category": "Income Certificate",
        "en": "What is the validity of income certificate?",
        "hi": "आय प्रमाण पत्र की वैधता क्या है?"
    },
    # 5. Domicile Certificate
    {
        "id": 22,
        "category": "Domicile Certificate",
        "en": "What are the documents required for domicile certificate?",
        "hi": "मूल निवासी प्रमाण पत्र के लिए आवश्यक दस्तावेज क्या हैं?"
    },
    {
        "id": 23,
        "category": "Domicile Certificate",
        "en": "What is the SLA processing time for domicile certificate?",
        "hi": "मूल निवासी प्रमाण पत्र के लिए SLA प्रसंस्करण समय क्या है?"
    },
    {
        "id": 24,
        "category": "Domicile Certificate",
        "en": "How much is the fee for domicile certificate?",
        "hi": "मूल निवासी प्रमाण पत्र के लिए शुल्क कितना है?"
    },
    {
        "id": 25,
        "category": "Domicile Certificate",
        "en": "What is the eligibility criteria for domicile in CG?",
        "hi": "छत्तीसगढ़ में मूल निवासी के लिए पात्रता मानदंड क्या हैं?"
    },
    {
        "id": 26,
        "category": "Domicile Certificate",
        "en": "Can I apply for domicile certificate online?",
        "hi": "क्या मैं मूल निवासी प्रमाण पत्र के लिए ऑनलाइन आवेदन कर सकता हूँ?"
    },
    # 6. Water Tap Connection
    {
        "id": 27,
        "category": "Water Connection",
        "en": "What documents are required for new water tap connection?",
        "hi": "नए नल कनेक्शन के लिए कौन से दस्तावेज आवश्यक हैं?"
    },
    {
        "id": 28,
        "category": "Water Connection",
        "en": "How much is the fee for new water tap connection?",
        "hi": "नए नल कनेक्शन के लिए शुल्क कितना है?"
    },
    {
        "id": 29,
        "category": "Water Connection",
        "en": "What is the processing time or SLA for water tap connection?",
        "hi": "नल कनेक्शन के लिए प्रसंस्करण समय या SLA क्या है?"
    },
    {
        "id": 30,
        "category": "Water Connection",
        "en": "Where do I apply for new water tap connection?",
        "hi": "मैं नए नल कनेक्शन के लिए कहाँ आवेदन करूँ?"
    },
    {
        "id": 31,
        "category": "Water Connection",
        "en": "Who issues the approval for water tap connection?",
        "hi": "नल कनेक्शन के लिए मंजूरी कौन जारी करता है?"
    },
    # 7. Ordinary Gazette Notification for Name Change
    {
        "id": 32,
        "category": "Gazette Name Change",
        "en": "What are the required documents for name change gazette notification?",
        "hi": "नाम परिवर्तन राजपत्र अधिसूचना के लिए आवश्यक दस्तावेज क्या हैं?"
    },
    {
        "id": 33,
        "category": "Gazette Name Change",
        "en": "What is the kiosk fee and online fee for name change gazette?",
        "hi": "नाम परिवर्तन राजपत्र के लिए किओस्क शुल्क और ऑनलाइन शुल्क क्या है?"
    },
    {
        "id": 34,
        "category": "Gazette Name Change",
        "en": "How many days does it take for name change gazette notification?",
        "hi": "नाम परिवर्तन राजपत्र अधिसूचना में कितने दिन लगते हैं?"
    },
    {
        "id": 35,
        "category": "Gazette Name Change",
        "en": "Where to apply for ordinary gazette notification for name change?",
        "hi": "नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना के लिए कहाँ आवेदन करें?"
    },
    {
        "id": 36,
        "category": "Gazette Name Change",
        "en": "Who is the contact authority for name change gazette?",
        "hi": "नाम परिवर्तन राजपत्र के लिए संपर्क प्राधिकारी कौन है?"
    },
    # 8. Chief Minister Employment Generation Programme (CMEGP)
    {
        "id": 37,
        "category": "CMEGP Scheme",
        "en": "What documents are required to apply for CMEGP?",
        "hi": "CMEGP के लिए आवेदन करने के लिए कौन से दस्तावेज आवश्यक हैं?"
    },
    {
        "id": 38,
        "category": "CMEGP Scheme",
        "en": "What is the fee for CMEGP application?",
        "hi": "CMEGP आवेदन के लिए शुल्क क्या है?"
    },
    {
        "id": 39,
        "category": "CMEGP Scheme",
        "en": "What is the SLA for CMEGP scheme process?",
        "hi": "CMEGP योजना प्रक्रिया के लिए SLA क्या है?"
    },
    {
        "id": 40,
        "category": "CMEGP Scheme",
        "en": "Who is eligible under the CMEGP scheme?",
        "hi": "CMEGP योजना के तहत कौन पात्र है?"
    },
    {
        "id": 41,
        "category": "CMEGP Scheme",
        "en": "Where can I apply for CMEGP?",
        "hi": "मैं CMEGP के लिए कहाँ आवेदन कर सकता हूँ?"
    },
    {
        "id": 42,
        "category": "CMEGP Scheme",
        "en": "Who is the implementing department for CMEGP?",
        "hi": "CMEGP के लिए कार्यान्वयन विभाग कौन सा है?"
    },
    # 9. Feature Film Subsidy
    {
        "id": 43,
        "category": "Film Subsidy",
        "en": "What are the required documents for feature film subsidy?",
        "hi": "फीचर फिल्म सब्सिडी के लिए आवश्यक दस्तावेज क्या हैं?"
    },
    {
        "id": 44,
        "category": "Film Subsidy",
        "en": "What is the fee for feature film subsidy application?",
        "hi": "फीचर फिल्म सब्सिडी आवेदन के लिए शुल्क क्या है?"
    },
    {
        "id": 45,
        "category": "Film Subsidy",
        "en": "What is the SLA or processing time for film subsidy?",
        "hi": "फिल्म सब्सिडी के लिए SLA या प्रसंस्करण समय क्या है?"
    },
    {
        "id": 46,
        "category": "Film Subsidy",
        "en": "Who is eligible for feature film subsidy in CG?",
        "hi": "छत्तीसगढ़ में फीचर फिल्म सब्सिडी के लिए कौन पात्र है?"
    },
    {
        "id": 47,
        "category": "Film Subsidy",
        "en": "Which department is responsible for film subsidy?",
        "hi": "फिल्म सब्सिडी के लिए कौन सा विभाग जिम्मेदार है?"
    },
    # 10. Out of Scope (Testing Strict Context adherence)
    {
        "id": 48,
        "category": "Out of Scope",
        "en": "How do I apply for a driver license?",
        "hi": "ड्राइविंग लाइसेंस के लिए आवेदन कैसे करें?"
    },
    {
        "id": 49,
        "category": "Out of Scope",
        "en": "What is the process for passport application?",
        "hi": "पासपोर्ट आवेदन की प्रक्रिया क्या है?"
    },
    {
        "id": 50,
        "category": "Out of Scope",
        "en": "How to get a birth certificate?",
        "hi": "जन्म प्रमाण पत्र कैसे प्राप्त करें?"
    }
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
    print("=== Starting SewaSetu Chatbot Evaluation Suite ===")
    print(f"Total query pairs (EN & HI): {len(QUERIES)}")
    print(f"Results will be appended incrementally to: {RESULTS_FILE}")
    print("-" * 50)
    
    # Initialize/overwrite markdown file with header
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write("# SewaSetu RAG Chatbot Evaluation Report\n\n")
        f.write("This report presents the testing results of the chatbot in both English and Hindi for 50 diverse queries.\n\n")
        f.write("## Test Parameters\n")
        f.write(f"- **API Endpoint:** `{API_URL}`\n")
        f.write("- **Date & Time:** " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write(f"- **Total Query Runs:** {len(QUERIES) * 2} (50 English + 50 Hindi)\n\n")
        f.write("## Test Results by Category\n\n")
        f.write("| ID | Category | Language | Query | Generated Answer | Time (s) |\n")
        f.write("| --- | --- | --- | --- | --- | --- |\n")

    count = 0
    total_time = 0.0
    
    for idx, item in enumerate(QUERIES):
        q_id = item["id"]
        category = item["category"]
        
        # 1. Test English Query
        print(f"[{idx+1}/{len(QUERIES)}] Querying EN: \"{item['en']}\" ...")
        ans_en, time_en = query_chat_api(item["en"], "en")
        total_time += time_en
        count += 1
        
        # Append English Result
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            # Escape newlines for table cells
            escaped_ans_en = ans_en.replace("\n", "<br>")
            f.write(f"| {q_id} | {category} | EN | {item['en']} | {escaped_ans_en} | {time_en:.2f} |\n")
        
        # 2. Test Hindi Query
        print(f"[{idx+1}/{len(QUERIES)}] Querying HI: \"{item['hi']}\" ...")
        ans_hi, time_hi = query_chat_api(item["hi"], "hi")
        total_time += time_hi
        count += 1
        
        # Append Hindi Result
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            escaped_ans_hi = ans_hi.replace("\n", "<br>")
            f.write(f"| {q_id} | {category} | HI | {item['hi']} | {escaped_ans_hi} | {time_hi:.2f} |\n")
            
        print(f"Completed query pair {q_id} (EN: {time_en:.1f}s | HI: {time_hi:.1f}s)")
        print("-" * 30)
        
        # Slight pause to avoid spamming the endpoint too fast
        time.sleep(1.0)
        
    avg_time = total_time / count if count > 0 else 0.0
    
    # Write summary
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write("\n## Summary & Statistics\n\n")
        f.write(f"- **Total Executed Queries:** {count}\n")
        f.write(f"- **Total Time Elapsed:** {total_time:.2f} seconds\n")
        f.write(f"- **Average Response Time:** {avg_time:.2f} seconds/query\n")
        
    print("\n=== Evaluation Suite Completed Successfully! ===")
    print(f"Results written to: {RESULTS_FILE}")

if __name__ == "__main__":
    main()
