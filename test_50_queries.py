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
    # 1. Domicile Certificate (Chhattisgarh Domicile Criteria)
    {
        "en": "What is the parent's continuous residence requirement for Chhattisgarh domicile?",
        "hi": "छत्तीसगढ़ में मूल निवासी के लिए माता-पिता के लिए निरंतर निवास की आवश्यकता क्या है?"
    },
    {
        "en": "If a parent owns property in Chhattisgarh for 5 years but the applicant did not study in Chhattisgarh, are they eligible for domicile?",
        "hi": "यदि माता-पिता के पास छत्तीसगढ़ में 5 वर्षों से संपत्ति है, लेकिन आवेदक ने छत्तीसगढ़ में पढ़ाई नहीं की है, तो क्या वे मूल निवासी के लिए पात्र हैं?"
    },
    {
        "en": "Are both Criteria A and B required to get a Domicile Certificate in Chhattisgarh, and are there any exceptions?",
        "hi": "क्या छत्तीसगढ़ में मूल निवासी प्रमाण पत्र प्राप्त करने के लिए मानदंड A और B दोनों आवश्यक हैं, और क्या इसके कोई अपवाद हैं?"
    },
    {
        "en": "Is a person whose spouse is a domicile of Chhattisgarh eligible for domicile, and are criteria A and B required for them?",
        "hi": "क्या वह व्यक्ति जिसका जीवनसाथी छत्तीसगढ़ का मूल निवासी है, मूल निवासी प्रमाण पत्र के लिए पात्र है, और क्या उनके लिए मानदंड A और B आवश्यक हैं?"
    },
    {
        "en": "What are the board exams accepted under Criteria B for establishing domicile in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में मूल निवासी स्थापित करने के लिए मानदंड B के तहत कौन सी बोर्ड परीक्षाएं स्वीकार की जाती हैं?"
    },
    {
        "en": "If an applicant is an All India Services officer allotted Chhattisgarh Cadre, do they need to meet Criteria A and B?",
        "hi": "यदि कोई आवेदक अखिल भारतीय सेवा का अधिकारी है और उसे छत्तीसगढ़ कैडर आवंटित किया गया है, तो क्या उसे मानदंड A and B को पूरा करने की आवश्यकता है?"
    },
    {
        "en": "List all required documents for applying for a Domicile Certificate in Chhattisgarh.",
        "hi": "छत्तीसगढ़ में मूल निवासी प्रमाण पत्र के लिए आवेदन करने के लिए आवश्यक सभी दस्तावेजों की सूची क्या है?"
    },
    {
        "en": "Does birth in Chhattisgarh alone qualify a person for a domicile certificate?",
        "hi": "क्या केवल छत्तीसगढ़ में जन्म होना ही किसी व्यक्ति को मूल निवासी प्रमाण पत्र के लिए योग्य बनाता है?"
    },
    # 2. Marriage Registration
    {
        "en": "What is the time limit for submitting the marriage registration memorandum to the Registrar in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में रजिस्ट्रार को विवाह पंजीकरण ज्ञापन सौंपने की समय सीमा क्या है?"
    },
    {
        "en": "What is the penalty under Rule 12 for willfully failing to submit the marriage memorandum?",
        "hi": "विवाह ज्ञापन प्रस्तुत करने में जानबूझकर विफल रहने पर नियम 12 के तहत क्या जुर्माना है?"
    },
    {
        "en": "What is the penalty under Rule 13 for destroying or tampering with the marriage register?",
        "hi": "विवाह रजिस्टर को नष्ट करने या उससे छेड़छाड़ करने पर नियम 13 के तहत क्या जुर्माना है?"
    },
    {
        "en": "If a marriage is not registered, does it become invalid in the state of Chhattisgarh under these rules?",
        "hi": "यदि विवाह पंजीकृत नहीं है, तो क्या वह इन नियमों के तहत छत्तीसगढ़ राज्य में अमान्य हो जाता है?"
    },
    {
        "en": "What is the appeal process, fee, and timeline if the Marriage Registrar refuses to register a marriage?",
        "hi": "यदि विवाह रजिस्ट्रार विवाह पंजीकृत करने से इनकार करता है तो अपील प्रक्रिया, शुल्क और समय सीमा क्या है?"
    },
    {
        "en": "Who is the designated Marriage Registrar for a local area in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में किसी स्थानीय क्षेत्र के लिए मनोनीत विवाह रजिस्ट्रार कौन है?"
    },
    {
        "en": "Under what rule and fee can a member of the public inspect the Register of Marriages?",
        "hi": "जनता किस नियम और शुल्क के तहत विवाह रजिस्टर का निरीक्षण कर सकती है?"
    },
    {
        "en": "Does the definition of marriage under the Chhattisgarh Rules include remarriages, and does it apply to all religions?",
        "hi": "क्या छत्तीसगढ़ नियमों के तहत विवाह की परिभाषा में पुनर्विवाह शामिल है, और क्या यह सभी धर्मों पर लागू होता है?"
    },
    {
        "en": "Can an employer update their office records regarding an employee's marital status without a marriage registration certificate?",
        "hi": "क्या कोई नियोक्ता विवाह पंजीकरण प्रमाणपत्र के बिना किसी कर्मचारी की वैवाहिक स्थिति के संबंध में अपने कार्यालय के रिकॉर्ड को अपडेट कर सकता है?"
    },
    {
        "en": "Who is the final appellate authority if the Chief Registrar confirms the refusal to register a marriage?",
        "hi": "यदि मुख्य रजिस्ट्रार विवाह पंजीकृत करने से इनकार करने के आदेश की पुष्टि करता है, तो अंतिम अपीलीय प्राधिकारी कौन होता है?"
    },
    # 3. Scheduled Castes Order
    {
        "en": "According to Paragraph 3 of the Constitution (Scheduled Castes) Order 1950, which religions must a person profess to be deemed a Scheduled Caste?",
        "hi": "संविधान (अनुसूचित जाति) आदेश 1950 के पैराग्राफ 3 के अनुसार, कोई व्यक्ति किस धर्म को मानने पर ही अनुसूचित जाति का सदस्य माना जा सकता है?"
    },
    {
        "en": "Is 'Audhelia' recognized as a Scheduled Caste in the State of Chhattisgarh under Part XVIIIL of the 1950 Order?",
        "hi": "क्या 1950 के आदेश के भाग XVIIIL के तहत छत्तीसगढ़ राज्य में 'औधेलिया' (Audhelia) को अनुसूचित जाति के रूप में मान्यता प्राप्त है?"
    },
    {
        "en": "Under which entry number are castes like Jatav, Mochi, Regar, Satnami, and Ramnami listed for Chhattisgarh in the SC Order 1950?",
        "hi": "अनुसूचित जाति आदेश 1950 में छत्तीसगढ़ के लिए जाटव, मोची, रेगर, सतनामी और रामनामी जैसी जातियों को किस प्रविष्टि संख्या के तहत सूचीबद्ध किया गया है?"
    },
    {
        "en": "Are 'Kolupulvandlu', 'Pambada', and 'Pambala' recognized as Scheduled Castes in Andhra Pradesh, and what is their entry number?",
        "hi": "क्या 'कोलुपुलवांडलू', 'पामबाड़ा' और 'पामबाला' को आंध्र प्रदेश में अनुसूचित जाति के रूप में मान्यता दी गई है, और उनकी प्रविष्टि संख्या क्या है?"
    },
    {
        "en": "Which entry in the Scheduled Castes list for Chhattisgarh includes 'Dumar, Dome, Domar, and Doris'?",
        "hi": "छत्तीसगढ़ के लिए अनुसूचित जाति की सूची में किस प्रविष्टि में 'डुमार, डोम, डोमार और डोरिस' शामिल हैं?"
    },
    {
        "en": "Is 'Banchada' recognized as a Scheduled Caste in Chhattisgarh, and under which entry number?",
        "hi": "क्या छत्तीसगढ़ में 'बांछड़ा' (Banchada) को अनुसूचित जाति के रूप में मान्यता प्राप्त है, और किस प्रविष्टि संख्या के तहत?"
    },
    {
        "en": "Are 'Kalbelia', 'Sapera', and 'Kubutar' listed under the Scheduled Castes list for Chhattisgarh, and under which entry?",
        "hi": "क्या छत्तीसगढ़ के लिए अनुसूचित जाति की सूची में 'कालबेलिया', 'सपेरा' और 'कबूतर' शामिल हैं, और किस प्रविष्टि के तहत?"
    },
    {
        "en": "How many distinct entries are listed under Part XVIIIL for Chhattisgarh in the Constitution (Scheduled Castes) Order, 1950?",
        "hi": "संविधान (अनुसूचित जाति) आदेश, 1950 में छत्तीसगढ़ के लिए भाग XVIIIL के तहत कितनी अलग प्रविष्टियां सूचीबद्ध हैं?"
    },
    # 4. Scheduled Tribes Order
    {
        "en": "Name any five Scheduled Tribes listed for Chhattisgarh in the Constitution (Scheduled Tribes) Order, 1950.",
        "hi": "संविधान (अनुसूचित जनजाति) आदेश, 1950 में छत्तीसगढ़ के लिए सूचीबद्ध किन्हीं पांच अनुसूचित जनजातियों के नाम बताइए।"
    },
    {
        "en": "Under which entry number is 'Halba, Halbi' listed as a Scheduled Tribe for Chhattisgarh in the 1950 Order?",
        "hi": "1950 के आदेश में छत्तीसगढ़ के लिए 'हलबा, हलबी' को किस प्रविष्टि संख्या के तहत अनुसूचित जनजाति के रूप में सूचीबद्ध किया गया है?"
    },
    {
        "en": "Is 'Bhil Mina' recognized as a Scheduled Tribe in Chhattisgarh under Part XX of the Scheduled Tribes Order?",
        "hi": "क्या अनुसूचित जनजाति आदेश के भाग XX के तहत छत्तीसगढ़ में 'भील मीना' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है?"
    },
    {
        "en": "What geographical limits or specific districts are mentioned for the 'Gond' tribe in the Chhattisgarh Scheduled Tribes list?",
        "hi": "छत्तीसगढ़ अनुसूचित जनजाति की सूची में 'गोंड' जनजाति के लिए कौन सी भौगोलिक सीमाएं या विशिष्ट जिले बताए गए हैं?"
    },
    {
        "en": "Under entry 5 of Andhra Pradesh in the Scheduled Tribes list, which sub-tribes of Gadabas are recognized?",
        "hi": "अनुसूचित जनजाति सूची में आंध्र प्रदेश की प्रविष्टि 5 के तहत गदबा (Gadabas) की कौन सी उप-जनजातियां मान्यता प्राप्त हैं?"
    },
    {
        "en": "Is 'Kawar, Kanwar, Kaur, Cherwa, Rathia, Tanwar, Chattri' recognized as a Scheduled Tribe in Chhattisgarh, and what is its entry number?",
        "hi": "क्या छत्तीसगढ़ में 'कवर, कंवर, कौर, चेरवा, रथिया, तंवर, छत्री' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है, और इसकी प्रविष्टि संख्या क्या है?"
    },
    {
        "en": "For which specific districts is the tribe 'Dhulia, Paiko, Putiya' recognized under entry 35 of Andhra Pradesh Scheduled Tribes?",
        "hi": "आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 35 के तहत 'धूलिया, पैको, पुतिया' जनजाति को किन विशिष्ट जिलों के लिए मान्यता दी गई है?"
    },
    {
        "en": "Is 'Sahariya, Saharia, Seharia, Sehria, Sosia, Sor' recognized as a Scheduled Tribe in Chhattisgarh, and under which entry number?",
        "hi": "क्या छत्तीसगढ़ में 'सहरिया, सहारिया, सेहारिया, सेहरिया, सोसिया, सोर' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है, और किस प्रविष्टि संख्या के तहत?"
    },
    # 5. Social Status Act (Caste Cert Rules / Act)
    {
        "en": "Under the Chhattisgarh Social Status Certification Act 2013, on whom does the burden of proof lie to establish caste status?",
        "hi": "छत्तीसगढ़ सामाजिक प्रास्थिति प्रमाणीकरण अधिनियम 2013 के तहत, जाति की प्रास्थिति साबित करने के लिए सबूत का भार किस पर होता है?"
    },
    {
        "en": "What are the minimum and maximum terms of imprisonment and fine for a person who obtains a false caste certificate under Section 10(1)?",
        "hi": "धारा 10(1) के तहत झूठा जाति प्रमाण पत्र प्राप्त करने वाले व्यक्ति के लिए कारावास और जुर्माने की न्यूनतम और अधिकतम अवधि क्या है?"
    },
    {
        "en": "Under Section 11 of the 2013 Act, are the offenses under Section 10 cognizable and bailable?",
        "hi": "2013 के अधिनियम की धारा 11 के तहत, क्या धारा 10 के तहत अपराध संज्ञेय और जमानतीय हैं?"
    },
    {
        "en": "Can a court take cognizance of a false certificate issued by a Competent Authority under Section 12 without government approval?",
        "hi": "क्या कोई न्यायालय सरकार की मंजूरी के बिना धारा 12 के तहत सक्षम प्राधिकारी द्वारा जारी किए गए झूठे प्रमाण पत्र का संज्ञान ले सकता है?"
    },
    {
        "en": "What is the time limit for an applicant to file an appeal against the rejection of a caste certificate, and how long does the appellate authority have to decide?",
        "hi": "जाति प्रमाण पत्र की अस्वीकृति के खिलाफ अपील दायर करने की समय सीमा क्या है, और अपीलीय प्राधिकारी के पास निर्णय लेने के लिए कितना समय होता है?"
    },
    {
        "en": "Within what time frame must the District Level Certificate Verification Committee report its findings to an employer or educational institution under Section 6(2)?",
        "hi": "धारा 6(2) के तहत जिला स्तरीय प्रमाणपत्र सत्यापन समिति को नियोक्ता या शैक्षणिक संस्थान को अपने निष्कर्षों की रिपोर्ट कितने समय में देनी होगी?"
    },
    {
        "en": "According to Section 4(2) of the Act, what is the validity period of a social status certificate issued by the Competent Authority?",
        "hi": "अधिनियम की धारा 4(2) के अनुसार सक्षम प्राधिकारी द्वारा जारी सामाजिक प्रास्थिति प्रमाणपत्र की वैधता अवधि क्या है?"
    },
    {
        "en": "Under what condition can a duplicate social status certificate be issued to an applicant according to Section 4(2)?",
        "hi": "धारा 4(2) के अनुसार आवेदक को किस स्थिति में डुप्लीकेट सामाजिक प्रास्थिति प्रमाण पत्र जारी किया जा सकता है?"
    },
    {
        "en": "If a social status certificate is cancelled under Section 8, what happens to the degrees or diplomas earned using that certificate according to Section 9(4)?",
        "hi": "यदि धारा 8 के तहत सामाजिक प्रास्थिति प्रमाणपत्र रद्द कर दिया जाता है, तो धारा 9(4) के अनुसार उस प्रमाणपत्र का उपयोग करके प्राप्त की गई डिग्री या डिप्लोमा का क्या होता है?"
    },
    {
        "en": "What is the consequence if a person is elected to a local authority or constitutional body based on a caste certificate that is later cancelled under Section 8?",
        "hi": "यदि कोई व्यक्ति ऐसे जाति प्रमाण पत्र के आधार पर स्थानीय प्राधिकरण या संवैधानिक निकाय के लिए चुना जाता है जिसे बाद में धारा 8 के तहत रद्द कर दिया जाता है, तो इसका क्या परिणाम होता है?"
    },
    # 6. Out of Scope
    {
        "en": "How do I apply for a new passport in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में नया पासपोर्ट आवेदन कैसे करें?"
    },
    {
        "en": "What is the procedure to get a new driving license in Raipur?",
        "hi": "रायपुर में नया ड्राइविंग लाइसेंस प्राप्त करने की प्रक्रिया क्या है?"
    },
    {
        "en": "How to apply for a voter ID card online?",
        "hi": "ऑनलाइन वोटर आईडी कार्ड के लिए आवेदन कैसे करें?"
    },
    {
        "en": "What is the application fee for a birth certificate in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में जन्म प्रमाण पत्र के लिए आवेदन शुल्क क्या है?"
    },
    {
        "en": "How can I register a company or start a new business in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में कंपनी का पंजीकरण कैसे करें या नया व्यवसाय कैसे शुरू करें?"
    },
    {
        "en": "What are the rules and guidelines for traffic violations in Chhattisgarh?",
        "hi": "छत्तीसगढ़ में यातायात उल्लंघन के क्या नियम और दिशा-निर्देश हैं?"
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
    print("=== Starting SewaSetu Chatbot Evaluation Suite (Real User Mode) ===")
    print(f"Total query pairs (EN & HI): {len(QUERIES)}")
    print(f"Results will be appended incrementally to: {RESULTS_FILE}")
    print("-" * 50)
    
    # Initialize/overwrite markdown file with header
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        f.write("# SewaSetu RAG Chatbot Evaluation Report (Real User Mode)\n\n")
        f.write("This report presents the testing results of the chatbot in both English and Hindi for 50 diverse queries, run without passing any service category or ID.\n\n")
        f.write("## Test Parameters\n")
        f.write(f"- **API Endpoint:** `{API_URL}`\n")
        f.write("- **Date & Time:** " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write(f"- **Total Query Runs:** {len(QUERIES) * 2} (50 English + 50 Hindi)\n\n")
        f.write("## Test Results\n\n")
        f.write("| Language | Query | Generated Answer | Time (s) |\n")
        f.write("| --- | --- | --- | --- |\n")

    count = 0
    total_time = 0.0
    
    for idx, item in enumerate(QUERIES):
        # 1. Test English Query
        print(f"[{idx+1}/{len(QUERIES)}] Querying EN: \"{item['en']}\" ...")
        ans_en, time_en = query_chat_api(item["en"], "en")
        total_time += time_en
        count += 1
        
        # Append English Result
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            escaped_ans_en = ans_en.replace("\n", "<br>")
            f.write(f"| EN | {item['en']} | {escaped_ans_en} | {time_en:.2f} |\n")
        
        # 2. Test Hindi Query
        print(f"[{idx+1}/{len(QUERIES)}] Querying HI: \"{item['hi']}\" ...")
        ans_hi, time_hi = query_chat_api(item["hi"], "hi")
        total_time += time_hi
        count += 1
        
        # Append Hindi Result
        with open(RESULTS_FILE, "a", encoding="utf-8") as f:
            escaped_ans_hi = ans_hi.replace("\n", "<br>")
            f.write(f"| HI | {item['hi']} | {escaped_ans_hi} | {time_hi:.2f} |\n")
            
        print(f"Completed query pair {idx+1} (EN: {time_en:.1f}s | HI: {time_hi:.1f}s)")
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
