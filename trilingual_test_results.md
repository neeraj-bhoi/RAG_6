# SewaSetu RAG Chatbot Trilingual Evaluation Report

This report presents the testing results of the chatbot in three languages: **English**, **Hindi**, and **Hinglish** across all 5 in-scope citizen services and out-of-scope scenarios. Queries were executed globally without specifying service serial numbers.

## Test Configuration
- **API Server:** `http://localhost:8000/api/chat`
- **Date & Time:** 2026-06-22 13:00:10
- **Total Query Runs:** 150 (50 English + 50 Hindi + 50 Hinglish)

## Table of Contents
- [1. Domicile Certificate (Chhattisgarh Domicile Criteria)](#1-domicile-certificate-chhattisgarh-domicile-criteria)
- [2. Marriage Registration & Certificate](#2-marriage-registration-and-certificate)
- [3. Scheduled Castes & Scheduled Tribes Order 1950](#3-scheduled-castes-and-scheduled-tribes-order-1950)
- [4. Social Status Act (Caste Certificate Rules)](#4-social-status-act-caste-certificate-rules)
- [5. Ordinary Gazette Notification for Name Change](#5-ordinary-gazette-notification-for-name-change)
- [6. Out of Scope Queries](#6-out-of-scope-queries)

---

## 1. Domicile Certificate (Chhattisgarh Domicile Criteria)

### Q1: Is formal education in Chhattisgarh for at least three years sufficient for establishing domicile under Criteria B?

**Hindi:** *क्या मानदंड B के तहत मूल निवासी स्थापित करने के लिए छत्तीसगढ़ में कम से कम तीन साल की औपचारिक शिक्षा पर्याप्त है?*

**Hinglish:** *Kya criteria B ke under domicile certificate ke liye CG me 3 saal ki padhai kafi hai?*

#### 🇬🇧 English Response:
> हाँ, छत्तीसगढ़ में कम से कम तीन साल की औपचारिक शिक्षा, Criteria B के तहत domicile स्थापित करने के लिए पर्याप्त है।
> 
> संदर्भ के अनुसार, Criteria Two में "CG में 3 साल की औपचारिक शिक्षा" को एक विकल्प के रूप में सूचीबद्ध किया गया है। चूँकि यह एक "OR" (या) की स्थिति है, इसलिए इस एकल मानदंड को पूरा करना domicile के लिए पात्र होने हेतु पर्याप्त है।
> 
> सेवा: Domicile Certificate
> विभाग: Revenue and disaster management Department

*Latency: 51.75 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ में तीन साल की औपचारिक शिक्षा एक मानदंड है।
> 
> सेवा सेटू छत्तीसगढ़ पोर्टल के अनुसार, मूल निवासी प्रमाण पत्र (डोमिसाइल सर्टिफिकेट) के लिए, मानदंड दो के तहत, आप मानदंड को पूरा करने के लिए या तो छत्तीसगढ़ में तीन साल की औपचारिक शिक्षा कर सकते हैं या फिर कक्षा 5, 8, 10, या 12 का बोर्ड परीक्षा पास कर सकते हैं।
> 
> यह सेवा राजस्व और आपदा प्रबंधन विभाग द्वारा प्रदान की जाती है।

*Latency: 12.39 seconds*

#### 💬 Hinglish Response:
> हाँ, Chhattisgarh में domicile certificate के लिए criteria B के तहत 3 साल की पढ़ाई काफी है।
> 
> Service: Domicile Certificate के अनुसार, criteria B में domicile certificate के लिए, आपके पास Chhattisgarh में 3 साल की formal padhai का प्रमाण होना चाहिए। इसके अलावा, आप CG से कोई board exam (जैसे Class 5, 8, 10, 12) भी pass कर सकते हैं।
> 
> याद रखें कि criteria B में इन दो में से किसी एक शर्त को पूरा करना होगा: या तो 3 साल की padhai, या फिर board exam pass करना।

*Latency: 15.77 seconds*

---

### Q2: Can a person obtain a Chhattisgarh domicile certificate if either of their parents is a state government employee?

**Hindi:** *यदि किसी व्यक्ति के माता-पिता में से कोई एक राज्य सरकार का कर्मचारी है, तो क्या वह छत्तीसगढ़ मूल निवासी प्रमाण पत्र प्राप्त कर सकता है?*

**Hinglish:** *Kya koi CG domicile le sakta hai agar uske parents me se koi state government employee ho?*

#### 🇬🇧 English Response:
> हाँ, Chhattisgarh domicile certificate प्राप्त करने के लिए एक व्यक्ति के माता-पिता में से कोई एक state government employee हो सकता है, लेकिन उन्हें अन्य criteria भी पूरे करने होंगे।
> 
> Context के अनुसार, criteria में से एक यह है: "Either of the parents is an employee of CG Government or its undertaking."
> 
> हालाँकि, rules में एक important note दिया गया है: "Criteria A and B together must be met to get the Certificate."
> 
> इसका मतलब है कि applicant को Criteria A या B में से किसी एक को भी satisfy करना होगा:
> 
> *   **Criteria A:** या तो applicant Chhattisgarh में पैदा हुआ हो, या उसके parents 25 साल से लगातार state के residents रहे हों।
> *   **या**
> *   **Criteria B:** Applicant ने Chhattisgarh में 3 साल की formal education ली हो, या उसने Class 5, 8, 10, या 12 में से किसी एक board exam को state से pass किया हो।
> 
> Summary में, हालाँकि parent का government employee होना एक relevant factor है, लेकिन यह अपने आप में काफी नहीं है। Applicant को domicile certificate पाने के लिए Criteria A और B के educational या residency requirements भी पूरे करने होंगे।
> 
> Chhattisgarh domicile certificate के लिए, service **Revenue and disaster management Department** द्वारा provide की जाती है।

*Latency: 12.52 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, यदि माता-पिता में से कोई एक छत्तीसगढ़ सरकार का कर्मचारी है, तो यह एक संभावित मानदंड है, लेकिन यह एकमात्र मानदंड नहीं है।
> 
> उपयोगकर्ता नियमावली के अनुसार, छत्तीसगढ़ मूल निवासी प्रमाण पत्र के लिए निम्नलिखित मानदंड हैं:
> 
> 1. **मानदंड एक:**
>     * a. जन्म छत्तीसगढ़ में हुआ हो (जन्म प्रमाण पत्र)
>     * b. माता-पिता में से कोई 25 वर्षों से छत्तीसगढ़ का निवासी हो
>     * c. **माता-पिता में से कोई छत्तीसगढ़ सरकार या उसके किसी उपक्रम का कर्मचारी हो**
>     * d. माता-पिता या आवेदक के पास पिछले 5 वर्षों से छत्तीसगढ़ में संपत्ति हो
> 
> **महत्वपूर्ण नोट:** प्रमाण पत्र प्राप्त करने के लिए 'मानदंड एक' के पहले दो बिंदुओं (जन्म स्थान या माता-पिता का निवास) को पूरा करना अनिवार्य है।
> 
> इसके अतिरिक्त, आवेदक को 'मानदंड दो' के अनुसार शिक्षा संबंधी आवश्यकताओं को भी पूरा करना होगा, जैसे कि छत्तीसगढ़ में तीन वर्ष की औपचारिक शिक्षा या कक्षा 5, 8, 10, या 12वीं की बोर्ड परीक्षा उत्तीर्ण करना।
> 
> अतः, माता-पिता का सरकारी कर्मचारी होना एक सहायक कारक है, लेकिन इसके साथ-साथ अन्य शर्तों को भी पूरा करना आवश्यक है।
> 
> सेवा नाम: मूल निवासी प्रमाण पत्र (सेवा संख्या: 7), विभाग: राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़।

*Latency: 14.66 seconds*

#### 💬 Hinglish Response:
> Haan, agar aapke parents mein se koi state government employee hai, toh aap CG Domicile certificate ke liye apply kar sakte hain.
> 
> Lekin, yeh ek hi condition nahi hai. Aapko criteria ke according bhi qualify karna padega.
> 
> Source 1 ke according, criteria mein se ek option yeh hai ki "Either of the parents is an employee of CG Government or its undertaking."
> 
> Lekin note mein likha hai ki Criteria A aur B dono saath mein meet karne padenge. Iska matlab hai ki aapko baaki criteria bhi satisfy karne honge, jaise ki aapka birth CG mein hua ho ya aapke parents 25 saal se CG mein resident hain, aur aapki education bhi CG mein hui ho.
> 
> Toh, parent ka state government employee hona ek option hai, lekin final certificate ke liye aapko sabhi criteria meet karne honge.

*Latency: 16.05 seconds*

---

### Q3: What property documents are required for domicile application if applying under the property ownership clause?

**Hindi:** *यदि संपत्ति स्वामित्व क्लॉज के तहत आवेदन कर रहे हैं, तो मूल निवासी आवेदन के लिए कौन से संपत्ति दस्तावेज आवश्यक हैं?*

**Hinglish:** *Property ownership clause ke under domicile apply karne ke liye kaun se property documents chahiye?*

#### 🇬🇧 English Response:
> For the Domicile Certificate application, if you are applying under the property ownership clause, the required document is a **Land And House Document**.
> 
> This document is used to prove that either you or your parents/guardians hold property in Chhattisgarh for the last 5 years, which is one of the criteria for getting a domicile certificate. This is listed as a mandatory supporting document in the official specifications for the application.

*Latency: 14.43 seconds*

#### 🇮🇳 Hindi Response:
> अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए मूल निवासी आवेदन हेतु संपत्ति स्वामित्व से संबंधित निम्नलिखित दस्तावेज आवश्यक हैं:
> 
> 1. अधिकार अभिलेख (Adhikar Abhilekh)
> 2. जमाबंदी (Jamabandi)
> 3. दाखिल / खारीज पंजी (Dakhil / Kharij Panji)
> 4. भूमि और घर का दस्तावेज (Land and House Document)
> 
> ये दस्तावेज सेवा के "OBC प्रमाण पत्र" (ID: 5) के अंतर्गत "OBC प्रमाण" (SNo 4) अनुभाग के तहत सूचीबद्ध हैं।
> 
> सेवा का नाम: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 15.08 seconds*

#### 💬 Hinglish Response:
> Agar aap property ownership clause ke under domicile apply kar rahe hain, to context ke according aapko property se related documents dene pad sakte hain. Ye documents ho sakte hain:
> 
> *   Jamabandi
> *   Dakhil / Kharij Panji
> *   Adhikar Abhilekh
> *   Land And House Document
> 
> Domicile Certificate section mein "Property docs if applicable" likha hai, jisse pata chalta hai ki ye zaroori ho sakte hain. Ye information Sewa Setu Chhattisgarh portal ke Revenue and disaster management Department se related hai.

*Latency: 14.54 seconds*

---

### Q4: Are grandchildren of a 25-year continuous resident of Chhattisgarh eligible for domicile?

**Hindi:** *क्या छत्तीसगढ़ के 25 वर्ष के निरंतर निवासी के पोते-पोतियां मूल निवासी के लिए पात्र हैं?*

**Hinglish:** *Kya CG ke 25 years continuous resident ke grandchildren domicile ke liye eligible hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the grandchildren of a 25-year continuous resident of Chhattisgarh are not explicitly mentioned as eligible for a domicile certificate.
> 
> The criteria for a CG Domicile, as stated in the Domicile Certificate service manual, require that **either of the applicant's parents** must be a resident of Chhattisgarh for a continuous 25 years. The eligibility is based on the applicant's parents' residency, not their grandparents.
> 
> Therefore, according to the provided information, the grandchildren of a 25-year resident would not meet the specified criteria for a domicile certificate.
> 
> This information is based on the Domicile Certificate service guidelines from the Revenue and disaster management Department.

*Latency: 11.60 seconds*

#### 🇮🇳 Hindi Response:
> Jaankari uplabd nahi hai.
> 
> Sewasuchit Chhattisgarh portal par diye gaye context mein, Chhattisgarh ke 25 saal ke nirantar nivas ke pote-potiyon ke liye koi jaankari nahi hai. Context mein sirf aavedak ya uske parents ke nivas se sambandhit criteria diye gaye hain.
> 
> Isliye, is aadhar par unki patrata ke baare mein kuch bhi kehna sambhav nahi hai.
> 
> Sewa Setu Chhattisgarh portal par Domicile Certificate (ID: 7) ke liye, Revenue and disaster management Department se jaankari leni hogi.

*Latency: 21.80 seconds*

#### 💬 Hinglish Response:
> Diye gaye context ke aadhar par, yeh jaankari uplabdh nahi hai ki kya CG ke 25 saal continuous resident ke grandchildren domicile ke liye eligible hain.
> 
> Context mein bataya gaya hai ki agar applicant ke parents 25 saal se Chhattisgarh mein resident hain, toh woh criteria A ke hisaab se eligible ho sakte hain. Grandparents ya grandchildren ke baare mein is context mein koi jaankari nahi di gayi hai. Jaankari uplabdh nahi hai.

*Latency: 12.00 seconds*

---

### Q5: What educational certificates must be submitted to satisfy Criteria B of the domicile requirements?

**Hindi:** *मूल निवासी आवश्यकताओं के मानदंड B को पूरा करने के लिए कौन से शैक्षणिक प्रमाण पत्र जमा किए जाने चाहिए?*

**Hinglish:** *Domicile requirements ke criteria B ko pura karne ke liye kaun se educational certificates jama karne honge?*

#### 🇬🇧 English Response:
> Based on the provided context for the Domicile Certificate service, to satisfy Criteria B, you must meet one of the following educational requirements:
> 
> 1.  Have three years of formal education in Chhattisgarh.
> 2.  Pass one of the board exams (Class 5, 8, L0, L2) from Chhattisgarh.
> 
> Please note that Criteria A and B together must be met to get the certificate.
> 
> Service: Domicile Certificate, Department: Revenue and disaster management Department.

*Latency: 18.64 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 13.70 seconds*

#### 💬 Hinglish Response:
> Sewasettu Chhattisgarh portal ke according, Domicile Certificate ke liye criteria B ko pura karne ke liye aapke paas do options hain:
> 
> 1.  Aapne Chhattisgarh mein 3 saal ki formal education ki ho.
> 2.  Aapne Chhattisgarh se koi bhi board exam (Class 5, 8, 10, 12) pass kiya ho.
> 
> Agar aapko educational certificate provide karna hai, toh ye documents valid maane jaate hain:
> 
> *   Middle School Certificate - 8th Standard
> *   Primary School Certificate - 5th Standard
> *   High School (10th) Certificate
> *   Higher Secondary School Certificate (12th)
> *   M.Phil/D.Lit./Ph.D. Certificate
> *   School Certificate (3 saal ki continuous study ke proof ke liye)
> *   Post Graduation Certificate
> *   Technical subjects ka certificate
> 
> Service: Domicile Certificate
> Department: Revenue and disaster management Department

*Latency: 18.88 seconds*

---

### Q6: Do All India Services officers allotted to the Chhattisgarh Cadre need to submit 25 years of residence proof for domicile?

**Hindi:** *क्या छत्तीसगढ़ कैडर में आवंटित अखिल भारतीय सेवा के अधिकारियों को मूल निवासी के लिए 25 वर्ष के निवास प्रमाण पत्र जमा करने की आवश्यकता है?*

**Hinglish:** *Kya CG Cadre ke All India Services officers ko domicile ke liye 25 years ka residence proof dena padta hai?*

#### 🇬🇧 English Response:
> नहीं, प्रदान की गई जानकारी के आधार पर, छत्तीसगढ़ कैडर में नियुक्त अखिल भारतीय सेवा (AIS) अधिकारियों को निवास प्रमाण पत्र (डोमिसाइल सर्टिफिकेट) के लिए 25 वर्ष के निवास प्रमाण प्रस्तुत करने की आवश्यकता नहीं है।
> 
> राजस्व और आपदा प्रबंधन विभाग के अंतर्गत डोमिसाइल सर्टिफिकेट सेवा के लिए संदर्भ निर्दिष्ट करता है कि "मानदंड तीन" (क्राइटेरिया थ्री) के अंतर्गत, जिसमें AIS अधिकारी शामिल हैं, 25 वर्ष के निवास प्रमाण की आवश्यकता अनिवार्य नहीं है।

*Latency: 12.71 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, उन्हें 25 वर्ष के निवास प्रमाण पत्र की आवश्यकता नहीं है।
> 
> राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़ के अनुसार, यदि आवेदक या उसके माता-पिता अखिल भारतीय सेवा (AIS) में हैं और उन्हें छत्तीसगढ़ कैडर आवंटित किया गया है, तो उन्हें निवास प्रमाण पत्र की आवश्यकता नहीं है।
> 
> यह जानकारी "मानदंड तीन" के अंतर्गत आती है, जहाँ इस श्रेणी के व्यक्तियों के लिए मानदंड A और B की शर्तें लागू नहीं होती हैं। इसलिए, उनके लिए 25 वर्ष के निवास प्रमाण पत्र की आवश्यकता नहीं है।
> 
> यह जानकारी राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़ के लिए है।

*Latency: 15.38 seconds*

#### 💬 Hinglish Response:
> Source 1 ke according, agar applicant ya unke parent All India Services mein hain aur unhe CG Cadre allot kiya gaya hai, toh unhe CG Domicile ke liye eligible maana jaata hai (Criteria Three). 25 saal ka residence proof (continuous 25 years) Criteria One mein mention hai, lekin yeh applicant ke parents ke liye hai, applicant ke liye nahi.
> 
> Isliye, diye gaye context mein yeh clear nahi hai ki CG Cadre ke All India Services officers ko 25 saal ka residence proof dena zaroori hai. Unki eligibility alag se criteria ke basis par hai.
> 
> Service: Domicile Certificate
> Department: Revenue and disaster management Department

*Latency: 19.42 seconds*

---

### Q7: What is the fee for obtaining a Domicile Certificate at a Sewa Setu Kendra?

**Hindi:** *सेवा सेतु केंद्र पर मूल निवासी प्रमाण पत्र प्राप्त करने का शुल्क क्या है?*

**Hinglish:** *Sewa Setu Kendra se domicile certificate lene ki fees kya hai?*

#### 🇬🇧 English Response:
> The fee for obtaining a Domicile Certificate at a Sewa Setu Kendra is ₹30.0. This fee is applicable both at the Sewa Setu Kendra and for online applications.
> 
> Service: Domicile Certificate (ID: 7)
> Department: Revenue and disaster management Department
> Time Limit / SLA: 7 Days
> Contact Details: Sewa Setu Kendra
> Kiosk Fee: 30.0
> Online Fee: 30.0
> 
> Information not available.

*Latency: 5.56 seconds*

#### 🇮🇳 Hindi Response:
> सेवा सेतु केंद्र पर मूल निवासी प्रमाण पत्र प्राप्त करने का शुल्क ₹30.0 है। यह शुल्क ऑनलाइन आवेदन के लिए भी समान है। यह सेवा राजस्व एवं आपदा प्रबंधन विभाग द्वारा संचालित की जाती है।

*Latency: 22.32 seconds*

#### 💬 Hinglish Response:
> Sewa Setu Kendra se Domicile Certificate (Service ID: 7) lene ke liye, fee ₹30.0 hai. Ye fee online apply karne par bhi same rehti hai.

*Latency: 13.57 seconds*

---

### Q8: Is an affidavit required for applying for a CG domicile certificate, and is it mandatory?

**Hindi:** *क्या सीजी मूल निवासी प्रमाण पत्र के लिए आवेदन करने के लिए शपथ पत्र आवश्यक है, और क्या यह अनिवार्य है?*

**Hinglish:** *Kya CG domicile certificate apply karne ke liye affidavit zaroori aur mandatory hai?*

#### 🇬🇧 English Response:
> Yes, an affidavit is required and is mandatory for applying for a CG Domicile Certificate.
> 
> According to the official manual for the Domicile Certificate service, the affidavit is listed as a required document. The service is managed by the Revenue and disaster management Department.

*Latency: 11.13 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, CG मूल निवासी प्रमाण पत्र के लिए शपथ पत्र आवश्यक है। यह एक अनिवार्य दस्तावेज है।
> 
> यह जानकारी 'डोमिसाइल सर्टिफिकेट' सेवा के मैनुअल से ली गई है, जो राजस्व और आपदा प्रबंधन विभाग के अंतर्गत आता है।

*Latency: 13.95 seconds*

#### 💬 Hinglish Response:
> Haan, CG domicile certificate apply karne ke liye affidavit zaroori aur mandatory hai.
> 
> Source 2 ke according, Domicile Certificate ke liye 'SNo 1: Affidavit (Mandatory: Yes)' listed hai.
> 
> Yeh information Revenue and disaster management Department se related hai.

*Latency: 14.63 seconds*

---

## 2. Marriage Registration & Certificate

### Q9: What are the rules regarding registration of marriages performed prior to the commencement of the Chhattisgarh Rules 2006?

**Hindi:** *छत्तीसगढ़ नियम 2006 के प्रारंभ होने से पहले संपन्न हुए विवाहों के पंजीकरण के संबंध में क्या नियम हैं?*

**Hinglish:** *CG Rules 2006 se pehle hui shadiyo ke registration ke liye kya rules hain?*

#### 🇬🇧 English Response:
> Information not available. The provided context does not specify the rules for marriages performed prior to the commencement of the Chhattisgarh Rules 2006. It only states that from the date of commencement, every marriage solemnized in the state shall be registered.

*Latency: 11.59 seconds*

#### 🇮🇳 Hindi Response:
> प्रदान किए गए संदर्भ में इस बात की जानकारी नहीं है कि छत्तीसगढ़ नियम 2006 के प्रारंभ होने से पहले संपन्न हुए विवाहों के पंजीकरण के लिए क्या नियम हैं।
> 
> संदर्भ के अनुसार, छत्तीसगढ़ अनिवार्य विवाह पंजीकरण नियम, 2006, आधिकारिक राजपत्र में इसके प्रकाशन की तिथि से लागू हुए हैं। नियम 4(1)(a) के अनुसार, इन नियमों के लागू होने की तिथि से राज्य में संपन्न होने वाले प्रत्येक विवाह का पंजीकरण अनिवार्य है।
> 
> प्रदान किए गए दस्तावेज़ में उन विवाहों के पंजीकरण की प्रक्रिया या नियमों का उल्लेख नहीं है जो 2006 के नियमों के लागू होने से पहले संपन्न हुए थे। सटीक जानकारी के लिए, आपको पूर्ण नियम पुस्तिका देखनी होगी या शहरी प्रशासन और विकास विभाग से संपर्क करना होगा।

*Latency: 17.30 seconds*

#### 💬 Hinglish Response:
> Provided context mein aisi koi specific rules nahi hain jo CG Rules 2006 se pehle hui shadiyon ke registration ke liye hain.
> 
> Context ke according, Chhattisgarh Compulsory Registration of Marriages Rules, 2006, ek specific date se laagu hue the. Rule 4(1)(a) ke anusar, in rules ke laagu hone ki date se, state mein solemnized har shadi register karni zaroori hai. Iska matlab hai ki 2006 ke rules se pehle hui shadiyon ke liye registration ki koi nayi obligation nahi thi.
> 
> Rule 9 bhi yeh batata hai ki jo shadiyan in rules ke under nahi aati, unhe sirf isliye invalid nahi maana jaata ki unka registration nahi hua hai. Context mein sirf current registration process ki jaankari di gayi hai, purani shadiyon ke registration ke liye koi details nahi hain.
> 
> Sewasankhya ke liye, yeh service 'Marriage Registration & Certificate' hai, jise 'Urban Administration and development Department' handle karta hai.

*Latency: 18.51 seconds*

---

### Q10: What local bodies act as the Registrar of Marriages in municipal areas of Chhattisgarh?

**Hindi:** *छत्तीसगढ़ के नगर निगम क्षेत्रों में विवाह रजिस्ट्रार के रूप में कौन से स्थानीय निकाय कार्य करते हैं?*

**Hinglish:** *CG ke municipal areas me Marriage Registrar ke roop me kaun se local bodies kaam karte hain?*

#### 🇬🇧 English Response:
> Based on the provided context, in the municipal areas of Chhattisgarh, the Municipality or Municipal Corporation acts as the Registrar of Marriages.
> 
> The rules state that the "Local Authority" is the registrar for its local area. A "Local Authority" is defined as "Gram Panchayat or Municipality or Municipal Corporation as the case may be".
> 
> This service is provided by the Urban Administration and development Department.

*Latency: 16.77 seconds*

#### 🇮🇳 Hindi Response:
> Error connecting to API: HTTPConnectionPool(host='localhost', port=8000): Read timed out. (read timeout=90)

*Latency: 0.00 seconds*

#### 💬 Hinglish Response:
> Jaankari ke anusar, Chhattisgarh ke municipal areas mein marriage registration ke liye local authority hi registrar ka kaam karti hai.
> 
> Rules ke according, 'Local Authority' ka matlab Gram Panchayat, Municipality, ya Municipal Corporation hai. Isliye, municipal area mein, local authority (jo ki Municipality ya Municipal Corporation hai) hi us area ke liye Marriage Registrar ke roop mein kaam karti hai.
> 
> Ye information Chhattisgarh Compulsory Registration of Marriages Rules, 2006 se mili hai. Sewa Setu Chhattisgarh portal ke liye, ye service Urban Administration and development Department ke under aati hai.

*Latency: 20.80 seconds*

---

### Q11: What is the fee for registering a marriage within thirty days versus after thirty days?

**Hindi:** *तीस दिनों के भीतर विवाह पंजीकृत करने और तीस दिनों के बाद पंजीकृत करने का शुल्क क्या है?*

**Hinglish:** *30 days ke andar shadi register karne aur 30 days ke baad register karne ki fee kya hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the fee for registering a marriage is ₹30.0. This fee is applicable for both online and offline applications.
> 
> The context does not specify different fees for registering a marriage within thirty days versus after thirty days. The information available is limited to a single, uniform fee of ₹30.0.
> 
> Information not available.

*Latency: 5.65 seconds*

#### 🇮🇳 Hindi Response:
> आपके प्रश्न के अनुसार, विवाह पंजीकरण के शुल्क के बारे में संदर्भ में जानकारी दी गई है।
> 
> अनुप्रयोग शुल्क 30.0 रुपये है, जो Sewa Setu Kendra या ऑनलाइन आवेदन के लिए है।
> 
> संदर्भ में ऐसा कोई उल्लेख नहीं है कि 30 दिनों के भीतर या उसके बाद विवाह पंजीकृत करने पर अलग-अलग शुल्क लागू होते हैं। इसलिए, संदर्भ के अनुसार, शुल्क समान रहता है।

*Latency: 16.59 seconds*

#### 💬 Hinglish Response:
> जानकारी के अनुसार, शादी की रजिस्ट्रेशन की फीस 30.0 रुपये है। यह फीस 30 दिनों के भीतर या 30 दिनों के बाद, दोनों ही स्थितियों में समान है। ऑनलाइन और सेवा सेटू केंद्र, दोनों जगह यह फीस 30.0 रुपये है।
> 
> यह जानकारी 'मैरिज रजिस्ट्रेशन एंड सर्टिफिकेट' सर्विस (ID: 3) और शहरी प्रशासन एवं विकास विभाग से संबंधित है।

*Latency: 37.38 seconds*

---

### Q12: Who can appeal against a Marriage Registrar's refusal to register a marriage?

**Hindi:** *विवाह रजिस्ट्रार द्वारा विवाह पंजीकृत करने से इनकार करने के खिलाफ कौन अपील कर सकता है?*

**Hinglish:** *Marriage Registrar ke shadi register karne se mana karne par kaun appeal kar sakta hai?*

#### 🇬🇧 English Response:
> Based on the provided context, a person can appeal against a Marriage Registrar's refusal to register a marriage in the following steps:
> 
> 1.  **Appeal to the Chief Registrar:** Any person who is aggrieved by the Registrar's refusal order can appeal to the Chief Registrar. This appeal must be filed within 30 days from the date of receiving the order and must be accompanied by a fee of Rs. 30/-.
> 
> 2.  **Appeal to the District Judge:** If the person is still not satisfied with the Chief Registrar's decision, they can appeal to the District Judge. This appeal must be filed within 30 days from the date of the Chief Registrar's order. The decision of the District Judge is final.
> 
> Service: Marriage Registration & Certificate (ID: 3)
> Department: Urban Administration and development Department

*Latency: 12.53 seconds*

#### 🇮🇳 Hindi Response:
> विवाह रजिस्ट्रार द्वारा विवाह पंजीकृत करने से इनकार करने के खिलाफ कोई भी व्यक्ति अपील कर सकता है।
> 
> अपील की प्रक्रिया इस प्रकार है:
> 
> 1.  **मुख्य रजिस्ट्रार (Chief Registrar) के पास:**
>     *   विवाह रजिस्ट्रार के इनकार के आदेश से प्रभावित व्यक्ति 30 दिनों के भीतर 30 रुपये के शुल्क के साथ मुख्य रजिस्ट्रार के पास अपील कर सकता है।
> 
> 2.  **जिला न्यायाधीश (District Judge) के पास:**
>     *   यदि मुख्य रजिस्ट्रार के निर्णय से भी व्यक्ति संतुष्ट नहीं है, तो वह मुख्य रजिस्ट्रार के आदेश के 30 दिनों के भीतर जिला न्यायाधीश के पास अपील कर सकता है।
>     *   जिला न्यायाधीश का निर्णय अंतिम होता है।
> 
> यह सेवा शहरी प्रशासन और विकास विभाग, छत्तीसगढ़ के अंतर्गत आती है।

*Latency: 15.34 seconds*

#### 💬 Hinglish Response:
> जो व्यक्ति शादी के रजिस्ट्रेशन से मना करने वाले रजिस्ट्रार के ऑर्डर से आहत है, वह 30 दिनों के भीतर 30 रुपये के शुल्क के साथ चीफ रजिस्ट्रार के पास अपील कर सकता है।
> 
> यह जानकारी 'Marriage Registration & Certificate' सेवा के तहत 'Urban Administration and development Department' के लिए है।

*Latency: 19.88 seconds*

---

### Q13: Under what conditions can a certified copy of the marriage register be issued to a third party?

**Hindi:** *किन परिस्थितियों में किसी तीसरे पक्ष को विवाह रजिस्टर की प्रमाणित प्रति जारी की जा सकती है?*

**Hinglish:** *Kin conditions me marriage register ki certified copy kisi third party ko di ja sakti hai?*

#### 🇬🇧 English Response:
> Based on the provided context, a certified copy of the marriage register can be issued to a third party under the following conditions:
> 
> 1.  The person must make an application.
> 2.  They must pay a fee of Rs. 20.
> 
> The register is also open for public inspection at all reasonable times.
> 
> Service: Marriage Registration & Certificate
> Department: Urban Administration and development Department

*Latency: 11.27 seconds*

#### 🇮🇳 Hindi Response:
> विवाह रजिस्टर की प्रमाणित प्रति किसी भी व्यक्ति को जारी की जा सकती है, बशर्ते वे आवेदन करें और निर्धारित शुल्क (२० रुपये) का भुगतान करें।
> 
> नियम ८ के अनुसार, विवाह रजिस्टर सार्वजनिक निरीक्षण के लिए खुला है। प्रमाणित प्रति प्राप्त करने के लिए, व्यक्ति को आवेदन करना होगा और शुल्क का भुगतान करना होगा।
> 
> यह सेवा 'विवाह पंजीकरण एवं प्रमाण पत्र' (ID: 3) है, जिसे 'शहरी प्रशासन और विकास विभाग' द्वारा संचालित किया जाता है।

*Latency: 27.41 seconds*

#### 💬 Hinglish Response:
> Source 1 के Rule 8 के according, marriage register की certified copy किसी third party को दी जा सकती है, लेकिन ये तीन conditions के साथ हैं:
> 
> 1. Register public inspection के लिए open होना चाहिए।
> 2. Applicant को application देनी होगी।
> 3. Prescribed fee, जो कि Rs. 20/- है, pay करनी होगी।
> 
> यह information Sewa Setu Chhattisgarh portal के Marriage Registration & Certificate service से related है।

*Latency: 16.42 seconds*

---

### Q14: Is a government employee's marriage certificate required to change their nominee name in service records?

**Hindi:** *क्या किसी सरकारी कर्मचारी के सेवा रिकॉर्ड में उनके नामांकित व्यक्ति का नाम बदलने के लिए विवाह प्रमाण पत्र आवश्यक है?*

**Hinglish:** *Kya kisi sarkari employee ke service records me nominee name badalne ke liye marriage certificate zaroori hai?*

#### 🇬🇧 English Response:
> Yes, a government employee's marriage registration certificate is required to change their nominee name in service records.
> 
> According to the provided context, under the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, Rule 11, a government or semi-government authority cannot make any change in an employee's office record, such as a change in nomination, unless the employee submits a certified copy of their marriage registration certificate.
> 
> This requirement is specified for the Urban Administration and development Department. Therefore, the marriage certificate is a mandatory document for this process.

*Latency: 13.11 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 13.36 seconds*

#### 💬 Hinglish Response:
> हाँ, सरकारी कर्मचारी के सर्विस रिकॉर्ड में नॉमिनी का नाम बदलने के लिए मैरिज सर्टिफिकेट ज़रूरी है।
> 
> यह नियम Chhattisgarh Compulsory Registration of Marriages Rules, 2006 में दिया गया है। नियम के अनुसार, कोई भी सरकारी या अर्ध-सरकारी संस्था अपने कर्मचारी के रिकॉर्ड में बदलाव (जैसे नॉमिनेशन) नहीं कर सकती, जब तक कि कर्मचारी मैरिज रजिस्ट्रेशन सर्टिफिकेट की प्रमाणित कॉपी प्रस्तुत न करे। यह प्रक्रिया Urban Administration and development Department के अंतर्गत आती है।

*Latency: 22.36 seconds*

---

### Q15: What constitutes the definition of 'Local Authority' under the Chhattisgarh marriage rules?

**Hindi:** *छत्तीसगढ़ विवाह नियमों के तहत 'स्थानीय प्राधिकरण' की परिभाषा क्या है?*

**Hinglish:** *CG marriage rules ke under 'Local Authority' ki definition kya hai?*

#### 🇬🇧 English Response:
> Based on the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, the definition of 'Local Authority' is provided in Rule 2 (Definitions).
> 
> It is defined as: "Gram Panchayat or Municipality Or a Municipal Corporation as the case may be;"
> 
> In simple terms, a Local Authority can be a Gram Panchayat, a Municipality, or a Municipal Corporation, depending on the specific case.
> 
> This information is from the official document for the Marriage Registration & Certificate service, handled by the Urban Administration and development Department.

*Latency: 12.82 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ विवाह नियमों के अनुसार, 'स्थानीय प्राधिकरण' का अर्थ है: ग्राम पंचायत या नगरपालिका या नगर निगम, जैसा कि मामला हो। यह जानकारी शहरी प्रशासन और विकास विभाग से संबंधित है।

*Latency: 11.01 seconds*

#### 💬 Hinglish Response:
> CG marriage rules ke under, 'Local Authority' ki definition yeh hai:
> 'Gram Panchayat ya Municipality ya Municipal Corporation, jaisa case mein ho.'
> 
> Yeh jaankari Urban Administration and development Department ke under Marriage Registration & Certificate service se related hai.

*Latency: 13.04 seconds*

---

### Q16: What action is taken if someone destroys a page of the official Register of Marriages?

**Hindi:** *यदि कोई आधिकारिक विवाह रजिस्टर का एक पृष्ठ नष्ट कर देता है तो क्या कार्रवाई की जाती है?*

**Hinglish:** *Agar koi official Register of Marriages ka page faad de ya destroy kar de to kya action liya jata hai?*

#### 🇬🇧 English Response:
> प्रदान कयल गेल जानकारीक आधार पर, यदि कोनो व्यक्ति विवाहक आधिकारिक रजिस्टर (रजिस्टर ऑफ मैरिज) केँ नष्ट करैत अछि वा ओहिमे फेरबदल करैत अछि, तँ ओकरा 2,000 रुपयाक जुर्माना सँ दंडित कयल जाएत। ई दंड ओहि कोनो अन्य दंडक अतिरिक्त अछि जे अन्य कानूनक अंतर्गत देल जा सकैत अछि।
> 
> ई जानकारी शहरी प्रशासन आ विकास विभागक अंतर्गत विवाह पंजीकरण आ प्रमाण पत्र (मैरिज रजिस्ट्रेशन एंड सर्टिफिकेट) सेवा सँ संबंधित अछि।

*Latency: 15.17 seconds*

#### 🇮🇳 Hindi Response:
> अगर कोई आधिकारिक विवाह रजिस्टर का एक पृष्ठ नष्ट करता है, तो नियम 13 के अनुसार कार्रवाई की जाती है।
> 
> जो व्यक्ति रजिस्टर को नष्ट करता है, छेड़छाड़ करता है, या झूठी जानकारी देता है, उसे 2,000 रुपये का जुर्माना लगाया जाता है। इसके अलावा, किसी भी अन्य कानून के तहत होने वाली सजा भी लागू हो सकती है।
> 
> यह कार्रवाई 'शहरी प्रशासन और विकास विभाग' के तहत 'विवाह पंजीकरण एवं प्रमाण पत्र' सेवा के लिए की जाती है।

*Latency: 27.07 seconds*

#### 💬 Hinglish Response:
> अगर कोई अधिकारी रजिस्टर को नष्ट या छेड़छाड़ करता है, तो उसे दो हजार रुपये के जुर्माने से दंडित किया जाएगा। इसके अलावा, समय के साथ लागू होने वाले किसी भी अन्य कानून के तहत भी सजा हो सकती है।
> 
> यह कार्रवाई 'Marriage Registration & Certificate' सेवा के तहत 'Urban Administration and development Department' द्वारा की जाती है।

*Latency: 17.09 seconds*

---

## 3. Scheduled Castes & Scheduled Tribes Order 1950

### Q17: Which religions are recognized for Scheduled Castes status under the Constitution Order 1950?

**Hindi:** *संविधान आदेश 1950 के तहत अनुसूचित जाति की स्थिति के लिए किन धर्मों को मान्यता दी गई है?*

**Hinglish:** *Constitution Order 1950 ke under SC status ke liye kaun se religions recognized hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the religions recognized for Scheduled Castes status are Hindu, Sikh, and Buddhist.
> 
> The document states: "no person who professes any religion different from the Hindu, Sikh, or Buddhist religion shall be deemed to be a member of a Scheduled Caste."
> 
> This information is from the Constitution (Scheduled Castes) Order, १९५०, which is part of the SC/ST Certificate service under the Revenue and disaster management Department.

*Latency: 12.50 seconds*

#### 🇮🇳 Hindi Response:
> संविधान (अनुसूचित जातियाँ) आदेश, 1950 के अनुसार, अनुसूचित जाति की स्थिति के लिए, व्यक्ति का हिंदू, सिख या बौद्ध धर्म के अतिरिक्त किसी अन्य धर्म को मानना अनिवार्य है।
> 
> संविधान आदेश, 1950 में स्पष्ट रूप से उल्लेख है कि हिंदू, सिख या बौद्ध धर्म को मानने वाले व्यक्ति को अनुसूचित जाति में शामिल नहीं किया जा सकता। अतः, इस आदेश के तहत अनुसूचित जाति की स्थिति के लिए अन्य सभी धर्मों को मान्यता प्राप्त है।

*Latency: 15.60 seconds*

#### 💬 Hinglish Response:
> Constitution (Scheduled Castes) Order, १९५० के according, SC status के लिए सिर्फ Hindu, Sikh, और Buddhist religions recognized हैं।
> 
> Order में mention है कि जो लोग इन religions के अलावा किसी और religion को मानते हैं, उन्हें Scheduled Caste का member नहीं माना जाता। यह information official document content में दी गई है।

*Latency: 21.82 seconds*

---

### Q18: Under which part of the Scheduled Castes Order is Chhattisgarh listed?

**Hindi:** *अनुसूचित जाति आदेश के किस भाग के तहत छत्तीसगढ़ को सूचीबद्ध किया गया है?*

**Hinglish:** *SC Order ke kis part me Chhattisgarh listed hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the specific part of the Scheduled Castes Order under which Chhattisgarh is listed is not mentioned.
> 
> The context refers to the "Constitution (Scheduled Castes) Order, १९५०" and the "Revenue and disaster management Department" as the relevant authorities for issuing SC/ST certificates in Chhattisgarh. However, the list of parts for the order is not included in the provided text.
> 
> Information not available.

*Latency: 9.12 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 14.93 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.

*Latency: 13.54 seconds*

---

### Q19: Is the 'Chamar' caste recognized as a Scheduled Caste in Chhattisgarh, and what are its synonyms listed in the order?

**Hindi:** *क्या छत्तीसगढ़ में 'चमार' जाति को अनुसूचित जाति के रूप में मान्यता प्राप्त है, और आदेश में सूचीबद्ध इसके समानार्थी शब्द क्या हैं?*

**Hinglish:** *Kya CG me 'Chamar' caste ko SC ke roop me recognize kiya gaya hai, aur iske synonyms kya hain?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 36.43 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ में 'चमार' जाति को अनुसूचित जाति के रूप में मान्यता प्राप्त है।
> 
> आदेश में 'चमार' के लिए निम्नलिखित समानार्थी शब्द सूचीबद्ध हैं:
> 1. चमारारी
> 2. बैरवा
> 3. भाम्भी
> 4. जाटव
> 5. मोची
> 
> यह जानकारी राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़ के आधिकारिक दस्तावेज़ों के अनुसार है।

*Latency: 16.37 seconds*

#### 💬 Hinglish Response:
> Chamar caste ko Chhattisgarh mein SC ke roop mein recognize kiya gaya hai. Iske synonyms mein Chamar, Chamar-Rabidas, Chamar-Rohidas, Charmarkar, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Rohidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas, Chamar-Ravidas

*Latency: 29.03 seconds*

---

### Q20: Under entry 26 of Andhra Pradesh Scheduled Tribes, which tribe is recognized?

**Hindi:** *आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 26 के तहत किस जनजाति को मान्यता दी गई है?*

**Hinglish:** *Andhra Pradesh ST list ki entry 26 ke under kaun si tribe aati hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the tribe recognized under entry 26 of the Andhra Pradesh Scheduled Tribes is **Koya**.
> 
> The context lists the following under entry 26:
> "Koya, [Doli K0ya, Gutta K0]2, Kammara 10]2, Musara Koya, Oddi 10]2, Pattidi Koyal, Rajah, Rasha Koya, Lingadhari Koya (ordinary), Kottu K0ya, Bhine K0ya, Rajkoya"
> 
> Therefore, the recognized tribe is Koya.
> 
> Information not available.

*Latency: 6.21 seconds*

#### 🇮🇳 Hindi Response:
> आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 26 के तहत मान्यता प्राप्त जनजाति 'होलेय' है। यह जानकारी 'SC/ST Certificate' सेवा और 'राजस्व एवं आपदा प्रबंधन विभाग' से संबंधित है।

*Latency: 20.47 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.

*Latency: 15.34 seconds*

---

### Q21: Are 'Kharia' and 'Kharwar' listed as Scheduled Tribes in Chhattisgarh, and under which entries?

**Hindi:** *क्या छत्तीसगढ़ में 'खड़िया' और 'खरवार' को अनुसूचित जनजाति के रूप में सूचीबद्ध किया गया है, और किस प्रविष्टि के तहत?*

**Hinglish:** *Kya 'Kharia' aur 'Kharwar' CG me Scheduled Tribes ki list me hain, aur unki entry number kya hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 22.40 seconds*

#### 🇮🇳 Hindi Response:
> Jaankari uplabhd nahi hai.

*Latency: 31.50 seconds*

#### 💬 Hinglish Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 53.55 seconds*

---

### Q22: Is 'Mahyavanshi' recognized as a Scheduled Caste in Chhattisgarh?

**Hindi:** *क्या छत्तीसगढ़ में 'मह्यावंशी' को अनुसूचित जाति के रूप में मान्यता प्राप्त है?*

**Hinglish:** *Kya 'Mahyavanshi' caste ko CG me SC recognized mana jata hai?*

#### 🇬🇧 English Response:
> Based on the provided context, there is no information available to confirm whether 'Mahyavanshi' is recognized as a Scheduled Caste in Chhattisgarh.
> 
> The documents describe the process for obtaining a Scheduled Caste/Tribes Certificate and provide examples of other recognized categories, such as Other Backward Classes (OBCs), but they do not list all Scheduled Castes or specifically mention the 'Mahyavanshi' caste.
> 
> For the most accurate and up-to-date information, it is recommended to contact the relevant department directly.
> 
> Service: Scheduled Caste/Tribes Certificate, Department: Revenue & Disaster Management Department, Chhattisgarh.

*Latency: 16.73 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 31.65 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 29.83 seconds*

---

### Q23: Which tribal groups in Chhattisgarh are listed under the entry for 'Gond'?

**Hindi:** *छत्तीसगढ़ में कौन से जनजातीय समूह 'गोंड' प्रविष्टि के तहत सूचीबद्ध हैं?*

**Hinglish:** *CG me 'Gond' entry ke under kaun-kaun se tribal groups listed hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the following tribal groups in Chhattisgarh are listed under the entry for 'Gond':
> 
> 1.  **Gond**
> 2.  **Rajgond**
> 3.  **Koya**
> 4.  **Koya Rajkova**
> 
> These groups are mentioned in the context of the Constitution (Scheduled Tribes) Order, १९५०, specifically in the section for Chhattisgarh (PART XL). The text states: "Gond, Rajgond Junagadh, Rajkot and Surendranagar districts" and also lists "Koya, Rajkova" in relation to the Gond entry.
> 
> Information not available.

*Latency: 14.44 seconds*

#### 🇮🇳 Hindi Response:
> Jaankari uplabd nahi hai.

*Latency: 20.03 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 36.51 seconds*

---

### Q24: Under which entry number is 'Bharia Bhumia' listed for Chhattisgarh Scheduled Tribes?

**Hindi:** *छत्तीसगढ़ अनुसूचित जनजाति के लिए 'भारिया भूमिया' किस प्रविष्टि संख्या के तहत सूचीबद्ध है?*

**Hinglish:** *CG ST list me 'Bharia Bhumia' kis entry number par registered hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 55.04 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 21.24 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 28.55 seconds*

---

## 4. Social Status Act (Caste Certificate Rules)

### Q25: What are the powers of the High Level Caste Scrutiny Committee regarding false certificates?

**Hindi:** *झूठे प्रमाण पत्रों के संबंध में उच्च स्तरीय जाति छानबीन समिति की शक्तियां क्या हैं?*

**Hinglish:** *False certificates ke mamle me High Level Caste Scrutiny Committee ki kya powers hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the High Power Certification Scrutiny Committee has the following powers regarding false certificates:
> 
> 1.  **Punishment for Issuing False Certificates:** Any person or authority performing the functions of a Competent Authority who intentionally issues a false Social Status Certificate shall be punished with rigorous imprisonment for a term not less than three months but which may extend to two years, and with a fine which shall not be less than two thousand rupees and which may extend to twenty thousand rupees.
> 
> 2.  **Punishment for Obtaining False Certificates:** If a Social Status Certificate is cancelled under Section 8, the person obtaining such certificate shall be punished with rigorous imprisonment for a term not less than three months but which may extend to two years, and with a fine which shall not be less than two thousand rupees and which may extend to twenty thousand rupees.
> 
> 3.  **Cognizable and Non-Bailable Offences:** Offences punishable under Section 10 of the Act are cognizable, non-bailable, and may be tried summarily.
> 
> 4.  **Complaint Requirement:** No court shall take cognizance of an offence punishable under this section except upon a written complaint made by the High Power Certification Scrutiny Committee or on its behalf by any person authorized by it.
> 
> 5.  **Good Faith Protection:** If a Social Status Certificate was issued based on an affidavit and due diligence by the Competent Authority, the authority shall not be deemed to have intentionally issued a false certificate.
> 
> 6.  **Abetment of Offences:** Whoever abets any offence punishable under this Act shall be punished with the punishment provided for such offence in the Act.
> 
> 7.  **Civil Court Powers:** The High Power Certification Scrutiny Committee, along with other authorities, has the powers of a Civil Court under the Code of Civil Procedure, 1908, for matters like summoning witnesses, examining them on oath, and receiving evidence on affidavits.
> 
> 8.  **Good Faith Protection:** No suit, prosecution, or legal proceedings shall lie against any person for anything done in good faith or intended to be done in pursuance of the Act.
> 
> 9.  **Rule-Making Power:** The Government may make rules to carry out the purposes of the Act.
> 
> 10. **Removal of Difficulties:** The Government can make provisions to remove any difficulty in giving effect to the Act's provisions.
> 
> 11. **Bar on Civil Court Jurisdiction:** No civil court has jurisdiction to entertain, continue, or decide any suit or proceeding if it would be contrary to the provisions of the Act.
> 
> 12. **Burden of Proof:** The burden of proving the social status lies on the applicant.
> 
> For the specific powers of the High Power Certification Scrutiny Committee, the context primarily outlines the general powers of the Committee and the penalties for offences related to false certificates. The exact powers of the High Power Certification Scrutiny Committee are not detailed separately from the general powers of the Committee.

*Latency: 8.17 seconds*

#### 🇮🇳 Hindi Response:
> उच्च स्तरीय प्रमाणीकरण छानबीन समिति की मुख्य शक्ति यह है कि यदि समिति यह पाती है कि प्रमाण पत्र गलत तरीके से जारी किया गया है, तो वह प्रमाण पत्र को रद्द और जप्त करने का आदेश दे सकती है।
> 
> यह समिति एक निर्धारित प्रक्रिया का पालन करती है और प्रमाण पत्र को अमान्य घोषित करने से पहले, जिस व्यक्ति का सामाजिक प्रास्थिति प्रमाण पत्र विवादित है, उसे सुनवाई का उचित अवसर देना अनिवार्य है। समिति जिला स्तरीय समिति की रिपोर्ट की जांच करती है और इस मामले में आवश्यक कार्रवाई करती है।
> 
> संक्षेप में, समिति का मुख्य कार्य झूठे प्रमाण पत्र की पहचान करना और उसे रद्द एवं जप्त करने की सिफारिश करना है, बशर्ते कि प्राकृतिक न्याय के सिद्धांतों का पालन किया गया हो।
> 
> यह जानकारी **राजस्व एवं आपदा प्रबंधन विभाग** के अंतर्गत **अनुसूचित जाति/जनजाति प्रमाण पत्र** और **अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र** सेवाओं के लिए है।

*Latency: 17.55 seconds*

#### 💬 Hinglish Response:
> High Power Certification Scrutiny Committee के पास false social status certificate के मामलों में action लेने की कई important powers हैं।
> 
> **मुख्य Powers:**
> 1.  **Enquiry करना:** Committee किसी भी false certificate की enquiry कर सकती है, खासकर तब जब District Level Certificates Verification Committee या State Government द्वारा इसे refer किया गया हो।
> 2.  **Final Order Pass करना:** Enquiry के बाद, अगर committee को लगता है कि certificate गलत तरीके से या धोखाधड़ी से लिया गया है, तो वो एक final और conclusive order pass कर सकती है।
> 3.  **Certificate Cancel और Confiscate करना:** Committee के पास false certificate को cancel और confiscate करने का power है।
> 
> **इस Order के Consequences:**
> *   जिस व्यक्ति का certificate cancel होता है, उसे educational institution या public employment से disqualify कर दिया जाता है।
> *   किसी भी financial benefit, scholarship, या special treatment को recover किया जा सकता है।
> *   अगर किसी reserved seat या post पर admission या appointment लिया गया था, तो उस educational qualification को cancel माना जाता है।
> 
> ये powers ensure करती हैं कि false certificates के खिलाफ strict action लिया जाए।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग, छत्तीसगढ़ के लिए है।

*Latency: 19.33 seconds*

---

### Q26: What is the penalty for a government officer who issues a false caste certificate intentionally?

**Hindi:** *जानबूझकर झूठा जाति प्रमाण पत्र जारी करने वाले सरकारी अधिकारी के लिए क्या दंड है?*

**Hinglish:** *Janboojhkar jhootha caste certificate issue karne wale govt officer ke liye kya saza hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the penalty for a government officer who intentionally issues a false caste certificate is as follows:
> 
> The officer will be punished with rigorous imprisonment for a term which shall not be less than three months but which may extend to two years, and with a fine which shall not be less than two thousand rupees and which may extend to twenty thousand rupees.
> 
> This information is from the "Penalties" section of the user manual for the Scheduled Caste/Tribe Certificate service. The relevant section states: "Any person or authority performing the functions of Competent Authority under this Act who intentionally issues a false Social Status Certificate. shall be punished with rigorous imprisonment for a term which shall not be less than three months but which may extend to two years and with fine which shall not be less than two thousand rupees and which may extend to twenty thousand rupees."
> 
> This service is provided by the Revenue and Disaster Management Department of Chhattisgarh.
> 
> Information not available.

*Latency: 5.29 seconds*

#### 🇮🇳 Hindi Response:
> राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की गई जानकारी के अनुसार, जानबूझकर झूठा जाति प्रमाण पत्र जारी करने वाले किसी भी व्यक्ति के लिए दंड इस प्रकार है:
> 
> *   **कठोर कारावास**, जिसकी अवधि तीन माह से कम नहीं होगी, परंतु जो दो वर्ष तक बढ़ सकती है।
> *   **जुर्माना**, जो दो हजार रुपये से कम नहीं होगा, परंतु जो बीस हजार रुपये तक बढ़ सकता है।
> 
> यह दंड सामाजिक प्रास्थिति प्रमाणपत्र को कपटपूर्ण तरीके से जारी करने पर लागू होता है।
> 
> सेवा का नाम: अनुसूचित जाति/जनजाति प्रमाण पत्र
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग
> 
> जानकारी उपलब्ध नहीं है।

*Latency: 10.13 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 14.39 seconds*

---

### Q27: Does the cancellation of a caste certificate affect government employment benefits retrospectively?

**Hindi:** *क्या जाति प्रमाण पत्र के रद्दीकरण से सरकारी रोजगार लाभ पूर्वव्यापी प्रभाव से प्रभावित होते हैं?*

**Hinglish:** *Caste certificate cancel hone par kya sarkari naukri ke benefits pehle se wapas le liye jate hain?*

#### 🇬🇧 English Response:
> Yes, based on the provided context, the cancellation of a caste certificate can affect government employment benefits, and the effects can be both immediate and retrospective.
> 
> According to Section 9 of the user manual, if a Social Status Certificate is cancelled, a person who secured a reserved seat in education or public employment using that certificate "shall on cancellation of such certificate be liable to be dismissed from the public employment as the case may be, forthwith or be denied any other benefit or advantage enjoyed by virtue of such admission or appointment."
> 
> Furthermore, the context states that any financial benefits, such as scholarships, "shall be recovered from such person(s) as arrears of land revenue." This indicates that the cancellation can have a retrospective effect, as benefits already received may be taken back.
> 
> The service name and department are Revenue & Disaster Management Department, Chhattisgarh.

*Latency: 19.45 seconds*

#### 🇮🇳 Hindi Response:
> दिए गए संदर्भ के अनुसार, जाति प्रमाण पत्र के रद्दीकरण का सरकारी रोजगार लाभों पर पूर्वव्यापी प्रभाव पड़ता है या नहीं, इस बारे में स्पष्ट जानकारी नहीं है।
> 
> हालांकि, संदर्भ में यह उल्लेख है कि रद्दीकरण के आदेश के साथ प्रमाण पत्र को "तत्काल प्रभाव से रद्द" माना जाता है। इसके अतिरिक्त, संदर्भ में यह भी बताया गया है कि यदि कोई व्यक्ति गलत प्रमाण पत्र प्राप्त करता है, तो उस पर जांच की जा सकती है और कानूनी कार्रवाई की जा सकती है।
> 
> इसलिए, जबकि संदर्भ प्रमाण पत्र के तत्काल रद्दीकरण और गलत प्रमाण पत्र प्राप्त करने के परिणामों की पुष्टि करता है, यह स्पष्ट नहीं करता कि क्या रद्दीकरण पहले से प्राप्त लाभों को वापस लेने (पूर्वव्यापी प्रभाव) की ओर ले जाता है।

*Latency: 20.11 seconds*

#### 💬 Hinglish Response:
> जानकारी उपलब्ध नहीं है।
> 
> दी गई जानकारी में केवल जाति प्रमाण पत्र के लिए आवेदन करने की प्रक्रिया, आवश्यक दस्तावेज और समय सीमा के बारे में बताया गया है। इसमें इस बात का कोई उल्लेख नहीं है कि जाति प्रमाण पत्र रद्द होने पर पहले से मिले सरकारी नौकरी के लाभ वापस ले लिए जाते हैं या नहीं। यह जानकारी राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़ सरकार से संबंधित है।

*Latency: 14.95 seconds*

---

### Q28: Who is the designated competent authority to issue SC and ST certificates in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में अनुसूचित जाति और अनुसूचित जनजाति प्रमाण पत्र जारी करने के लिए नामित सक्षम प्राधिकारी कौन है?*

**Hinglish:** *CG me SC aur ST certificates issue karne ke liye competent authority kaun hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the designated competent authority to issue SC and ST certificates in Chhattisgarh is the **Sub-Divisional Officer (Revenue)**.
> 
> This information is specified in the user manual for the SC/ST Certificate, which states that the office for this purpose is the Tehsil Office and the competent authority is the Sub-Divisional Officer (Revenue).
> 
> This service is provided by the **Revenue and Disaster Management Department**.
> 
> For an appeal against the decision of the Sub-Divisional Officer (Revenue), the designated appellate authority is the **Collector**.

*Latency: 14.68 seconds*

#### 🇮🇳 Hindi Response:
> राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत 'सक्षम प्राधिकारी' (Competent Authority) को अनुसूचित जाति और अनुसूचित जनजाति प्रमाण पत्र जारी करने के लिए नामित किया गया है।
> 
> सेवा: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4), विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 41.08 seconds*

#### 💬 Hinglish Response:
> छत्तीसगढ़ में अनुसूचित जाति/जनजाति प्रमाण पत्र जारी करने के लिए, **राजस्व और आपदा प्रबंधन विभाग** जिम्मेदार है।
> 
> सेवा: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4) के लिए, विभाग: राजस्व और आपदा प्रबंधन विभाग है।

*Latency: 13.12 seconds*

---

### Q29: Under what conditions can the competent authority reject a caste certificate application?

**Hindi:** *सक्षम प्राधिकारी किन परिस्थितियों में जाति प्रमाण पत्र आवेदन को अस्वीकार कर सकता है?*

**Hinglish:** *Competent authority kin halato me caste certificate application reject kar sakta hai?*

#### 🇬🇧 English Response:
> प्रदत्त संदर्भ के आधार पर, एक सक्षम प्राधिकारी (कॉम्पिटेंट अथॉरिटी) किसी जाति प्रमाण पत्र (कास्ट सर्टिफिकेट) के आवेदन को अस्वीकार कर सकता है, यदि वह इस निष्कर्ष पर पहुँचता है कि ऐसा करने के लिए "पर्याप्त कारण" मौजूद हैं।
> 
> प्राधिकारी के लिए निम्नलिखित प्रक्रियात्मक आवश्यकताएँ अनिवार्य हैं:
> 1. अस्वीकृति के कारणों को लिखित रूप में दर्ज करना।
> 2. आवेदक को अस्वीकृति और उसके कारणों के बारे में सूचित करना।
> 
> संदर्भ में उन विशिष्ट "पर्याप्त कारणों" का उल्लेख नहीं किया गया है जो अस्वीकृति का आधार बन सकते हैं।
> 
> यह जानकारी **राजस्व एवं आपदा प्रबंधन विभाग** के अंतर्गत **अनुसूचित जाति/अनुसूचित जनजाति/अन्य पिछड़ा वर्ग जाति प्रमाण पत्र** (आई डी: 4) सेवा के लिए है।

*Latency: 12.92 seconds*

#### 🇮🇳 Hindi Response:
> सेवा सेटू छत्तीसगढ़ पोर्टल के संदर्भ के अनुसार, सक्षम प्राधिकारी जाति प्रमाण पत्र आवेदन को निम्नलिखित परिस्थितियों में अस्वीकार कर सकता है:
> 
> 1. **आवश्यक दस्तावेजों की कमी:** यदि आवेदन के साथ आवश्यक दस्तावेज संलग्न नहीं हैं, तो प्राधिकारी आवेदन को अस्वीकार कर सकता है। इनमें शामिल हैं:
>     * पूर्वजों के दस्तावेज (जैसे जाति, सर्वेक्षण रिकॉर्ड)।
>     * निवास का प्रमाण।
>     * जन्म या मृत्यु का प्रमाण पत्र।
>     * पिता का आय प्रमाण पत्र।
>     * यह प्रमाण कि आवेदक के माता-पिता सरकारी कर्मचारी हैं।
>     * सभी दस्तावेजों की उचित रूप से प्रमाणित प्रतियां।
>     * आवेदन पत्र पर उचित डाक शुल्क और पूर्ण पता।
> 
> 2. **22 दिनों के भीतर:** आवेदन जमा करने के बाद, यदि सक्षम प्राधिकारी को दस्तावेजों में कोई कमी या त्रुटि मिलती है, तो वह आवेदन को अस्वीकार कर सकता है। यह अस्वीकृति आवेदन जमा करने के 22 कार्य दिवसों के भीतर की जानी चाहिए।
> 
> 3. **जानकारी प्रदान करने में असमर्थता:** यदि आवेदक कुछ आवश्यक दस्तावेज प्रदान नहीं कर पाता है, तो वह "जानकारी न दे पाने का ज्ञापन" (फॉर्म-3C) प्रस्तुत कर सकता है। प्राधिकारी तब जांच करेगा। यदि जांच के बाद, प्राधिकारी आवेदक के स्पष्टीकरण या साक्ष्यों से संतुष्ट नहीं होता है, तो वह आवेदन को अस्वीकार कर सकता है।
> 
> 4. **धोखाधड़ी या गलत तरीके से प्राप्त करना:** यदि यह पाया जाता है कि जाति प्रमाण पत्र "गलत तरीके से या धोखाधड़ी से" प्राप्त किया गया है, तो आवेदन अस्वीकार कर दिया जाएगा। यह प्रक्रिया जिला स्तर के प्रमाणपत्र सत्यापन समिति द्वारा की जाती है। यदि समिति को धोखाधड़ी का प्रथम दृष्टया (prima-facie) साक्ष्य मिलता है, तो वह मामले को उच्च शक्ति प्रमाणन जांच समिति (High Power Certification Scrutiny Committee) को भेज सकती है, जो अंततः अस्वीकृति का आदेश दे सकती है।
> 
> सेवा सेटू छत्तीसगढ़ पोर्टल, राजस्व और आपदा प्रबंधन विभाग।

*Latency: 17.92 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 28.70 seconds*

---

### Q30: What happens to the school admission of a child if their parent's caste certificate is found to be false?

**Hindi:** *यदि किसी बच्चे के माता-पिता का जाति प्रमाण पत्र झूठा पाया जाता है तो उसके स्कूल प्रवेश का क्या होता है?*

**Hinglish:** *Agar kisi bache ke parent ka caste certificate fake nikle to uske school admission ka kya hota hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 42.24 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 22.16 seconds*

#### 💬 Hinglish Response:
> Provided context ke according, agar kisi bache ke parent ka caste certificate fake ya fraudulent nikla, to uska certificate immediate effect se cancel maana jaata hai.
> 
> Iske saath hi, Chhattisgarh SC/ST/OBC Act ke Section 8-13 ke under action bhi shuru kiya jaata hai. Iska matlab hai ki:
> 
> 1.  **Certificate Cancel ho jaata hai:** Certificate ko "deemed to be cancelled with immediate effect" maana jaata hai.
> 2.  **Admission par asar:** Agar bache ka school admission uske parent ke caste certificate ke basis par hua tha, to admission ki bhi review ho sakti hai. Kyunki certificate hi admission ka proof hota hai, uske cancel hone se admission ka basis khatam ho jaata hai.
> 
> Service: Scheduled Caste/Scheduled Tribe Certificate
> Department: Revenue & Disaster Management Department, Chhattisgarh
> Jaankari uplabd nahi hai.

*Latency: 25.34 seconds*

---

### Q31: Can a person request the review of their rejected caste certificate application, and what is the process?

**Hindi:** *क्या कोई व्यक्ति अपने अस्वीकृत जाति प्रमाण पत्र आवेदन की समीक्षा का अनुरोध कर सकता है, और इसकी प्रक्रिया क्या है?*

**Hinglish:** *Kya koi apne rejected caste certificate application ka review maang sakta hai, aur iska process kya hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the process for handling a rejected application involves escalating the matter to a higher-level committee.
> 
> The document describes the role of the **Scrutiny Committee** as the higher authority that can review decisions. While the context does not explicitly use the term "review" or "appeal," it indicates that the Scrutiny Committee is the body that can take action, such as forwarding cases for inquiry to a Vigilance Cell.
> 
> The final order from the Scrutiny Committee is sent to the applicant, and if they request a copy, it is provided with an appropriate fee. Therefore, the process involves seeking a review through the institutional structure, with the Scrutiny Committee being the final authority mentioned in the context.
> 
> Service: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4) Department: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 19.18 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, एक व्यक्ति अस्वीकृत जाति प्रमाण पत्र आवेदन की समीक्षा का अनुरोध कर सकता है। यह प्रक्रिया मुख्य रूप से **जिला स्तरीय प्रमाणपत्र सत्यापन समिति** और **उच्च शक्ति प्रमाणपत्र जांच समिति** द्वारा संचालित की जाती है।
> 
> समीक्षा प्रक्रिया का विवरण इस प्रकार है:
> 
> 1. **जिला स्तरीय समिति द्वारा समीक्षा:** यदि जिला स्तरीय समिति को लगता है कि प्रमाणपत्र गलत तरीके से प्राप्त किया गया है, तो वह मामले को उच्च समिति को भेज सकती है। महत्वपूर्ण बात यह है कि यदि समिति किसी व्यक्ति के प्रमाणपत्र के विरुद्ध प्रतिकूल निष्कर्ष निकालती है, तो उसे उस व्यक्ति को सुनवाई का उचित अवसर देना चाहिए।
> 
> 2. **उच्च शक्ति प्रमाणपत्र जांच समिति को प्रेषण:** जिला स्तरीय समिति के निष्कर्षों की जांच उच्च शक्ति जांच समिति द्वारा की जाती है। यह समिति प्रमाणपत्र को रद्द करने और जब्त करने का आदेश दे सकती है।
> 
> 3. **सुनवाई का अवसर:** समीक्षा प्रक्रिया का एक मुख्य हिस्सा आवेदक को अपना पक्ष रखने का मौका देना है। समिति द्वारा प्रतिकूल निष्कर्ष निकालने से पहले सुनवाई का अवसर देना अनिवार्य है।
> 
> 4. **परिणाम:** यदि उच्च समिति प्रमाणपत्र को रद्द करने का निर्णय लेती है, तो यह अंतिम माना जाता है। इसके बाद, यदि प्रमाणपत्र गलत पाया जाता है, तो संबंधित व्यक्ति के विरुद्ध कानूनी कार्रवाई की जा सकती है।
> 
> यह प्रक्रिया सुनिश्चित करती है कि किसी भी अस्वीकृत आवेदन की निष्पक्ष जांच हो और व्यक्ति को अपना पक्ष रखने का उचित अवसर मिले।
> 
> सेवा केंद्र, राजस्व एवं आपदा प्रबंधन विभाग, छत्तीसगढ़।

*Latency: 17.67 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.
> 
> Diye gaye context mein rejected application ke review ka process nahi bataya gaya hai. Yeh documents application process, required documents, aur forms ke baare mein hain, lekin rejection ke baad kya karna hai, iska koi zikr nahi hai.
> 
> Aap jis department se application ki thi, wahan se ya Scrutiny Committee se directly sampark kar sakte hain. Unse review ke liye pooch sakte hain.
> 
> Sewasethu Chhattisgarh portal ke liye, yeh service hai: Scheduled Caste/Scheduled Tribe Certificate (ID: 4), Department: राजस्व एवं आपदा प्रबंधन विभाग.

*Latency: 16.00 seconds*

---

### Q32: Is there any protection for actions taken in good faith by officers under the Social Status Act?

**Hindi:** *क्या सामाजिक प्रास्थिति अधिनियम के तहत अधिकारियों द्वारा सद्भावना में की गई कार्रवाइयों के लिए कोई सुरक्षा है?*

**Hinglish:** *Kya Social Status Act ke under officers dwara good faith me kiye gaye kaamo ko protection milti hai?*

#### 🇬🇧 English Response:
> Yes, there is protection for actions taken in good faith under the Social Status Act. According to the context, Section 17 of the Act states: "No suit, prosecution or other legal proceedings shall lie against any person for anything which is done in good faith or intended to be done in pursuance of this Act or the rules made thereunder."
> 
> This means that if an officer or authority is acting based on the information provided and within the scope of the Act, they are protected from legal action, as long as their actions were done in good faith.
> 
> Information not available.

*Latency: 5.84 seconds*

#### 🇮🇳 Hindi Response:
> Provided context mein social status act ke under officials ke good faith mein ki gayi actions ke liye koi specific protection nahi di gayi hai.
> 
> Context mein false ya fraudulent social status certificate issue karne ke consequences par focus kiya gaya hai, jaise ki punishment aur court action ke liye government ki previous sanction ki zaroorat. Isliye, good faith mein ki gayi actions ke liye direct protection ka zikr yahan nahi hai. Jaankari uplabd nahi hai.

*Latency: 14.58 seconds*

#### 💬 Hinglish Response:
> Haan, Social Status Act ke under officers dwara good faith mein kiye gaye kaamo ko protection milti hai.
> 
> Act ke Section 17 mein yeh clearly mention hai ki agar koi bhi person ya authority iss Act ke under ya iske rules ke hisaab se good faith mein koi kaam karta hai, toh uske khilaaf koi bhi legal proceedings (jaise suit ya prosecution) nahi ki ja sakti.
> 
> Iska matlab hai ki jo officers iss Act ke under apni duties nibha rahe hain, agar unhone good faith mein kaam kiya hai, toh unhe legal action se protection milega. Yeh protection Chhattisgarh ke Revenue & Disaster Management Department ke under aane wale officers ke liye bhi applicable hai.

*Latency: 15.10 seconds*

---

## 5. Ordinary Gazette Notification for Name Change

### Q33: What is the minimum non-judicial stamp paper value required for the name change affidavit?

**Hindi:** *नाम परिवर्तन हलफनामे के लिए आवश्यक न्यूनतम गैर-न्यायिक स्टांप पेपर मूल्य क्या है?*

**Hinglish:** *Name change ke affidavit ke liye minimum kitne rupaye ka non-judicial stamp paper lagta hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the minimum non-judicial stamp paper value required for the name change affidavit is ₹50.
> 
> The required document is:
> - A Notarized Affidavit In Form-Iii On A ₹ 50 Non-Judicial Stamp Paper (Should Not Be More Than 03 Months Old From The Date Of Application).
> 
> For reference, the application fee for this service is ₹30, which is separate from the stamp paper value.
> 
> Information not available.

*Latency: 5.57 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन के हलफनामे के लिए आवश्यक न्यूनतम गैर-न्यायिक स्टांप पेपर का मूल्य 50 रुपये है। यह हलफनामा फॉर्म-III में नोटराइज्ड होना चाहिए।
> 
> यह सेवा 'सरकारी मुद्रण और लेखन सामग्री विभाग' के अंतर्गत 'नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना' है।

*Latency: 16.71 seconds*

#### 💬 Hinglish Response:
> Name change ke affidavit ke liye minimum ₹ 50 ka non-judicial stamp paper lagta hai. Yeh Form-Iii par notarized affidavit hona chahiye aur stamp paper 03 months se zyada purana nahi hona chahiye.

*Latency: 15.95 seconds*

---

### Q34: Which form number is used to publish the notice of name change in a local newspaper?

**Hindi:** *स्थानीय समाचार पत्र में नाम परिवर्तन का नोटिस प्रकाशित करने के लिए किस फॉर्म नंबर का उपयोग किया जाता है?*

**Hinglish:** *Local newspaper me name change notice publish karne ke liye kis form number ka use kiya jata hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the form number used to publish the notice of name change in a local newspaper is **Form-I**.
> 
> The required documents list for the "Ordinary Gazette Notification for Name Change" service (ID: 201) specifies:
> - **SNo 3:** The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application).
> 
> This document is mandatory for the application.
> 
> Information not available.

*Latency: 5.62 seconds*

#### 🇮🇳 Hindi Response:
> स्थानीय समाचार पत्र में नाम परिवर्तन का नोटिस प्रकाशित करने के लिए फॉर्म-I का उपयोग किया जाता है। यह नोटिस स्थानीय समाचार पत्र में प्रकाशित किया जाना चाहिए, और इसकी प्रति 3 महीने से अधिक पुरानी नहीं होनी चाहिए।

*Latency: 11.78 seconds*

#### 💬 Hinglish Response:
> Local newspaper me name change notice publish karne ke liye, Form-I ka use kiya jata hai. Yeh service ke liye ek mandatory document hai.

*Latency: 17.06 seconds*

---

### Q35: What is the state government's SLA processing time in days for a name change gazette notification?

**Hindi:** *नाम परिवर्तन राजपत्र अधिसूचना के लिए राज्य सरकार का SLA प्रसंस्करण समय दिनों में क्या है?*

**Hinglish:** *Name change gazette notification ke liye state government ka SLA time kitne dino ka hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the state government's SLA processing time for an Ordinary Gazette Notification for Name Change is 29 days.
> 
> This service is handled by the Government Printing and Stationery Department.

*Latency: 10.93 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन राजपत्र अधिसूचना के लिए राज्य सरकार का SLA प्रसंस्करण समय 29 दिन है।
> 
> यह सेवा 'सरकारी मुद्रण और स्टेशनरी विभाग' के अंतर्गत 'सरकारी राजपत्र में नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना' (ID: 201) है।

*Latency: 9.74 seconds*

#### 💬 Hinglish Response:
> Sewa Setu Chhattisgarh portal par 'Ordinary Gazette Notification for Name Change' service ke liye state government ka SLA time 29 din ka hai. Yeh service Government Printing and Stationery Department dwara sanchalit hai.

*Latency: 15.51 seconds*

---

### Q36: Can the name change deed form be signed by family members as witnesses?

**Hindi:** *क्या नाम परिवर्तन विलेख फॉर्म पर परिवार के सदस्य गवाह के रूप में हस्ताक्षर कर सकते हैं?*

**Hinglish:** *Kya name change deed form me family members witness ke roop me sign kar sakte hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the name change deed form (Form-Ii) requires the names, signatures, and addresses of two witnesses. However, the context does not specify whether these witnesses can be family members.
> 
> Service: Ordinary Gazette Notification for Name Change (ID: 201)
> Department: Government Printing and Stationery Department

*Latency: 11.15 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 20.38 seconds*

#### 💬 Hinglish Response:
> हाँ, name change deed form में witnesses के रूप में family members sign कर सकते हैं।
> 
> Service: Ordinary Gazette Notification for Name Change (ID: 201) के लिए, एक "Deed Form" की ज़रूरत होती है जिसमें "02 Witnesses" के नाम, signature और address शामिल होते हैं। यह mandatory है। साथ ही, witnesses की government-issued identity card भी ज़रूरी है।
> 
> यह process Government Printing and Stationery Department के under आता है।

*Latency: 14.37 seconds*

---

### Q37: Under what head of account must the treasury challan for name change publication be deposited?

**Hindi:** *नाम परिवर्तन प्रकाशन के लिए ट्रेजरी चालान किस खाता शीर्ष के तहत जमा किया जाना चाहिए?*

**Hinglish:** *Name change publication ke liye treasury challan kis head of account me jama karna hota hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the treasury challan for the name change publication must be deposited under the head of account: **Printing and Stationery**.
> 
> This information is found in the "Required Documents" section for the "Ordinary Gazette Notification for Name Change" service, which specifies that the challan should be from the "Head – 0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts" branch of the State Bank of India.
> 
> Information not available.

*Latency: 6.38 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन प्रकाशन के लिए ट्रेजरी चालान '0058 मुद्रण एवं लेखन सामग्री, 102 राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां' के खाता शीर्ष के तहत जमा किया जाना चाहिए।

*Latency: 14.63 seconds*

#### 💬 Hinglish Response:
> Name change publication ke liye jo treasury challan deposit karna hota hai, uska head of account '0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts' hai.
> 
> Yeh information Ordinary Gazette Notification for Name Change service ke required documents mein di gayi hai. Sewa Setu Chhattisgarh portal aur Government Printing and Stationery Department.

*Latency: 16.41 seconds*

---

### Q38: Is the name change notification published in a Weekly Gazette or an Extraordinary Gazette?

**Hindi:** *क्या नाम परिवर्तन अधिसूचना साप्ताहिक राजपत्र में प्रकाशित होती है या असाधारण राजपत्र में?*

**Hinglish:** *Name change notification weekly gazette me publish hota hai ya extraordinary gazette me?*

#### 🇬🇧 English Response:
> Based on the provided context, the name change notification is published in an **Extraordinary Gazette**.
> 
> The context mentions that the notification is published in the "Publication Of Gazette" and the document format references "Gazette of India, Extraordinary, १९५०". This indicates it is not a regular Weekly Gazette but an Extraordinary Gazette.
> 
> For the Ordinary Gazette Notification for Name Change service, the time limit is 29 days.
> 
> Information not available.

*Latency: 6.04 seconds*

#### 🇮🇳 Hindi Response:
> आपके प्रश्न के अनुसार, नाम परिवर्तन अधिसूचना साधारण राजपत्र (Ordinary Gazette) में प्रकाशित होती है।
> 
> सेवा सेटू छत्तीसगढ़ पोर्टल के संदर्भ में, "साधारण राजपत्र अधिसूचना" (Ordinary Gazette Notification) नाम की सेवा का विवरण उपलब्ध है। आवश्यक दस्तावेजों की सूची में "सरकारी मुद्रणालय राजनांदगांव से मुद्रित तथा प्रकाशित" (Government Printing and Stationery Department) का उल्लेख है, जो साधारण राजपत्र में प्रकाशन की ओर संकेत करता है।
> 
> संदर्भ में यह स्पष्ट नहीं है कि यह साप्ताहिक राजपत्र है या कोई अन्य प्रकार का साधारण राजपत्र। सेवा का नाम "साधारण राजपत्र अधिसूचना" ही मुख्य जानकारी है।
> 
> अतः, उपलब्ध जानकारी के आधार पर, अधिसूचना साधारण राजपत्र में प्रकाशित होती है।
> 
> **सेवा का नाम:** साधारण राजपत्र अधिसूचना (ID: 201)
> **विभाग:** सरकारी मुद्रण और लेखन सामग्री, छत्तीसगढ़

*Latency: 18.36 seconds*

#### 💬 Hinglish Response:
> Aapke sawal ka jawab hai ki name change notification **Ordinary Gazette** mein publish hota hai.
> 
> Source 1 mein di gayi jaankari ke anusar, service ka naam hi "Ordinary Gazette Notification for Name Change" hai. Is process mein aap Sewa Setu portal par apply karte hain aur ek local newspaper mein notice publish karna zaroori hota hai, jo ordinary gazette ke liye standard procedure hai.
> 
> Yeh service Government Printing and Stationery Department dwara handle ki jaati hai.

*Latency: 26.66 seconds*

---

### Q39: What form number is used for the name change deed?

**Hindi:** *नाम परिवर्तन विलेख के लिए किस फॉर्म नंबर का उपयोग किया जाता है?*

**Hinglish:** *Name change deed ke liye kis form number ka use kiya jata hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the form number used for the name change deed is **Form-II**.
> 
> The required documents list for the "Ordinary Gazette Notification for Name Change" service (ID: 201) specifies:
> - **SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses.** (Mandatory: Yes)
> 
> This indicates that the deed form is referred to as **Form-II** in the application process.
> 
> Information not available.

*Latency: 5.36 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन विलेख के लिए प्ररूप-दो (Form-Ii) का उपयोग किया जाता है। यह 'साधारण राजपत्र अधिसूचना' सेवा का एक अनिवार्य दस्तावेज़ है, जिसका सर्विस ID 201 है। यह दस्तावेज़ 'शासकीय मुद्रण एवं लेखन सामग्री विभाग' द्वारा संचालित किया जाता है।

*Latency: 14.02 seconds*

#### 💬 Hinglish Response:
> Sewa Setu Chhattisgarh portal par name change ke liye koi specific form number mention nahi kiya gaya hai. Service ID 201 ke under Ordinary Gazette Notification for Name Change ke liye required documents mein Form-I, Form-II, aur Form-III ka reference diya gaya hai, lekin koi specific form number nahi bataya gaya hai. Aapko application form mein diye gaye fields ke according details fill karne honge.

*Latency: 6.33 seconds*

---

### Q40: Is it required to submit identity cards for the witnesses of the name change deed?

**Hindi:** *क्या नाम परिवर्तन विलेख के गवाहों के पहचान पत्र जमा करना आवश्यक है?*

**Hinglish:** *Kya name change deed ke witnesses ke ID cards submit karna zaroori hai?*

#### 🇬🇧 English Response:
> Yes, it is required.
> 
> For the 'Ordinary Gazette Notification for Name Change' service, you must submit the identity card of the witnesses. The required documents list specifically states: "Identity card of witnesses issued by the government (Mandatory: Yes)".
> 
> This information is from the Government Printing and Stationery Department.

*Latency: 14.62 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, नाम परिवर्तन विलेख के गवाहों के पहचान पत्र जमा करना अनिवार्य है।
> 
> सेवा सेटू केंद्र पर आवेदन करते समय गवाहों के पहचान पत्र (शासन द्वारा जारी) जमा करना आवश्यक है। यह सेवा 'सरकारी मुद्रण एवं लेखन सामग्री विभाग' द्वारा प्रदान की जाती है।

*Latency: 13.42 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.

*Latency: 18.12 seconds*

---

### Q41: What is the required amount for the State Bank of India challan for name change publication?

**Hindi:** *नाम परिवर्तन प्रकाशन के लिए भारतीय स्टेट बैंक के चालान की आवश्यक राशि क्या है?*

**Hinglish:** *Name change publication ke liye State Bank of India ke challan ki kitni amount chahiye?*

#### 🇬🇧 English Response:
> The required amount for the State Bank of India challan for name change publication is ₹430.
> 
> Information not available.

*Latency: 5.35 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन प्रकाशन के लिए भारतीय स्टेट बैंक के चालान की आवश्यक राशि 430 रुपये है। यह चालान किसी भी स्टेट बैंक ऑफ इंडिया की शाखा से जारी होना चाहिए।
> 
> यह जानकारी 'नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना' सेवा से संबंधित है, जो 'शासकीय मुद्रण एवं लेखन सामग्री विभाग' द्वारा प्रदान की जाती है।

*Latency: 12.48 seconds*

#### 💬 Hinglish Response:
> Name change publication ke liye State Bank of India ke challan ki amount ₹ 430/- hai. Ye Ordinary Gazette Notification for Name Change service ke liye required hai.

*Latency: 11.91 seconds*

---

### Q42: How long must an affidavit be kept before applying, or is there a validity limit?

**Hindi:** *आवेदन करने से पहले हलफनामे को कितने समय तक रखा जा सकता है, या क्या कोई वैधता सीमा है?*

**Hinglish:** *Apply karne se pehle affidavit kitna purana ho sakta hai, kya iski koi validity limit hai?*

#### 🇬🇧 English Response:
> Based on the provided context, there is no information about the validity limit or how long an affidavit must be kept.
> 
> The context does state that the application, which includes the affidavit, must be submitted within a prescribed time limit of one month. For details on the specific validity period of the affidavit itself, you would need to refer to the full set of rules or contact the Revenue & Disaster Management Department directly.
> 
> Service: Scheduled Caste/Tribe Certificate (ID: 4) or Other Backward Class Certificate (ID: 5) | Department: Revenue & Disaster Management Department

*Latency: 24.27 seconds*

#### 🇮🇳 Hindi Response:
> आवेदन करने से पहले, हलफनामे की वैधता तीन महीने है।
> 
> हलफनामा आवेदन की तिथि से तीन महीने से अधिक पुराना नहीं होना चाहिए।
> 
> यह जानकारी 'साधारण गजट सूचना के लिए नाम परिवर्तन' सेवा से संबंधित है, जो सरकारी प्रिंटिंग और स्टेशनरी विभाग के अंतर्गत आती है।

*Latency: 16.16 seconds*

#### 💬 Hinglish Response:
> दिए गए संदर्भ में, affidavit की validity limit के बारे में कोई विशिष्ट जानकारी नहीं है।
> 
> संदर्भ में यह उल्लेख है कि verification committee को application मिलने के बाद एक महीने के भीतर apply करना होता है। Affidavit applicant द्वारा application के समय पर बनाया गया एक sworn statement होता है। इसलिए, affidavit की age की कोई limit context में mention नहीं की गई है।
> 
> अगर आपको official service के लिए exact जानकारी चाहिए, तो आप Revenue & Disaster Management Department से संपर्क कर सकते हैं।

*Latency: 25.79 seconds*

---

## 6. Out of Scope Queries

### Q43: How do I download the digitally signed copy of my land records (B-I/Khasra) in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में मैं अपने भूमि रिकॉर्ड (बी-आई/खसरा) की डिजिटल हस्ताक्षरित प्रति कैसे डाउनलोड करूं?*

**Hinglish:** *CG me apni zameen ka naksha ya B-1 Khasra digital signed copy kaise download kare?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 8.79 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 9.75 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.

*Latency: 14.85 seconds*

---

### Q44: What is the procedure to register a rental agreement in Raipur?

**Hindi:** *रायपुर में रेंट एग्रीमेंट पंजीकृत करने की प्रक्रिया क्या है?*

**Hinglish:** *Raipur me rent agreement register karne ka kya process hai?*

#### 🇬🇧 English Response:
> Based on the provided context, I am unable to answer your question about the procedure to register a rental agreement in Raipur. The context contains information about marriage registration, domicile certificates, and OBC certificates, but does not include any details regarding rental agreement registration procedures.
> 
> Information not available.

*Latency: 5.23 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 13.61 seconds*

#### 💬 Hinglish Response:
> Di gayi jaankari me rent agreement register karne ka process nahi hai. Jaankari uplabd nahi hai.

*Latency: 25.44 seconds*

---

### Q45: How can a student apply for a post-matric scholarship online in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में कोई छात्र पोस्ट-मैट्रिक छात्रवृत्ति के लिए ऑनलाइन आवेदन कैसे कर सकता है?*

**Hinglish:** *CG me post matric scholarship ke liye student online kaise apply kare?*

#### 🇬🇧 English Response:
> To apply for a post-matric scholarship online in Chhattisgarh, you can follow these steps:
> 
> 1.  **Visit the Official Portal**: Go to the Sewa Setu Chhattisgarh portal at [https://sewasetu.cgstate.gov.in/home?lang=en](https://sewasetu.cgstate.gov.in/home?lang=en).
> 
> 2.  **Navigate to the Scholarship Section**: Look for the "Post-Matric Scholarship" or a similar scholarship service on the portal.
> 
> 3.  **Fill Out the Application Form**: You will need to provide details such as:
>     *   General details (name, date of birth, etc.)
>     *   Academic details (course, college, etc.)
>     *   Financial details (family income, etc.)
>     *   Upload required documents (like caste certificate, income certificate, etc.).
> 
> 4.  **Submit and Track**: After filling in the form, submit it and track its status online.
> 
> **Important Notes**:
> *   The application process is entirely online through the Sewa Setu portal.
> *   Ensure all required documents are uploaded in the specified format.
> *   The time limit for processing is typically 22 days, as per the SC/ST Certificate service.
> 
> If you need further assistance, you can contact the Sewa Setu Kendra or the Revenue and Disaster Management Department.
> 
> For more details, you can refer to the official specification for the SC/ST Certificate service, which outlines the required documents and application process.
> 
> **Service Name**: Post-Matric Scholarship Application  
> **Department**: Revenue and Disaster Management Department  
> **Portal**: Sewa Setu Chhattisgarh  
> 
> If you have any specific questions or need help with the application, feel free to ask!

*Latency: 9.19 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में पोस्ट-मैट्रिक छात्रवृत्ति के लिए ऑनलाइन आवेदन करने हेतु, आपको निम्नलिखित चरणों का पालन करना होगा:
> 
> 1. **आधिकारिक वेबसाइट पर जाएं**: आप https://sewasetu.cgstate.gov.in/home?lang=hi पर जा सकते हैं।
> 2. **खाता बनाएं**: वेबसाइट पर "नया उपयोगकर्ता" (New User) के विकल्प पर क्लिक करके पंजीकरण करें।
> 3. **लॉगिन करें**: पंजीकरण के बाद, अपने क्रेडेंशियल के साथ लॉगिन करें।
> 4. **आवेदन खोजें**: वेबसाइट पर "योजना खोज" (Scheme Search) या "आवेदन करें" (Apply) विकल्प खोजें।
> 5. **आवेदन भरें**: आवेदन फॉर्म में सभी आवश्यक विवरण भरें।
> 6. **दस्तावेज़ अपलोड करें**: आवश्यक दस्तावेज़ों को अपलोड करें।
> 7. **शुल्क का भुगतान करें**: ऑनलाइन शुल्क का भुगतान करें।
> 8. **आवेदन जमा करें**: अंत में, आवेदन जमा करें।
> 
> **महत्वपूर्ण बिंदु**:
> - आवेदन की समय सीमा और शुल्क संरचना के बारे में अधिक जानकारी के लिए, आप वेबसाइट पर उपलब्ध "योजना खोज" अनुभाग देख सकते हैं।
> - यदि आपको कोई समस्या आती है, तो आप सहायता के लिए सेवा केंद्र (Sewa Setu Kendra) से संपर्क कर सकते हैं।
> 
> **सेवा केंद्र**:
> - **संपर्क**: सेवा सेतु केंद्र
> - **शुल्क**: आवेदन शुल्क ₹30.0 (ऑनलाइन और ऑफलाइन दोनों)
> 
> **नोट**: पोस्ट-मैट्रिक छात्रवृत्ति के लिए विशिष्ट विवरण इस संदर्भ में उपलब्ध नहीं हैं। आपको वेबसाइट पर विस्तृत जानकारी देखनी होगी।

*Latency: 12.62 seconds*

#### 💬 Hinglish Response:
> Sewa Setu Chhattisgarh portal par post matric scholarship ke liye online apply karne ke liye, aapko ye steps follow karne honge:
> 
> 1. **Sewa Setu Portal par jayein**: Aap https://sewasetu.cgstate.gov.in/home?lang=en par ja sakte hain.
> 
> 2. **Login karein**: Apne account mein login karein. Agar aapke paas account nahi hai, toh naya account banayein.
> 
> 3. **Application Form bharein**: Application form mein sabhi zaroori details bharein, jaise:
>    - General Details
>    - Beneficiary Details
>    - Educational Details
>    - Income Details
>    - Bank Account Details
> 
> 4. **Documents Upload karein**: Required documents ki list check karein aur unhe upload karein.
> 
> 5. **Fee Pay karein**: Online fee pay karein, jo ki ₹30.0 hai.
> 
> 6. **Submit karein**: Form submit kar dein.
> 
> Agar aapko koi problem aati hai, toh aap Sewa Setu Kendra se help le sakte hain.
> 
> **Note**: Post matric scholarship ke liye specific documents aur process ki jaankari yahan available nahi hai. Aapko official website par jaakar detailed information check karni hogi.
> 
> **Service Name**: Post Matric Scholarship
> **Department**: Revenue and disaster management Department (ya relevant department)
> 
> Jaankari uplabd nahi hai.

*Latency: 18.23 seconds*

---

### Q46: What are the subsidies available for installing rooftop solar panels in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में रूफटॉप सोलर पैनल लगाने के लिए क्या सब्सिडी उपलब्ध है?*

**Hinglish:** *CG me rooftop solar panel lagwane ke liye kya subsidies milti hain?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 5.52 seconds*

#### 🇮🇳 Hindi Response:
> Jaankari uplabd nahi hai.

*Latency: 12.14 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai. Di gayi jaankari mein rooftop solar panel lagwane ke liye milne vali subsidies ka koi zikr nahi hai.

*Latency: 16.92 seconds*

---

### Q47: How can I check the status of my ration card application online?

**Hindi:** *मैं अपने राशन कार्ड आवेदन की स्थिति ऑनलाइन कैसे देख सकता हूं?*

**Hinglish:** *Apne ration card application ka status online kaise check kare?*

#### 🇬🇧 English Response:
> To check the status of your ration card application online, you can use the official Sewa Setu Chhattisgarh portal.
> 
> Here's how you can do it:
> 
> 1.  **Visit the Sewa Setu Portal:** Go to the official website: [https://sewasetu.cgstate.gov.in/home?lang=en](https://sewasetu.cgstate.gov.in/home?lang=en)
> 
> 2.  **Find the Application Status Section:** Look for a section on the website related to "Application Status" or "Track Application." This is typically found in the main menu or under a "Services" or "My Applications" tab.
> 
> 3.  **Enter Your Details:** You will need to provide some information to locate your application. This usually includes:
>     *   Your application number or reference ID.
>     *   Your name.
>     *   Your date of birth.
>     *   Your address.
> 
> 4.  **View the Status:** After entering your details, the system will display the current status of your application (e.g., submitted, under review, approved, rejected).
> 
> **Important Note:** The provided context does not contain specific information about checking the status of a ration card application. The information available is for the **Domicile Certificate** service. For the most accurate and up-to-date instructions, please refer to the official Sewa Setu portal or contact their support.
> 
> For the Domicile Certificate service, the time limit is 7 days, and you can apply through a Sewa Setu Kendra or online.
> 
> If you need help with the Domicile Certificate, you can find the required documents and application form fields on the portal.
> 
> Information not available.

*Latency: 7.11 seconds*

#### 🇮🇳 Hindi Response:
> आप अपने राशन कार्ड आवेदन की स्थिति ऑनलाइन देख सकते हैं। Sewa Setu Chhattisgarh पोर्टल पर जाकर आप अपनी आवेदन स्थिति की जांच कर सकते हैं।
> 
> **सेवा का नाम:** राशन कार्ड आवेदन स्थिति
> **विभाग:** राजस्व और आपदा प्रबंधन विभाग
> 
> **स्थिति जांचने के लिए:**
> 1. Sewa Setu पोर्टल पर जाएं: https://sewasetu.cgstate.gov.in/home?lang=hi
> 2. लॉगिन करने के बाद "आवेदन स्थिति" (Application Status) या "ट्रैक आवेदन" (Track Application) विकल्प चुनें।
> 3. अपनी आवेदन संख्या या आधार नंबर दर्ज करें।
> 4. स्थिति की जानकारी प्राप्त करें।
> 
> **जरूरी दस्तावेज:**
> - राशन कार्ड आवेदन संख्या
> - आधार कार्ड
> - मोबाइल नंबर (सत्यापन के लिए)
> 
> **समय सीमा:** 7 दिन
> 
> **शुल्क:** ₹30.0 (ऑनलाइन)
> 
> **संपर्क:** सेवा सेतु केंद्र
> 
> आपकी आवेदन स्थिति की जांच के लिए यह जानकारी पर्याप्त है।

*Latency: 9.70 seconds*

#### 💬 Hinglish Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 19.07 seconds*

---

### Q48: What is the process to apply for a water connection in Bilaspur municipal corporation?

**Hindi:** *बिलासपुर नगर निगम में जल कनेक्शन के लिए आवेदन करने की प्रक्रिया क्या है?*

**Hinglish:** *Bilaspur municipal corporation me water connection apply karne ka kya process hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 5.37 seconds*

#### 🇮🇳 Hindi Response:
> जल कनेक्शन के लिए आवेदन करने की प्रक्रिया यहाँ दी गई है:
> 
> 1. **पंजीकरण**: सबसे पहले, आपको सेवा सेतु पोर्टल पर पंजीकरण करना होगा। आप सेवा सेतु केंद्र पर जाकर या ऑनलाइन पंजीकरण करके ऐसा कर सकते हैं।
> 2. **योजना खोज**: सेवा सेतु पोर्टल पर, "जल कनेक्शन" योजना खोजें और उस पर क्लिक करें।
> 3. **बुनियादी जानकारी**: आवेदन पत्र भरें, जिसमें आपका पता, पिन कोड, जिला, तहसील, तहसील, और परिवार के मुखिया से संबंध जैसे विवरण शामिल होंगे।
> 4. **दस्तावेज़ अपलोड**: आवश्यक दस्तावेज़ जैसे निवास का प्रमाण, आय प्रमाण, और अन्य आवश्यक कागजात अपलोड करें।
> 5. **सत्यापन**: जमा करने के बाद, आपके आवेदन की समीक्षा की जाएगी।
> 6. **शुल्क भुगतान**: ऑनलाइन शुल्क का भुगतान करें, जो ₹30.0 है।
> 7. **आवेदन जमा करना**: जमा करने के बाद, आपको एक आवेदन संख्या प्राप्त होगी। इसका उपयोग करके आप अपने आवेदन की स्थिति की जांच कर सकते हैं।
> 
> सेवा सेतु केंद्र पर जाकर या सेवा सेतु पोर्टल पर ऑनलाइन आवेदन करके इस प्रक्रिया को पूरा किया जा सकता है।

*Latency: 17.58 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.

*Latency: 15.52 seconds*

---

### Q49: How do I register a complaint on the Chhattisgarh electricity board portal?

**Hindi:** *छत्तीसगढ़ बिजली बोर्ड पोर्टल पर शिकायत कैसे दर्ज करें?*

**Hinglish:** *CG electricity board portal par shikayat kaise register kare?*

#### 🇬🇧 English Response:
> I'm sorry, but the information you're looking for is not available in the provided context. The context contains details about various certificates like OBC, SC/ST, and Domicile certificates from the Revenue and Disaster Management Department, but it does not include any information about registering complaints on the Chhattisgarh electricity board portal.
> 
> If you need help with a different service, please let me know.
> 
> Information not available.

*Latency: 5.05 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ बिजली बोर्ड पोर्टल पर शिकायत दर्ज करने के लिए, आपको निम्नलिखित चरणों का पालन करना होगा:
> 
> 1. **पोर्टल पर जाएं**: अपने कंप्यूटर या लैपटॉप में वेब ब्राउज़र खोलें और `www.cgvcl.com` या `www.cggvcl.com` टाइप करें।
> 2. **लॉगिन करें**: पोर्टल पर लॉगिन करने के लिए अपना यूजरनेम और पासवर्ड दर्ज करें।
> 3. **शिकायत दर्ज करें**: लॉगिन करने के बाद, "शिकायत दर्ज करें" या "सेवा" (Service) विकल्प पर क्लिक करें।
> 4. **शिकायत का विवरण भरें**: शिकायत में समस्या का विवरण, जैसे बिजली की कटौती, बिल भुगतान में समस्या, या अन्य संबंधित जानकारी शामिल करें।
> 5. **सबमिट करें**: शिकायत दर्ज करने के बाद, उसे सबमिट करें।
> 
> **नोट**: यदि आपके पास ऑनलाइन शिकायत दर्ज करने की सुविधा नहीं है, तो आप ग्राहक सेवा केंद्र पर जाकर या हेल्पलाइन नंबर पर कॉल करके भी शिकायत दर्ज कर सकते हैं।
> 
> **सेवा**: छत्तीसगढ़ बिजली बोर्ड (CGVCL/CGGVCL)
> **विभाग**: ऊर्जा विभाग, छत्तीसगढ़ राज्य।
> 
> जानकारी उपलब्ध नहीं है।

*Latency: 8.13 seconds*

#### 💬 Hinglish Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 12.87 seconds*

---

### Q50: What is the interest rate for the Chhattisgarh Gramin Bank housing loan?

**Hindi:** *छत्तीसगढ़ ग्रामीण बैंक गृह ऋण के लिए ब्याज दर क्या है?*

**Hinglish:** *CG Gramin Bank home loan ka interest rate kya hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 6.06 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ ग्रामीण बैंक गृह ऋण के लिए ब्याज दरें बैंक की नीतियों और वर्तमान बाजार स्थितियों के आधार पर भिन्न हो सकती हैं। सामान्यतः, गृह ऋण पर ब्याज दरें 8.5% से 12% प्रति वर्ष के बीच होती हैं, लेकिन यह बैंक के विशिष्ट उत्पाद और आवेदक की क्रेडिट हिस्ट्री पर निर्भर करता है।
> 
> **जानकारी उपलब्ध नहीं है।**

*Latency: 5.61 seconds*

#### 💬 Hinglish Response:
> सेवा केंद्र में जाकर या ऑनलाइन पोर्टल पर जाकर आप CG Gramin Bank की होम लोन ब्याज दर की जानकारी प्राप्त कर सकते हैं। यह जानकारी बैंक की आधिकारिक वेबसाइट या शाखा से प्राप्त की जा सकती है।
> 
> सेवा केंद्र से संपर्क करने के लिए:
> - Sewa Setu Kendra: ₹30.0
> - ऑनलाइन: ₹30.0
> 
> आप Sewa Setu पोर्टल पर आवेदन करने के लिए यहाँ जा सकते हैं: https://sewasetu.cgstate.gov.in/home?lang=en
> 
> सेवा केंद्र में जाकर आप बैंक से सीधे बात करके भी ब्याज दर की जानकारी ले सकते हैं।

*Latency: 6.73 seconds*

---

## Evaluation Summary & Metrics

- **Total Executed Queries:** 150
- **Total Time Taken:** 2475.77 seconds
- **Average Latency:** 16.51 seconds/query
