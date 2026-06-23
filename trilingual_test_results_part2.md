# SewaSetu RAG Chatbot Trilingual Evaluation Report - Part 2

This report presents the second batch of testing results of the chatbot in three languages: **English**, **Hindi**, and **Hinglish** across all citizen services and out-of-scope scenarios. Queries were executed globally without specifying service serial numbers.

## Test Configuration
- **API Server:** `http://localhost:8000/api/chat`
- **Date & Time:** 2026-06-22 15:24:16
- **Total Query Runs:** 150 (50 English + 50 Hindi + 50 Hinglish)

## Table of Contents
- [1. Domicile Certificate (Chhattisgarh Domicile Criteria)](#1-domicile-certificate-chhattisgarh-domicile-criteria)
- [2. Marriage Registration & Certificate](#2-marriage-registration-and-certificate)
- [3. Scheduled Castes & Scheduled Tribes Order 1950](#3-scheduled-castes-and-scheduled-tribes-order-1950)
- [4. Social Status Act (Caste Certificate Rules)](#4-social-status-act-caste-certificate-rules)
- [5. Other Backward Classes (OBC) Certificate](#5-other-backward-classes-obc-certificate)
- [6. Ordinary Gazette Notification for Name Change](#6-ordinary-gazette-notification-for-name-change)
- [7. Out of Scope Queries](#7-out-of-scope-queries)

---

## 1. Domicile Certificate (Chhattisgarh Domicile Criteria)

### Q1: If the applicant was born in Chhattisgarh, does this satisfy Criteria A by itself?

**Hindi:** *यदि आवेदक का जन्म छत्तीसगढ़ में हुआ था, तो क्या यह अपने आप में मानदंड A को संतुष्ट करता है?*

**Hinglish:** *Agar applicant CG me paida hua tha, to kya ye apne aap me Criteria A ko pura karta hai?*

#### 🇬🇧 English Response:
> Yes, if the applicant was born in Chhattisgarh, this satisfies Criteria A by itself.
> 
> According to the Domicile Certificate criteria, Criteria A is "Born in CG (Birth Certificate)". The text lists this as the first option under Criteria A, followed by other conditions connected with "OR". This means meeting just one of these conditions is sufficient.
> 
> Therefore, being born in Chhattisgarh and providing a birth certificate fulfills the requirement for Criteria A on its own.
> 
> For the Domicile Certificate service provided by the Revenue and disaster management Department, this single criterion is enough to proceed.

*Latency: 12.93 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, यदि आप 'जन्म स्थान' (जन्म प्रमाण पत्र) के मानदंड की बात कर रहे हैं, तो छत्तीसगढ़ में जन्म लेना मानदंड A को संतुष्ट करता है।
> 
> उपयोगकर्ता नियमावली के अनुसार, मानदंड A का विवरण इस प्रकार है:
> "Criterion one: a. Born in CG (Birth Certificate) OR"
> 
> हालांकि, समग्र रूप से Domicile Certificate प्राप्त करने के लिए, आवेदक को 'मानदंड A' और 'मानदंड B' दोनों को पूरा करना आवश्यक है, जैसा कि नियमावली में उल्लेखित है।
> 
> सेवा का नाम: Domicile Certificate
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 40.57 seconds*

#### 💬 Hinglish Response:
> Haan, agar applicant Chhattisgarh mein paida hua hai aur uske paas birth certificate hai, to wo apne aap Criteria A ko pura karta hai.
> 
> Context ke according, "Born in CG (Birth Certificate)" Criteria A ke under ek option hai. Isliye, agar applicant ka birth certificate hai, to wo is criterion ko meet karta hai.

*Latency: 15.35 seconds*

---

### Q2: Are employee details required in the application form if the parent is a state PSU employee?

**Hindi:** *यदि माता-पिता राज्य पीएसयू के कर्मचारी हैं, तो क्या आवेदन पत्र में कर्मचारी विवरण आवश्यक हैं?*

**Hinglish:** *Agar parents state PSU employee hain, to kya application form me employee details dena padega?*

#### 🇬🇧 English Response:
> Based on the provided context, employee details are required in the application form if the parent is a state PSU employee.
> 
> The context specifies that for the OBC Certificate application, a supporting document is required: "Service Certificate / Identity Card Of Father / Guardian" (Source 2, SNo 3). This document would typically include employee details if the parent is a state PSU employee.
> 
> Additionally, the context mentions that for the Domicile Certificate, a supporting document is required: "Father/ Guardian Service Certificate / Identity Card (If The Applicant Is Under Govt./Semi Govt.)" (Source 3, SNo 3).
> 
> Therefore, if the parent is a state PSU employee, their employee details would be required as part of the "Service Certificate / Identity Card Of Father / Guardian" or "Father/ Guardian Service Certificate / Identity Card" supporting documents.
> 
> Information not available.

*Latency: 7.50 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 17.31 seconds*

#### 💬 Hinglish Response:
> हाँ, अगर आपके parents state PSU employee हैं, तो उनकी details application के साथ ज़रूरी हैं।
> 
> Context के according, अगर applicant के father या mother government employee हैं, तो उनके post को verify करने वाले documents (जैसे service number, post, etc.) submit करने पड़ते हैं। यह information application form के साथ required documents में माँगी जाती है।
> 
> ये services 'राजस्व एवं आपदा प्रबंधन विभाग' द्वारा provide की जाती हैं।

*Latency: 15.93 seconds*

---

### Q3: What happens if the applicant fails to provide Class 8 or Class 5 board exam certificates for Criteria B?

**Hindi:** *यदि आवेदक मानदंड B के लिए कक्षा 8 या कक्षा 5 की बोर्ड परीक्षा के प्रमाण पत्र प्रदान करने में विफल रहता है तो क्या होता है?*

**Hinglish:** *Agar applicant Criteria B ke liye class 8 ya class 5 board exam certificate na de paye to kya hoga?*

#### 🇬🇧 English Response:
> Based on the provided context, if an applicant fails to provide the Class 8 or Class 5 board exam certificates, they can still meet Criteria B for a Domicile Certificate.
> 
> The context states that Criteria B has two options connected by "OR":
> a) Three years of formal education in CG.
> b) Passed one of the board exams (Class 5, 8, 10, 12) from CG.
> 
> Therefore, if the applicant does not have the board exam certificate, they can still qualify by fulfilling the first option, which is having three years of formal education in the state.
> 
> This information is for the Domicile Certificate service under the Revenue and Disaster Management Department.

*Latency: 13.17 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 12.39 seconds*

#### 💬 Hinglish Response:
> Agar applicant class 8 ya class 5 board exam certificate na de paye, to bhi unhe Criteria B ke under eligible maana ja sakta hai. Kyunki Criteria B mein 'OR' (ya) ka use kiya gaya hai.
> 
> Agar applicant ne board exam certificate nahi diya, to woh 'Three yrs of formal education in CG' wala alternative option fulfill karke criteria meet kar sakte hain.

*Latency: 13.31 seconds*

---

### Q4: Can a resident who has lived in Chhattisgarh for 30 years get a domicile certificate even if they have no land records?

**Hindi:** *क्या कोई निवासी जो 30 वर्षों से छत्तीसगढ़ में रह रहा है, भूमि रिकॉर्ड न होने पर भी मूल निवासी प्रमाण पत्र प्राप्त कर सकता है?*

**Hinglish:** *Kya CG me 30 saal se rehne wala resident zameen ke kagaz na hone par bhi domicile certificate le sakta hai?*

#### 🇬🇧 English Response:
> हाँ, दिए गए context के आधार पर, Chhattisgarh में 30 साल तक रहने वाला निवासी बिना land records के भी domicile certificate के लिए eligible हो सकता है।
> 
> Source 3 में दी गई criteria के मुताबिक, domicile certificate के लिए एक key requirement applicant या उनके parents का Chhattisgarh में continuous 25 साल तक रहना है। चूंकि applicant 30 साल से रह रहा है, इसलिए यह criterion पूरा हो जाता है।
> 
> Context में land records को domicile certificate के लिए mandatory requirement के रूप में नहीं बताया गया है। इसके बजाय, यह long-term residency, parents की residency, या education-related criteria जैसे कि formal schooling या board exams pass करने पर focus करता है।
> 
> इसलिए, land records न होने से applicant disqualify नहीं होगा, बशर्ते वे residency criteria को पूरा करते हों।
> 
> Sewasetu Chhattisgarh portal पर Domicile Certificate के लिए, यह service **राजस्व एवं आपदा प्रबंधन विभाग (Department of Revenue and Disaster Management)** द्वारा provide की जाती है।

*Latency: 12.72 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 35.36 seconds*

#### 💬 Hinglish Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 35.58 seconds*

---

### Q5: What are the form fields related to the guardian's details in the domicile application?

**Hindi:** *मूल निवासी आवेदन में अभिभावक के विवरण से संबंधित फॉर्म फ़ील्ड क्या हैं?*

**Hinglish:** *Domicile application form me guardian details se related kaun-kaun se fields hote hain?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}

*Latency: 1205.00 seconds*

#### 🇮🇳 Hindi Response:
> मूल निवासी प्रमाण पत्र आवेदन में, अभिभावक से संबंधित निम्नलिखित फॉर्म फ़ील्ड हैं:
> 
> 1. हितग्राही के अभिभावक का प्रकार: यह फील्ड अभिभावक के प्रकार (जैसे पिता, माता) का चयन करने के लिए है।
> 2. हितग्राही के अभिभावक का नाम: यह फील्ड अभिभावक का नाम दर्ज करने के लिए है।
> 3. हितग्राही के अभिभावक का व्यवसाय: यह फील्ड अभिभावक के व्यवसाय के बारे में जानकारी देने के लिए है।
> 
> ये विवरण आवेदन की प्रक्रिया को पूर्ण करने के लिए आवश्यक हैं।
> सेवा: मूल निवासी प्रमाण पत्र, विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 23.39 seconds*

#### 💬 Hinglish Response:
> Domicile application form me guardian se related ye fields hote hain:
> 
> 1.  **Beneficiary Guardian Type** (Mandatory: Yes)
> 2.  **Beneficiary Guardian name** (Mandatory: Yes)
> 3.  **Guardians Occupation of Beneficiary** (Mandatory: No)
> 
> Yeh details Chhattisgarh ke Revenue and disaster management Department ke Domicile Certificate service ke liye hain.

*Latency: 15.51 seconds*

---

### Q6: Is there any time limit specified under the SLA for the disposal of a Domicile Certificate application?

**Hindi:** *क्या मूल निवासी प्रमाण पत्र आवेदन के निपटान के लिए SLA के तहत कोई समय सीमा निर्दिष्ट है?*

**Hinglish:** *Kya domicile certificate application process hone ke liye SLA ke under koi time limit di gayi hai?*

#### 🇬🇧 English Response:
> Yes, there is a time limit specified for the disposal of a Domicile Certificate application. The Service Level Agreement (SLA) for this service is 7 days. This information is from the Domicile Certificate service, provided by the Revenue and disaster management Department.

*Latency: 9.66 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, मूल निवासी प्रमाण पत्र आवेदन के निपटान के लिए SLA के तहत समय सीमा निर्दिष्ट है।
> 
> राजस्व एवं आपदा प्रबंधन विभाग के अनुसार, इस सेवा के लिए आवेदन जमा करने की समय सीमा 30 कार्य दिवस है।
> 
> सेवा का नाम: मूल निवासी प्रमाण पत्र, विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 12.22 seconds*

#### 💬 Hinglish Response:
> हाँ, domicile certificate application process के लिए Service Level Agreement (SLA) के under time limit दी गई है।
> 
> Context में दो अलग-अलग time limits mention की गई हैं:
> 
> 1. **7 days:** एक source के according, time limit 7 days है।
> 2. **30 working days:** दूसरे source, जो SLA details का table है, उसके according, time limit 30 working days है।
> 
> यह ध्यान रखना ज़रूरी है कि context में दो अलग-अलग information दी गई हैं।

*Latency: 14.29 seconds*

---

### Q7: Who is the first appellate authority if a domicile certificate is rejected?

**Hindi:** *यदि मूल निवासी प्रमाण पत्र अस्वीकार कर दिया जाता है तो प्रथम अपीलीय प्राधिकारी कौन होता है?*

**Hinglish:** *Agar domicile certificate reject ho jaye to first appellate authority kaun hota hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 13.13 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 13.51 seconds*

#### 💬 Hinglish Response:
> अगर डोमिसाइल सर्टिफिकेट reject हो जाता है, तो पहली अपीलीय प्राधिकारी कलेक्टर (कलेक्टर) होती है।
> 
> यह जानकारी 'डोमिसाइल सर्टिफिकेट' (ID: 7) सेवा के लिए दी गई है, जो राजस्व और आपदा प्रबंधन विभाग के अंतर्गत आती है।

*Latency: 12.54 seconds*

---

### Q8: What supporting documents are accepted as 25 years residence proof of the father?

**Hindi:** *पिता के 25 वर्ष के निवास प्रमाण के रूप में कौन से सहायक दस्तावेज स्वीकार किए जाते हैं?*

**Hinglish:** *Father ke 25 years residence proof ke roop me kaun se supporting documents accept kiye jate hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the specific documents accepted as 25 years residence proof of the father are not listed.
> 
> The context does confirm that a 25-year continuous residence of a parent in Chhattisgarh is one of the criteria for obtaining a Domicile Certificate. However, the documents listed for residence proof in the context are for a 15-year stay and include:
> 
> *   Birth Certificate
> *   Father/ Guardian Service Certificate
> *   Job Service Certificate / Identity Card (if applicable)
> *   Voters Identity Card
> *   Land And House Document
> *   Birth Information Form
> *   Certificate From Ward Member, Local Mla/Mp
> *   Ration Card
> *   Electricity Bill
> 
> For the exact documents required for the 25-year proof, you may need to consult the official application form or contact the Sewa Setu Kendra.
> 
> Service: Domicile Certificate, Department: Revenue and disaster management Department.

*Latency: 14.00 seconds*

#### 🇮🇳 Hindi Response:
> आपके प्रश्न के अनुसार, पिता के 25 वर्ष के निवास प्रमाण के लिए कोई एक विशिष्ट दस्तावेज नहीं है। हालांकि, निवास के प्रमाण के लिए निम्नलिखित दस्तावेज स्वीकार किए जा सकते हैं:
> 
> 1. पिता/अभिभावक सेवा प्रमाण पत्र
> 2. भूमि और घर का दस्तावेज
> 3. राशन कार्ड
> 4. मतदाता पहचान पत्र
> 5. जन्म प्रमाण पत्र
> 
> ये दस्तावेज निवास के मानदंड को पूरा करने के लिए उपयोग किए जाते हैं।

*Latency: 11.95 seconds*

#### 💬 Hinglish Response:
> Aapke sawal ke liye, context mein father ke 25 saal ke continuous residence proof ke liye koi ek specific list nahi di gayi hai. Par jo documents relevant maane jaate hain, woh ye hain:
> 
> *   Proof of Residence for २५ साल (continuous residence ka general proof).
> *   Father/Guardian ka Service Certificate (agar woh government employee hain).
> *   Property documents (jaise land aur house ka document) agar father ke naam par property hai.
> *   Ration Card, Voter ID Card, ya Electricity Bill jaise documents jo residence prove karte hain.
> *   Affidavit (notarized statement).
> 
> Yeh information Sewa Setu Chhattisgarh portal ke Domicile Certificate (Service ID: 7) se related hai.

*Latency: 36.13 seconds*

---

## 2. Marriage Registration & Certificate

### Q9: What is the penalty if a person willfully destroys or tampers with the official Register of Marriages under Rule 13?

**Hindi:** *नियम 13 के तहत यदि कोई व्यक्ति जानबूझकर आधिकारिक विवाह रजिस्टर को नष्ट या छेड़छाड़ करता है तो क्या जुर्माना है?*

**Hinglish:** *Rule 13 ke under agar koi marriage register ko nuksan pahunchaye ya tamper kare to kya penalty hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the penalty for willfully destroying or tampering with the official Register of Marriages is a fine of rupees two thousand. This fine is in addition to any other punishment that may be awarded under other laws in effect at the time.
> 
> This information is from the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, under the Marriage Registration & Certificate service, managed by the Urban Administration and development Department.

*Latency: 17.98 seconds*

#### 🇮🇳 Hindi Response:
> नियम 13 के अनुसार, यदि कोई व्यक्ति जानबूझकर आधिकारिक विवाह रजिस्टर को नष्ट या छेड़छाड़ करता है, तो उसे दो हजार रुपये का जुर्माना देना होगा। यह जुर्माना किसी भी अन्य कानून के तहत दी जाने वाली सजा के अतिरिक्त होगा।
> 
> यह जानकारी Urban Administration and development Department की Marriage Registration & Certificate सेवा से संबंधित है।

*Latency: 12.31 seconds*

#### 💬 Hinglish Response:
> Rule 13 ke according, agar koi marriage register ko nuksan pahunchaye ya tamper kare, to penalty yeh hai:
> 
> Uske liye Rs. 2,000 ka fine lagaya ja sakta hai. Iske alawa, uss samay ke kisi aur law ke under jo bhi punishment ho, woh bhi lag sakti hai.
> 
> Yeh information Chhattisgarh Compulsory Registration of Marriages Rules, 2006 ke under hai.

*Latency: 19.44 seconds*

---

### Q10: Can a citizen inspect the Register of Marriages, and is there any fee for doing so?

**Hindi:** *क्या कोई नागरिक विवाह रजिस्टर का निरीक्षण कर सकता है, और क्या ऐसा करने के लिए कोई शुल्क है?*

**Hinglish:** *Kya koi citizen marriage register check ya inspect kar sakta hai, aur iski fee kitni hai?*

#### 🇬🇧 English Response:
> Yes, a citizen can inspect the Register of Marriages. According to the rules, the Register of marriages shall be open to inspection at all reasonable times.
> 
> Yes, there is a fee for inspection. The certified extracts from the register can be provided to an applicant on payment of a fee of Rs. 20/-.
> 
> Service: Marriage Registration & Certificate
> Department: Urban Administration and development Department

*Latency: 12.10 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, एक नागरिक विवाह रजिस्टर का निरीक्षण कर सकता है। ई-निस्ट्रिक्ट पोटटल पर आवेिन की स्थिगत देखी जा सकती है। प्रमाणित प्रति प्राप्त करने के लिए ₹20/- का शुल्क देना पड़ता है। यह सेवा नगरीय प्रशासन एवं विकास विभाग द्वारा प्रदान की जाती है।

*Latency: 23.06 seconds*

#### 💬 Hinglish Response:
> Ji haan, ek citizen marriage register check ya inspect kar sakta hai.
> 
> Register sabhi reasonable time par public inspection ke liye khula rehta hai. Iske liye Rs. 20 ki fee deni padti hai, aur certified extracts mil jaate hain. Ye service Urban Administration and development Department ke under aati hai.

*Latency: 27.53 seconds*

---

### Q11: Is a marriage certificate mandatory for changing a wife's surname in her bank account records?

**Hindi:** *क्या पत्नी का बैंक खाता रिकॉर्ड में उपनाम बदलने के लिए विवाह प्रमाण पत्र अनिवार्य है?*

**Hinglish:** *Kya wife ka bank account me surname change karne ke liye marriage certificate mandatory hai?*

#### 🇬🇧 English Response:
> Based on the provided context, a marriage certificate is not mandatory for changing a wife's surname in her bank account records. The context does not contain any information regarding the process of changing a surname in bank account records. The available services and documents listed are specific to marriage registration and name change notifications, but none of them directly address the requirements for updating a bank account. Therefore, the information is not available in the provided context.
> 
> Information not available.

*Latency: 6.06 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।
> 
> दी गई जानकारी में यह नहीं बताया गया है कि बैंक रिकॉर्ड में पत्नी का नाम बदलने के लिए विवाह प्रमाण पत्र अनिवार्य है या नहीं। यह जानकारी केवल विवाह पंजीकरण की प्रक्रिया और आवश्यक दस्तावेजों के बारे में है। सेवा केंद्र या बैंक से सीधे संपर्क करना बेहतर होगा।

*Latency: 10.95 seconds*

#### 💬 Hinglish Response:
> बैंक अकाउंट में नाम बदलने की प्रक्रिया के बारे में दी गई जानकारी में विवरण नहीं है। संदर्भ में केवल नाम परिवर्तन के लिए गजट अधिसूचना और विवाह पंजीकरण की सेवाओं का विवरण है। इसलिए, इस संबंध में जानकारी उपलब्ध नहीं है।

*Latency: 22.46 seconds*

---

### Q12: What is the maximum time allowed for a citizen to file the first appeal against refusal to register a marriage?

**Hindi:** *विवाह पंजीकृत करने से इनकार करने के खिलाफ नागरिक को पहली अपील दायर करने के लिए अधिकतम कितना समय दिया जाता है?*

**Hinglish:** *Shadi registration refuse hone ke baad citizen ke paas first appeal karne ke liye maximum kitna time hota hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the maximum time allowed for a citizen to file the first appeal against a refusal to register a marriage is **thirty days**.
> 
> This period begins from the date the citizen receives the order of refusal from the Registrar. This information is specified in Rule 5 of the Chhattisgarh Compulsory Registration of Marriages Rules, 2006.
> 
> The service is Marriage Registration & Certificate, handled by the Urban Administration and development Department.

*Latency: 14.22 seconds*

#### 🇮🇳 Hindi Response:
> विवाह पंजीकृत करने से इनकार के खिलाफ पहली अपील दायर करने के लिए नागरिक को अधिकतम 30 दिन दिए जाते हैं।
> 
> यह अपील आदेश प्राप्त होने की तिथि से 30 दिनों के भीतर दायर की जानी चाहिए। इस अपील के साथ 30 रुपये का शुल्क भी जमा करना होगा।
> 
> यह प्रक्रिया 'विवाह पंजीकरण एवं प्रमाण पत्र' सेवा के अंतर्गत आती है, जो नगरीय प्रशासन एवं विकास विभाग द्वारा संचालित है।

*Latency: 11.42 seconds*

#### 💬 Hinglish Response:
> Agar aapki marriage registration refuse ho jaati hai, toh aapke paas pehli appeal karne ke liye **30 din** ka time hota hai.
> 
> Aap ye appeal Registrar ke order ke 30 din ke andar Chief Registrar ke paas file kar sakte hain.
> 
> Ye service Urban Administration and development Department ke under aati hai.

*Latency: 14.82 seconds*

---

### Q13: Does the definition of marriage under the CG rules apply to Christian or Muslim marriages?

**Hindi:** *क्या छत्तीसगढ़ नियमों के तहत विवाह की परिभाषा ईसाई या मुस्लिम विवाहों पर लागू होती है?*

**Hinglish:** *Kya CG rules ke under marriage ki definition Christian ya Muslim shadiyo par bhi apply hoti hai?*

#### 🇬🇧 English Response:
> Yes, the definition of marriage under the CG rules applies to Christian and Muslim marriages.
> 
> According to Rule 2(e) of the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, "Marriage" means and includes all marriages solemnized performed or contracted between a male and a female, **irrespective of the religion or caste of either party** to the marriage. The definition also includes marriages performed as per law, custom, practice, or any tradition of the parties.
> 
> Service: Marriage Registration & Certificate (ID: 3)
> Department: Urban Administration and development Department

*Latency: 11.48 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ के नियमों के तहत विवाह की परिभाषा ईसाई और मुस्लिम विवाहों पर लागू होती है।
> 
> नियमों के अनुसार, 'विवाह' की परिभाषा में स्पष्ट रूप से कहा गया है कि यह 'किसी भी धर्म या जाति की परवाह किए बिना' किया गया विवाह है। इसका अर्थ है कि ईसाई, मुस्लिम, हिंदू, आर्य समाज या किसी अन्य धर्म के विवाहों को इसमें शामिल किया गया है।
> 
> यह व्यापक परिभाषा सुनिश्चित करती है कि सभी प्रकार के विवाह, चाहे वे किसी भी धर्म के हों, छत्तीसगढ़ विवाह पंजीकरण नियम, २००६ के दायरे में आते हैं।
> 
> यह जानकारी छत्तीसगढ़ विवाह पंजीकरण नियम, २००६ के अंतर्गत 'विवाह पंजीकरण एवं प्रमाण पत्र' सेवा से संबंधित है।

*Latency: 15.38 seconds*

#### 💬 Hinglish Response:
> हाँ, CG rules के तहत 'शादी' की परिभाषा में Christian और Muslim शादियों को भी शामिल किया गया है।
> 
> नियम 2(d) के अनुसार, 'शादी' का मतलब है कि यह धर्म या जाति के आधार पर नहीं होती। यह परिभाषा बहुत व्यापक है और इसमें कानून, रिवाज या किसी भी परंपरा के अनुसार की गई सभी शादियों को शामिल किया गया है। इसलिए, Christian या Muslim शादियों पर भी ये नियम लागू होते हैं।

*Latency: 12.86 seconds*

---

### Q14: What is the fee for obtaining a certified copy of the marriage certificate from the registrar?

**Hindi:** *रजिस्ट्रार से विवाह प्रमाण पत्र की प्रमाणित प्रति प्राप्त करने का शुल्क क्या है?*

**Hinglish:** *Registrar se marriage certificate ki certified copy lene ke liye kitni fee lagti hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the fee for obtaining a certified extract from the marriage register is Rs. 20.
> 
> This information is from the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, which states that certified extracts from the register can be given to applicants on payment of Rs. 20.
> 
> The service is provided by the Urban Administration and development Department.

*Latency: 15.50 seconds*

#### 🇮🇳 Hindi Response:
> विवाह प्रमाण पत्र की प्रमाणित प्रति प्राप्त करने के लिए 20 रुपये शुल्क देना होता है।
> 
> यह शुल्क छत्तीसगढ़ अनिवार्य विवाह पंजीकरण नियम, 2006 के नियम 8 के अनुसार है, जिसमें उल्लेख है कि विवाह प्रमाण पत्र की प्रमाणित प्रति प्राप्त करने के लिए 20 रुपये शुल्क देना होगा।

*Latency: 16.80 seconds*

#### 💬 Hinglish Response:
> Marriage certificate ki certified copy lene ke liye ₹30.0 fee lagti hai. Yeh fee online application ke liye ya Sewa Setu Kendra (kiosk) par apply karne ke liye same hai. Yeh service 'Marriage Registration & Certificate' hai, jo Urban Administration and development Department ke under aati hai.

*Latency: 19.74 seconds*

---

### Q15: Who is the designated Chief Registrar of Marriages for the state of Chhattisgarh?

**Hindi:** *छत्तीसगढ़ राज्य के लिए मनोनीत मुख्य विवाह रजिस्ट्रार कौन होता है?*

**Hinglish:** *CG state ke liye designated Chief Registrar of Marriages kaun hota hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 9.79 seconds*

#### 🇮🇳 Hindi Response:
> मनोनीत मुख्य विवाह रजिस्ट्रार का विशिष्ट नाम संदर्भ में उपलब्ध नहीं है।
> 
> हालाँकि, नियम 3 के अनुसार, छत्तीसगढ़ राज्य के मुख्य रजिस्ट्रार की नियुक्ति राज्य सरकार द्वारा की जाती है।

*Latency: 27.33 seconds*

#### 💬 Hinglish Response:
> CG state ke liye koi specific person nahi hota jo Chief Registrar of Marriages ho. Ye ek role hai jo State Government appoint karti hai.
> 
> Rule 3 ke according, State Government notification ke through kisi bhi officer ko Chief Registrar appoint kar sakti hai. Iske liye Urban Administration and development Department responsible hai.

*Latency: 12.66 seconds*

---

### Q16: Are details of witnesses, such as names and signatures, required in the marriage registration form?

**Hindi:** *क्या विवाह पंजीकरण फॉर्म में गवाहों के विवरण, जैसे नाम और हस्ताक्षर, आवश्यक हैं?*

**Hinglish:** *Kya marriage registration form me witnesses ke naam aur signature jaise details chahiye hote hain?*

#### 🇬🇧 English Response:
> Yes, details of witnesses are required in the marriage registration form.
> 
> The application form includes specific fields for witness information:
> *   **Witness Details of Groom Side**
> *   **Witness Details of Bride Side**
> 
> These fields are part of the form structure for the marriage registration process.

*Latency: 15.08 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, विवाह पंजीकरण फॉर्म में गवाहों के विवरण, जैसे नाम और हस्ताक्षर, आवश्यक हैं।
> 
> छत्तीसगढ़ ई-डिस्ट्रिक्ट पोटाल पर विवाह पंजीकरण के लिए आवेदन फॉर्म में "गवाहों के विवरण" (Witness Details) के लिए अलग से फील्ड दिए गए हैं, जो वर पक्ष और वधू पक्ष, दोनों के लिए अनिवार्य हैं। यह जानकारी शहरी प्रशासन और विकास विभाग, छत्तीसगढ़ के विवाह पंजीकरण एवं प्रमाण पत्र सेवा से संबंधित है।

*Latency: 13.20 seconds*

#### 💬 Hinglish Response:
> हाँ, विवाह पंजीकरण फॉर्म में गवाहों के नाम और हस्ताक्षर से संबंधित विवरण आवश्यक हैं।
> 
> फॉर्म में 'गवाहों के विवरण' (Witness Details) के लिए एक विशेष फील्ड है। इसके अतिरिक्त, दूल्हा और दुल्हन दोनों के हस्ताक्षर वाले दस्तावेज भी अनिवार्य हैं। फॉर्म में उनके पहले और दूसरे पन्ने के अलग-अलग हस्ताक्षर वाले दस्तावेज मांगे गए हैं।
> 
> सेवा: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3)
> विभाग: शहरी प्रशासन और विकास विभाग
> सेवा केंद्र: Sewa Setu Kendra
> कियोस्क शुल्क: 30.0
> ऑनलाइन शुल्क: 30.0
> समय सीमा / SLA: 15 दिन
> आवेदन कहाँ करें: Sewa Setu Kendra : ₹30.0 ऑनलाइन : ₹30.0
> आवेदन लिंक: https://sewasetu.cgstate.gov.in/home?lang=en

*Latency: 21.23 seconds*

---

## 3. Scheduled Castes & Scheduled Tribes Order 1950

### Q17: Which parts of the Scheduled Castes and Scheduled Tribes Orders 1950 apply specifically to the State of Chhattisgarh?

**Hindi:** *अनुसूचित जाति और अनुसूचित जनजाति आदेश 1950 के कौन से भाग विशेष रूप से छत्तीसगढ़ राज्य पर लागू होते हैं?*

**Hinglish:** *SC aur ST Orders 1950 ke kaun se parts khaas karke Chhattisgarh state par laagu hote hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the specific parts of the Constitution (Scheduled Castes) Order, १९५० and the Constitution (Scheduled Tribes) Order, १९५० that apply to the State of Chhattisgarh are not explicitly mentioned.
> 
> The context lists the states and regions covered by these Orders, such as Andhra Pradesh and Assam, but Chhattisgarh is not included in the list of "PART Il. Rules and Orders under the Constitution". While the context details the process for obtaining SC/ST certificates in Chhattisgarh under the Chhattisgarh Scheduled Castes, Scheduled Tribes and Other Backward Classes (Regulation of Social Status Certification) Act, २०१३, it does not specify which parts of the 1950 Orders are applicable to the state.
> 
> Information not available.

*Latency: 16.41 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।
> 
> प्रदान किए गए संदर्भ के अनुसार, 'अनुसूचित जाति और अनुसूचित जनजाति आदेश, 1950' के 'भागों' में छत्तीसगढ़ राज्य का उल्लेख नहीं है। संदर्भ में 'भाग II' के अंतर्गत आंध्र प्रदेश और असम राज्यों को सूचीबद्ध किया गया है, लेकिन छत्तीसगढ़ का उल्लेख नहीं है।
> 
> यह जानकारी 'राजस्व और आपदा प्रबंधन विभाग' के अंतर्गत 'अनुसूचित जाति/जनजाति प्रमाण पत्र' सेवा से संबंधित है।

*Latency: 18.80 seconds*

#### 💬 Hinglish Response:
> Provided context mein sirf Constitution (Scheduled Tribes) Order, १९५० ka zikr hai. Yeh order Constitution ke under aane waale rules aur orders ka hissa hai. Context mein Chhattisgarh state ke liye is order ke specific parts ke baare mein koi jaankari nahi di gayi hai. Isi tarah, context mein SC (Scheduled Castes) Order, १९५० ke baare mein bhi koi jaankari nahi hai. Isliye, diye gaye context ke aadhar par, Chhattisgarh ke liye SC aur ST Orders 1950 ke specific parts ke baare mein jaankari uplabhd nahi hai.

*Latency: 23.08 seconds*

---

### Q18: Under entry 17 of Andhra Pradesh Scheduled Tribes, which tribal group is recognized?

**Hindi:** *आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 17 के तहत किस जनजातीय समूह को मान्यता दी गई है?*

**Hinglish:** *Andhra Pradesh ST list ki entry 17 ke under kaun sa tribal group aata hai?*

#### 🇬🇧 English Response:
> प्रदत्त दस्तावेज़ के आधार पर, आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 17 के अंतर्गत मान्यता प्राप्त जनजातीय समूह कोटिया, बेंटो, ओरिया, बतिका, दुआलिया, होल्या, संनोरा और सिधपाएको हैं।
> 
> यह जानकारी छत्तीसगढ़ पोर्टल के राजस्व और आपदा प्रबंधन विभाग के अंतर्गत SC/ST प्रमाण पत्र सेवा से संबंधित है।

*Latency: 15.66 seconds*

#### 🇮🇳 Hindi Response:
> आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 17 के तहत मान्यता प्राप्त जनजातीय समूह कोन्डा कपू है।
> 
> सेवा: अनुसूचित जाति/अनुसूचित जनजाति प्रमाण पत्र (ID: 4), विभाग: राजस्व और आपदा प्रबंधन विभाग।

*Latency: 18.23 seconds*

#### 💬 Hinglish Response:
> Andhra Pradesh ST list ki entry 17 ke under jo tribal groups aate hain, woh ye hain:
> 1. Kotia
> 2. Bentho Oriya
> 3. Bartika
> 4. 3*** Dulia
> 5. Holya
> 6. 3*** Sanrona
> 7. Sidhopaiko
> 
> Service: SC/ST Certificate (ID: 4), Department: Revenue and disaster management Department.

*Latency: 22.78 seconds*

---

### Q19: Is 'Ganda' recognized as a Scheduled Caste in Chhattisgarh under Part XVIIIL of the SC Order?

**Hindi:** *क्या छत्तीसगढ़ में अनुसूचित जाति आदेश के भाग XVIIIL के तहत 'गांडा' को अनुसूचित जाति के रूप में मान्यता प्राप्त है?*

**Hinglish:** *Kya 'Ganda' caste ko CG me SC list ke Part XVIIIL me recognize kiya gaya hai?*

#### 🇬🇧 English Response:
> Yes, 'Ganda' is recognized as a Scheduled Caste in Chhattisgarh.
> 
> According to the provided context, 'Ganda, Gandi' is listed in the official schedule for Chhattisgarh under the Constitution (Scheduled Castes) Order, 1950. This is found in the section titled 'PART III. Chhattisgarh' and other related lists within the document.
> 
> Therefore, it is officially included in the list of Scheduled Castes for the state.
> 
> Service: SC/ST Certificate (ID: 4)
> Department: Revenue and disaster management Department

*Latency: 16.46 seconds*

#### 🇮🇳 Hindi Response:
> प्रदत्त संदर्भ के आधार पर, यह पुष्टि करना संभव नहीं है कि 'गांडा' को अनुसूचित जाति के रूप में मान्यता प्राप्त है या नहीं।
> 
> दस्तावेज़ अनुसूचित जाति को "छत्तीसगढ़ राज्य के लिए संविधान के अनुच्छेद 341 के अधीन निर्दिष्ट अनुसूचित जातियों" के रूप में परिभाषित करते हैं, परंतु वे उस आदेश में शामिल विशिष्ट जातियों की सूची प्रदान नहीं करते हैं।
> 
> अतः, प्रदत्त संदर्भ में यह जानकारी उपलब्ध नहीं है।
> 
> सूचना उपलब्ध नहीं है।
> सेवा: अनुसूचित जाति/जनजाति प्रमाण पत्र (आई डी: 4)
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 25.91 seconds*

#### 💬 Hinglish Response:
> Haan, 'Ganda' caste को Chhattisgarh के लिए SC list me recognize किया गया है।
> 
> Context me दिए गए document, Constitution (Scheduled Castes) Order, १९५०, के Part XVIIIL (जो Chhattisgarh के लिए है) me, entry number ४ के under 'Ganda, Gandi' listed है।
> 
> यह information Sewa Setu Chhattisgarh portal के SC/ST Certificate service से related है, जो Revenue and disaster management Department के under आती है।

*Latency: 19.04 seconds*

---

### Q20: Which entry number contains 'Bhil, Bhilala, Patelia' in the Scheduled Tribes list of Chhattisgarh?

**Hindi:** *छत्तीसगढ़ की अनुसूचित जनजाति की सूची में किस प्रविष्टि संख्या में 'भील, भिलाला, पटेलिया' शामिल हैं?*

**Hinglish:** *CG ST list me 'Bhil, Bhilala, Patelia' kis entry number par listed hain?*

#### 🇬🇧 English Response:
> Based on the provided context, there is no single entry number that contains 'Bhil, Bhilala, Patelia'.
> 
> The list is structured as follows:
> *   **Entry 17** is for 'Bhil' and explicitly excludes 'Bhilala'.
> *   **Entry 22** is for 'Patelia'.
> 
> Therefore, these tribes are listed in separate entries, and Bhilala is not included in the Bhil entry.

*Latency: 29.62 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 30.75 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 36.63 seconds*

---

### Q21: Is 'Katkari' or 'Kathodi' recognized as a Scheduled Tribe in Chhattisgarh, and under which entry number?

**Hindi:** *क्या छत्तीसगढ़ में 'काटकारी' या 'काथोड़ी' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है, और किस प्रविष्टि संख्या के तहत?*

**Hinglish:** *Kya 'Katkari' ya 'Kathodi' CG me ST recognized hai, aur iska entry number kya hai?*

#### 🇬🇧 English Response:
> Information not available.
> 
> The provided context does not contain a list of specific castes like 'Katkari' or 'Kathodi' and their corresponding entry numbers in the Schedule for Chhattisgarh.
> 
> However, the context explains that for a Social Status Certificate to be issued, the caste of the applicant must be "recognized" or "included" in the list of Scheduled Castes, Scheduled Tribes, or Other Backward Classes as per the Chhattisgarh Scheduled Castes Scheduled Tribes and Other Backward Classes ( Regulation of Social Status Certification) Act, 2013.
> 
> For such specific details, you would need to consult the official list of Scheduled Tribes and Scheduled Castes for the state of Chhattisgarh or contact the Revenue and Disaster Management Department.
> 
> Service: Revenue and Disaster Management Department
> Department: Sewa Setu Chhattisgarh Portal

*Latency: 25.93 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 159.61 seconds*

#### 💬 Hinglish Response:
> दिए गए संदर्भ के अनुसार, छत्तीसगढ़ (CG) के लिए आधिकारिक दस्तावेज़ सामग्री में 'कठोरी' और 'काठोडी' समुदायों का उल्लेख नहीं है। इसलिए, उनकी प्रवेश संख्या के बारे में जानकारी उपलब्ध नहीं है।

*Latency: 16.19 seconds*

---

### Q22: Are 'Khatik' and 'Koli' listed under the Scheduled Castes list for Chhattisgarh?

**Hindi:** *क्या छत्तीसगढ़ के लिए अनुसूचित जाति की सूची में 'खटीक' और 'कोली' शामिल हैं?*

**Hinglish:** *Kya CG ki SC list me 'Khatik' aur 'Koli' castes shamil hain?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 27.79 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ के लिए अनुसूचित जाति की सूची में 'खटीक' और 'कोली' दोनों शामिल हैं।
> 
> प्रदान किए गए संदर्भ के अनुसार, 'राजस्व और आपदा प्रबंधन विभाग' के अंतर्गत 'अनुसूचित जाति प्रमाण पत्र' सेवा के लिए उपयोगकर्ता नियमावली में इन जातियों का उल्लेख है।
> 
> *   **खटीक:** स्रोत 1 में, सूची में 'खटीक' (प्रविष्टि 35) का उल्लेख है।
> *   **कोली:** स्रोत 2 में, सूची में 'कोली' (प्रविष्टि 37) और 'खटीक' (प्रविष्टि 36) दोनों का स्पष्ट रूप से उल्लेख है।
> 
> आपके प्रश्न में 'खटीक' का उपयोग किया गया है, जो सूची में प्रयुक्त शब्द के अनुरूप है।

*Latency: 17.21 seconds*

#### 💬 Hinglish Response:
> हाँ, Chhattisgarh की SC/ST Certificate सेवा की official document content के अनुसार, 'Khatik' और 'Koli' दोनों जातियाँ शामिल हैं।
> 
> **'Khatik' के लिए:**
> Source 1, 2, 3, और 4 में "36. Khatik Jatav, Jatava, Mochi, Raidas, Rohidas, Regar," लिखा है।
> 
> **'Koli' के लिए:**
> Source 1, 2, 3, और 4 में "37. Koli, Kori Raigar Ramdasia, Asadaru, Asodi, Chamadia," लिखा है।
> 
> यह जानकारी 'SC/ST Certificate' सेवा (ID: 4) के लिए 'Revenue and disaster management Department' के अंतर्गत दी गई है।

*Latency: 20.72 seconds*

---

### Q23: What are the districts or regions mentioned for the 'Halba' tribe in the Chhattisgarh Scheduled Tribes list?

**Hindi:** *छत्तीसगढ़ अनुसूचित जनजाति की सूची में 'हलबा' जनजाति के लिए कौन से जिले या क्षेत्र बताए गए हैं?*

**Hinglish:** *CG ST list me 'Halba' tribe ke liye kaun se districts ya areas specify kiye gaye hain?*

#### 🇬🇧 English Response:
> Based on the provided context, the districts or regions mentioned for the 'Halba' tribe in the Chhattisgarh Scheduled Tribes list are:
> 
> 1.  **Bastar Division:**
>     *   Bailadila
>     *   Bijapur
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kondagaon
>     *   Kanker
>     *   Darbha
>     *   Gudumaharas
>     *   Malkangiri (Note: This is in Odisha, but the context places it within the Chhattisgarh list)
> 
> 2.  **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 3.  **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 4.  **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 5.  **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
>     *   Raipur
> 
> 6.  **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 7.  **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 8.  **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 9.  **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 10. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 11. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 12. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 13. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 14. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 15. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 16. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 17. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 18. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 19. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 20. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 21. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 22. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 23. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 24. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 25. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 26. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 27. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 28. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 29. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 30. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 31. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 32. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 33. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 34. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 35. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 36. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 37. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 38. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 39. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 40. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 41. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 42. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 43. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 44. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 45. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 46. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 47. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 48. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 49. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 50. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 51. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 52. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 53. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 54. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 55. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 56. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 57. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 58. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 59. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 60. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 61. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 62. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 63. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 64. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 65. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 66. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 67. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 68. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 69. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 70. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 71. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 72. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 73. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 74. **Bhilai Division:**
>     *   Bhilai
>     *   Durg
>     *   Balod
>     *   Dhamtari
>     *   Rajnandgaon
>     *   Kondagaon
>     *   Narayanpur
>     *   Bailadila
> 
> 75. **Bilaspur Division:**
>     *   Bilaspur
>     *   Mungeli
>     *   Janjgir-Champa
>     *   Bastar
>     *   Durg
> 
> 76. **Jashpur Division:**
>     *   Jashpur
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 77. **Surguja Division:**
>     *   Surguja
>     *   Koriya
>     *   Bastar
>     *   Dantewada
> 
> 78. **Bastar Division:**
>     *   Bastar
>     *   Dantewada
>     *   Sukma
>     *   Narayanpur
>     *   Kanker
>     *   Kondagaon
>     *   Darbha
>     *   Gudumaharas
> 
> 79. **Dantewada Division:**
>     *   Dantewada
>     *   Narayanpur
>     *   Sukma
>     *   Bijapur
>     *   Bailadila
> 
> 80. **Raipur Division:**
>     *   Raipur
>     *   Sambalpur
>     *   Bargarh
>     *   Sundergarh
>     *   Bailadila
> 
> 81. **Bhilai Division:**

*Latency: 28.91 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 29.89 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabhd nahi hai.

*Latency: 29.97 seconds*

---

### Q24: Under which entry number is 'Dewar' listed as a Scheduled Caste for Chhattisgarh?

**Hindi:** *छत्तीसगढ़ के लिए 'देवार' किस प्रविष्टि संख्या के तहत अनुसूचित जाति के रूप में सूचीबद्ध है?*

**Hinglish:** *CG SC list me 'Dewar' kis entry number par listed hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 6.16 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।
> 
> प्रदान किए गए संदर्भ में 'छत्तीसगढ़ अनुसूचित जाति/जनजाति प्रमाण पत्र' प्राप्त करने की प्रक्रिया और संबंधित अधिनियमों, जैसे कि 'छत्तीसगढ़ अनुसूचित जाति/जनजाति और अन्य पिछड़ा वर्ग (सामाजिक स्थिति प्रमाणन का विनियमन) अधिनियम, 2013' का विवरण है।
> 
> संदर्भ के अनुसार, अनुसूचित जातियों की सूची मध्य प्रदेश पुनर्गठन अधिनियम, 2000 के 'अनुसूची 3' में उपलब्ध है, जिसे छत्तीसगढ़ के लिए अपनाया गया था।
> 
> अतः, 'देवार' की विशिष्ट प्रविष्टि संख्या इस संदर्भ में नहीं दी गई है। सटीक प्रविष्टि संख्या के लिए, आधिकारिक अनुसूचित जाति सूची की जांच करनी होगी, जो यहाँ उपलब्ध नहीं है।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग, छत्तीसगढ़ द्वारा संभाली जाती है।

*Latency: 18.43 seconds*

#### 💬 Hinglish Response:
> Jaankari uplabd nahi hai.

*Latency: 19.05 seconds*

---

## 4. Social Status Act (Caste Certificate Rules)

### Q25: Under Section 10(1) of the Act, what is the minimum term of imprisonment for obtaining a false caste certificate?

**Hindi:** *अधिनियम की धारा 10(1) के तहत झूठा जाति प्रमाण पत्र प्राप्त करने के लिए न्यूनतम कारावास की अवधि क्या है?*

**Hinglish:** *Act ki section 10(1) ke under fake caste certificate lene par minimum kitne saal ki jail ho sakti hai?*

#### 🇬🇧 English Response:
> प्रदत्त संदर्भ के आधार पर, जानबूझकर गलत सामाजिक स्थिति प्रमाण पत्र (सोशल स्टेटस सर्टिफिकेट) जारी करने के लिए न्यूनतम कारावास की अवधि तीन महीने है।
> 
> अधिनियम की धारा 12 का प्रासंगिक पाठ इस प्रकार है: "कोई भी व्यक्ति या प्राधिकारी, जो जानबूझकर गलत सामाजिक स्थिति प्रमाण पत्र जारी करता है... उसे कम से कम तीन महीने की अवधि के लिए कठोर कारावास, जिसकी अवधि दो वर्ष तक बढ़ सकती है, और साथ ही जुर्माना, जो कम से कम दो हजार रुपये और जिसकी राशि बीस हजार रुपये तक हो सकती है, से दंडित किया जाएगा।"
> 
> सेवा: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र (ID: 5)
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 21.83 seconds*

#### 🇮🇳 Hindi Response:
> अधिनियम की धारा 10(1) के अनुसार, झूठा जाति प्रमाण पत्र प्राप्त करने पर न्यूनतम तीन माह की कठोर कारावास की सजा का प्रावधान है।
> 
> यह सेवा राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत आती है।

*Latency: 14.43 seconds*

#### 💬 Hinglish Response:
> Act ki section 10(1) ke under, agar koi fake caste certificate banwata hai ya use karta hai, toh use **kam se kam 3 mahine** ki jail ho sakti hai. Iske saath hi, 2 saal tak ki jail aur 20,000 Rs. tak ka fine bhi ho sakta hai. Ye jaankari Chhattisgarh ke Revenue and Disaster Management Department se related hai.

*Latency: 69.76 seconds*

---

### Q26: Are offenses related to fake caste certificates under Section 10 cognizable and non-bailable?

**Hindi:** *क्या धारा 10 के तहत नकली जाति प्रमाण पत्र से संबंधित अपराध संज्ञेय और गैर-जमानतीय हैं?*

**Hinglish:** *Kya Section 10 ke under fake caste certificate se related cases cognizable aur non-bailable hote hain?*

#### 🇬🇧 English Response:
> हाँ, प्रदान किए गए संदर्भ के अनुसार, जाली जाति प्रमाण पत्रों से संबंधित अपराधों को संज्ञेय (cognizable) और गैर-जमानती (non-bailable) माना जाता है।
> 
> पाठ में स्पष्ट रूप से उल्लेख किया गया है कि "इस अनुभाग के अंतर्गत दंडनीय अपराध संज्ञेय, गैर-जमानती होंगे और इनका विचारण संक्षेप में (summarily) किया जा सकता है।"
> 
> यह जानकारी अनुसूचित जाति/जनजाति प्रमाण पत्र (आई डी: 4) के लिए उपयोगकर्ता नियमावली (user manual) से ली गई है, जो राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत आती है।
> 
> सेवा: अनुसूचित जाति/जनजाति प्रमाण पत्र, विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 18.84 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, दी गई जानकारी के अनुसार, धारा 10 के तहत जाति प्रमाण पत्र से संबंधित अपराध संज्ञेय और गैर-जमानतीय हैं।
> 
> संदर्भ में उल्लेख है कि "दण्ड प्रक्रिया संहिता, १९७३ में अंतर्विष्ट किसी बात के होते हुए भी, इस अधिनियम की धारा १० के अधीन दण्डनीय अपराध संज्ञेय, अजमानतीय होंगे तथा उनका संक्षिप्त विचारण किया जा सकेगा।"
> 
> इस धारा के तहत अपराध के लिए कठोर कारावास, जिसकी अवधि तीन माह से कम न हो, किंतु जो दो वर्ष तक का हो सकता है, और जुर्माना, जो दो हजार रुपये से कम न हो, और जो बीस हजार रुपये तक का हो सकता है, से दंडित किया जाएगा।
> 
> सेवा विभाग, राजस्व एवं आपदा प्रबंधन विभाग, छत्तीसगढ़।

*Latency: 35.13 seconds*

#### 💬 Hinglish Response:
> Haan, provided context ke according, Chhattisgarh Act ke Section 10 ke under, jo cases fake ya false Social Status Certificate se related hote hain, unhe cognizable aur non-bailable maana jaata hai. Context mein likha hai ki "offences punishable under this Act shall be cognizable, non bailable".

*Latency: 13.30 seconds*

---

### Q27: What happens to the election of a candidate to a local authority if their caste certificate is cancelled?

**Hindi:** *यदि किसी उम्मीदवार का जाति प्रमाण पत्र रद्द कर दिया जाता है तो स्थानीय प्राधिकरण में उसके चुनाव का क्या होता है?*

**Hinglish:** *Agar kisi candidate ka caste certificate cancel ho jaye to local body me uske election ka kya hota hai?*

#### 🇬🇧 English Response:
> यदि किसी उम्मीदवार का जाति प्रमाण पत्र रद्द कर दिया जाता है, तो वे स्थानीय प्राधिकरण के सदस्य बनने के लिए अयोग्य हो जाते हैं। यह अयोग्यता प्रमाण पत्र रद्द होने की तिथि से प्रभावी हो जाती है, और उनके द्वारा धारित आरक्षित सीट को तुरंत रिक्त माना जाता है। यह जानकारी अनुसूचित जाति/जनजाति प्रमाण पत्र सेवा के आधिकारिक दस्तावेज़ सामग्री में विस्तृत है, जो राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत आती है।

*Latency: 12.83 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 16.39 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}

*Latency: 347.93 seconds*

---

### Q28: What is the time limit for an applicant to file an appeal against the rejection of a caste certificate?

**Hindi:** *जाति प्रमाण पत्र की अस्वीकृति के खिलाफ अपील दायर करने की समय सीमा क्या है?*

**Hinglish:** *Caste certificate reject hone par appeal file karne ki time limit kya hoti hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 33.01 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 15.89 seconds*

#### 💬 Hinglish Response:
> Agar caste certificate reject ho jaata hai, to appeal file karne ke liye 22 din ki time limit hoti hai. Yeh time limit SC/ST certificate aur OBC certificate dono ke liye apply hoti hai. Application submit karne ke baad yeh time limit shuru hoti hai.

*Latency: 17.28 seconds*

---

### Q29: Who bears the burden of proof to establish caste status under the Social Status Act?

**Hindi:** *सामाजिक प्रास्थिति अधिनियम के तहत जाति की स्थिति स्थापित करने के लिए सबूत का भार कौन वहन करता है?*

**Hinglish:** *Social Status Act ke under caste status prove karne ke liye burden of proof kis par hota hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the burden of proof to establish caste status under the Social Status Act lies with the applicant.
> 
> The document explicitly states that when an application is made for a Social Status Certificate, or in any related inquiry or trial, "the burden of proving the social status... shall be on such applicant." This means the person applying for the certificate is responsible for proving their social status.
> 
> This information pertains to the services of the Revenue & Disaster Management Department of Chhattisgarh.

*Latency: 14.23 seconds*

#### 🇮🇳 Hindi Response:
> सामाजिक प्रास्थिति अधिनियम के तहत, जाति की स्थिति स्थापित करने का भार अधिनियम के तहत गठित अधिकारियों पर होता है।
> 
> ये अधिकारी अधिनियम के तहत दी गई शक्तियों का प्रयोग कर सकते हैं, जैसे कि सिविल कोर्ट की शक्तियाँ। इसका अर्थ है कि जब किसी प्रमाण पत्र की वैधता पर प्रश्न उठता है, तो इन अधिकारियों को ही प्रमाण पत्र की सत्यता की जांच करनी होती है। यह प्रावधान अधिनियम के 'मिसलेनियस' (Miscellaneous) खंड में दिया गया है।

*Latency: 15.67 seconds*

#### 💬 Hinglish Response:
> Social Status Act के under, caste status prove करने का burden of proof applicant पर ही होता है। जब भी कोई Social Status Certificate के लिए apply करता है, तो उन्हें अपनी social status prove करनी पड़ती है।
> 
> यह Chhattisgarh Scheduled Castes Scheduled Tribes and Other Backward Classes (Regulation of Social Status Certification) Act, 2013 के Section 14 में clearly mention है। इसलिए, applicant को ही अपनी caste status prove करनी होती है।
> 
> Service: Scheduled Caste/Tribe Certificate (ID: 4), Department: Revenue & Disaster Management Department.

*Latency: 16.18 seconds*

---

### Q30: Under what section of the 2013 Act can a duplicate social status certificate be issued?

**Hindi:** *2013 के अधिनियम की किस धारा के तहत डुप्लीकेट सामाजिक प्रास्थिति प्रमाण पत्र जारी किया जा सकता है?*

**Hinglish:** *2013 Act ki kis section ke under duplicate social status certificate issue kiya ja sakta hai?*

#### 🇬🇧 English Response:
> प्रदत्त संदर्भ के आधार पर, एक डुप्लिकेट सामाजिक स्थिति प्रमाण पत्र (सोशल स्टेटस सर्टिफिकेट) केवल तभी जारी किया जा सकता है जब आवेदक मूल प्रमाण पत्र के खोने की घोषणा करता है।

*Latency: 14.56 seconds*

#### 🇮🇳 Hindi Response:
> Jaankari uplabhd nahi hai.

*Latency: 44.48 seconds*

#### 💬 Hinglish Response:
> 2013 Act के Section 4 के अंडर डुप्लिकेट सोशल स्टेटस सर्टिफिकेट जारी किया जा सकता है।
> 
> Context के अनुसार, कॉम्पिटेंट अथॉरिटी डुप्लिकेट कॉपी जारी कर सकता है, लेकिन सिर्फ तब जब आवेदक original certificate के loss का declaration दे।
> 
> यह सेवा छत्तीसगढ़ रेवेन्यू एवं डिजास्टर मैनेजमेंट डिपार्टमेंट से संबंधित है।

*Latency: 14.40 seconds*

---

### Q31: Can a government servant be prosecuted for issuing a false certificate without prior government sanction?

**Hindi:** *क्या पूर्व सरकारी मंजूरी के बिना झूठा प्रमाण पत्र जारी करने के लिए किसी सरकारी कर्मचारी के खिलाफ मुकदमा चलाया जा सकता है?*

**Hinglish:** *Kya sarkari sanction ke bina kisi govt servant par fake certificate issue karne ka case chalaya ja sakta hai?*

#### 🇬🇧 English Response:
> Based on the provided context, a government servant can be prosecuted for issuing a false Social Status Certificate without prior government sanction.
> 
> According to the context, under the penalties section, any person or authority performing the functions of a Competent Authority who intentionally issues a false Social Status Certificate shall be punished with rigorous imprisonment for a term not less than three months but which may extend to two years and with a fine not less than two thousand rupees and which may extend to twenty thousand rupees.
> 
> The context also states that no court shall take cognizance of an offence punishable under this section except with the previous sanction of the Government. This means that for the prosecution to proceed, prior government sanction is required.
> 
> Therefore, if a government servant issues a false certificate without this prior sanction, the prosecution would not be legally valid.
> 
> Information not available.

*Latency: 5.35 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, प्रदान किए गए संदर्भ के अनुसार, एक सरकारी कर्मचारी को झूठा प्रमाण पत्र जारी करने के लिए मुकदमा चलाया जा सकता है।
> 
> संदर्भ के 'अपराध एवं शास्ति' (अपराध एवं शास्ति) अनुभाग में उल्लेख है कि यदि कोई व्यक्ति या प्राधिकारी, जो सक्षम प्राधिकारी के रूप में कार्य कर रहा है, जानबूझकर (fraudulently) झूठा सामाजिक प्रास्थिति प्रमाण पत्र जारी करता है, तो उसे दंडित किया जा सकता है। इसके लिए उन्हें कठोर कारावास और जुर्माने की सजा हो सकती है।
> 
> यह सेवा राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत आती है, जो अनुसूचित जाति/जनजाति प्रमाण पत्र और अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र जैसी सेवाओं को संभालता है।

*Latency: 19.26 seconds*

#### 💬 Hinglish Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 62.71 seconds*

---

### Q32: What is the consequence on educational degrees if the social status certificate is cancelled under Section 8?

**Hindi:** *यदि धारा 8 के तहत सामाजिक प्रास्थिति प्रमाण पत्र रद्द कर दिया जाता है तो शैक्षणिक डिग्री पर क्या परिणाम होता है?*

**Hinglish:** *Agar Section 8 ke under social status certificate cancel ho jaye to educational degrees ka kya hota hai?*

#### 🇬🇧 English Response:
> Based on the provided context, if a Social Status Certificate is cancelled under Section 8, any educational degree, diploma, or certificate obtained using that false certificate is considered to have been cancelled and is deemed to have never been awarded.
> 
> This information is from the user manual for the Scheduled Caste/Scheduled Tribe Certificate service, managed by the Revenue & Disaster Management Department of Chhattisgarh.

*Latency: 10.93 seconds*

#### 🇮🇳 Hindi Response:
> यदि धारा 8 के तहत सामाजिक प्रास्थिति प्रमाण पत्र रद्द कर दिया जाता है, तो शैक्षणिक डिग्री पर निम्नलिखित परिणाम होते हैं:
> 
> ऐसी स्थिति में प्राप्त की गई कोई भी डिग्री, डिप्लोमा, प्रमाणपत्र या अन्य शैक्षणिक योग्यता भी रद्द मानी जाएगी और इसे कभी भी सम्मानित नहीं किया जाएगा।
> 
> यह सेवा राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की जाती है।

*Latency: 12.32 seconds*

#### 💬 Hinglish Response:
> Agar Section 8 ke under social status certificate cancel ho jaata hai, to educational degrees ka kya hota hai, yeh jaankari yahan hai.
> 
> Section 9(4) ke according, agar kisi ne cancelled social status certificate ke basis par admission liya hai, to uski degree, diploma, ya koi bhi educational qualification cancel maani jaati hai aur kabhi award hi nahi hui hoti.

*Latency: 20.25 seconds*

---

## 5. Other Backward Classes (OBC) Certificate

### Q33: Which department is responsible for issuing the OBC Certificate in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र जारी करने के लिए कौन सा विभाग जिम्मेदार है?*

**Hinglish:** *CG me OBC Certificate issue karne ke liye kaun sa department responsible hai?*

#### 🇬🇧 English Response:
> The Revenue and disaster management Department is responsible for issuing the OBC Certificate in Chhattisgarh.
> 
> The service is the Other Backward Class (OBC) Certificate, and the responsible department is the Revenue and disaster management Department.

*Latency: 14.87 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र जारी करने के लिए 'राजस्व एवं आपदा प्रबंधन विभाग' जिम्मेदार है।
> 
> यह जानकारी 'अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र' सेवा के आधिकारिक यूजर मैनुअल में दी गई है।
> 
> सेवा का नाम: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र, विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 12.39 seconds*

#### 💬 Hinglish Response:
> CG me OBC Certificate (अन्य पिछड़ा वर्ग प्रमाण-पत्र) issue karne ke liye **राजस्व एवं आपदा प्रबंधन विभाग** responsible hai. Ye department iss service ke liye official authority hai.

*Latency: 10.39 seconds*

---

### Q34: What is the processing time limit (SLA) for the OBC Certificate in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए प्रसंस्करण समय सीमा (SLA) क्या है?*

**Hinglish:** *CG me OBC Certificate banne ka SLA processing time kitne dino ka hota hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the processing time limit (SLA) for the OBC Certificate in Chhattisgarh is 30 working days, as specified by the Revenue and disaster management Department.
> Service: OBC Certificate, Department: Revenue and disaster management Department.

*Latency: 10.13 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए प्रसंस्करण समय सीमा (SLA) के संबंध में दी गई जानकारी के अनुसार, सक्षम प्राधिकारी आवेदन की तिथि से पन्द्रह (15) दिन के भीतर अस्थायी प्रमाण पत्र जारी कर सकता है।
> 
> अस्थायी प्रमाण पत्र छह (6) माह की अवधि के लिए वैध होगा।
> 
> सेवा का नाम: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र, विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 16.25 seconds*

#### 💬 Hinglish Response:
> Sewasethu Chhattisgarh portal ke according, Chhattisgarh mein OBC Certificate banne ka SLA processing time 22 din ka hota hai. Ye service Revenue aur disaster management Department dwara provide ki jaati hai.

*Latency: 12.59 seconds*

---

### Q35: What are the required documents to apply for an OBC Certificate on the Sewa Setu portal?

**Hindi:** *सेवा सेतु पोर्टल पर अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए आवेदन करने के लिए आवश्यक दस्तावेज क्या हैं?*

**Hinglish:** *Sewa Setu portal par OBC Certificate apply karne ke liye kaun se documents chahiye?*

#### 🇬🇧 English Response:
> To apply for an OBC Certificate on the Sewa Setu portal, you need to provide the following required documents:
> 
> **SNo 1: Residential Proof (Mandatory: No)**
> - Supporting Document 1: Certificate From Ward Member, Local Mla/Mp
> - Supporting Document 2: Land And House Document
> - Supporting Document 3: Ration Card
> - Supporting Document 4: Electricity Bill
> - Supporting Document 5: Domicile Certificate
> - Supporting Document 6: Birth Certificate
> - Supporting Document 7: Birth Information Form
> - Supporting Document 8: Service Certificate / Identity Card Of Father / Guardian
> - Supporting Document 9: Order Of Involuntary Migration
> 
> **SNo 2: Affidavit (Mandatory: Yes)**
> - Supporting Document 1: Affidavit
> 
> **SNo 3: Income Proof (Mandatory: Yes)**
> - Supporting Document 1: Certificate From Patwari/Sarpanch/Parshad
> - Supporting Document 2: Income Certificate Employer/Form 16
> - Supporting Document 3: Ration Card
> - Supporting Document 4: Income From Land/House
> - Supporting Document 5: Other Documents
> - Supporting Document 6: Application Form
> 
> **SNo 4: Obc Proof (Mandatory: Yes)**
> - Supporting Document 1: Educational Certificate
> - Supporting Document 2: Transfer Certificate Of Primary School Education
> - Supporting Document 3: Obc Certificate Of Father
> - Supporting Document 4: Obc Certificate From Sarpanch / Parshad
> - Supporting Document 5: Father/Guardians Service Certificate/Identity Card
> - Supporting Document 6: Misal
> - Supporting Document 7: Adhikar Abhilekh
> - Supporting Document 8: Jamabandi
> - Supporting Document 9: Census Register Of 1931
> - Supporting Document 10: Citizen Register Of 1949
> - Supporting Document 11: Dakhil / Kharij Panji
> - Supporting Document 12: Disability / Unavailability Proof
> 
> **SNo 5: Vanshavali (Mandatory: No)**
> - Supporting Document 1: Vanshavali
> - Supporting Document 2: Vanshavali 1
> - Supporting Document 3: Vanshavali 2
> - Supporting Document 4: Vanshavali 3
> - Supporting Document 5: Vanshavali 4
> 
> **SNo 6: Gram Sabha Proposal (Resident Of Rural Areas People) (Mandatory: No)**
> - Supporting Document 1: Gram Sabha Proposal (Resident Of Rural Areas People)
> 
> **SNo 7: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof (Mandatory: No)**
> - Supporting Document 1: Madhya Pradesh Reorganization Act 2000 (No. 26 Of 2000 Under Section 67 C.G. State Cadre Allocation) Proof
> 
> For more details, you can visit the Sewa Setu portal at https://sewasetu.cgstate.gov.in/home?lang=en. The application process is handled through the Sewa Setu Kendra or online.
> 
> Information not available.

*Latency: 9.05 seconds*

#### 🇮🇳 Hindi Response:
> नमस्ते! Sewa Setu पोर्टल पर अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए आवेदन करने के लिए, आपको निम्नलिखित दस्तावेजों की आवश्यकता होगी:
> 
> 1.  **आवासीय प्रमाण (SNo 1):**
>     *   वार्ड सदस्य, स्थानीय विधायक / सांसद से प्रमाण पत्र
>     *   घर या भूमि का दस्तावेज़
>     *   राशन कार्ड
>     *   बिजली का बिल
>     *   मूल निवासी प्रमाण पत्र
>     *   जन्म प्रमाण पत्र
>     *   जन्म सूचना प्रपत्र
>     *   पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र
>     *   अनैच्छिक प्रवजन का आदेश
> 
> 2.  **शपथ पत्र (SNo 2):**
>     *   शपथ पत्र (Mandatory)
> 
> 3.  **आय प्रमाण (SNo 3):**
>     *   पटवारी/सरपंच/पार्षद से प्रमाण पत्र
>     *   नियोक्ता का आय प्रमाण पत्र/फार्म 16
>     *   राशन कार्ड
>     *   भूमि/घर से आय
>     *   अन्य
>     *   आवेदन प्रपत्र
> 
> 4.  **अन्य पिछड़ा वर्ग का प्रमाण (SNo 4):**
>     *   शैक्षणिक प्रमाण पत्र
>     *   प्राथमिक स्कूल शिक्षा के प्रमाण पत्र के लिए स्थानांतरण
>     *   पिता का अ.पि.व. प्रमाण पत्र
>     *   सरपंच / पार्षद से ओबीसी प्रमाणपत्र
>     *   पिता / अभिभावक की सेवा प्रमाण पत्र / पहचान पत्र
>     *   मिसल
>     *   अधिकार अभिलेख
>     *   जमाबंदी
>     *   १९३१ का जनगणना पंजी
>     *   १९४९ का नागरिक पंजी
>     *   दाखिल / ख़ारिज पंजी
>     *   असमर्थता / अनुपलब्धता का प्रमाण
> 
> 5.  **वंशावली (SNo 5):**
>     *   वंशावली (Mandatory नहीं)
> 
> 6.  **ग्राम सभा प्रस्ताव (SNo 6):**
>     *   ग्राम सभा प्रस्ताव (ग्रामीण क्षेत्र के निवासी के लिए) (Mandatory नहीं)
> 
> 7.  **मध्य प्रदेश पुनर्गठन अधिनियम 2000 (SNo 7):**
>     *   मध्य प्रदेश पुनर्गठन अधिनियम 2000 का प्रमाण (Mandatory नहीं)
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग की है।

*Latency: 22.60 seconds*

#### 💬 Hinglish Response:
> Sewa Setu portal par OBC Certificate apply karne ke liye aapko ye documents submit karne padenge:
> 
> 1.  **Residential Proof (Mandatory: No)**
>     *   Ward Member, Local Mla/Mp se Certificate
>     *   Land aur House ka Document
>     *   Ration Card
>     *   Electricity Bill
>     *   Domicile Certificate
>     *   Birth Certificate
>     *   Birth Information Form
>     *   Father/Guardian ka Service Certificate/Identity Card
>     *   Order of Involuntary Migration
> 
> 2.  **Affidavit (Mandatory: Yes)**
>     *   Affidavit
> 
> 3.  **Income Proof (Mandatory: Yes)**
>     *   Patwari/Sarpanch/Parshad se Certificate
>     *   Income Certificate ya Form 16
>     *   Ration Card
>     *   Land/House se Income ka proof
>     *   Other Documents
>     *   Application Form
> 
> 4.  **OBC Proof (Mandatory: Yes)**
>     *   Educational Certificate
>     *   Primary School ka Transfer Certificate
>     *   Father ka OBC Certificate
>     *   Sarpanch/Parshad se OBC Certificate
>     *   Father/Guardian ka Service Certificate/Identity Card
>     *   Misal
>     *   Adhikar Abhilekh
>     *   Jamabandi
>     *   1931 ka Census Register
>     *   1949 ka Citizen Register
>     *   Dakhil/Kharij Panji
>     *   Disability/Unavailability Proof
> 
> Ye documents optional hain, aap chahein toh submit kar sakte hain:
> *   Vanshavali (Mandatory: No)
> *   Gram Sabha Proposal (Mandatory: No)
> *   Madhya Pradesh Reorganization Act 2000 Proof (Mandatory: No)
> 
> Ye information 'OBC Certificate' service ke liye hai, jo Chhattisgarh ke 'Revenue and disaster management Department' ke under aati hai.

*Latency: 27.48 seconds*

---

### Q36: What is the application fee for an OBC Certificate online versus at a kiosk?

**Hindi:** *ऑनलाइन बनाम कियोस्क पर अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए आवेदन शुल्क क्या है?*

**Hinglish:** *OBC Certificate apply karne ki online fees aur kiosk fees kitni hai?*

#### 🇬🇧 English Response:
> For the OBC Certificate, the application fee is the same whether you apply online or at a kiosk. The fee for both online and kiosk applications is ₹30.0.
> 
> This is for the OBC Certificate (ID: 5) under the Revenue and disaster management Department.

*Latency: 16.91 seconds*

#### 🇮🇳 Hindi Response:
> कियोस्क (सेव सेटू केंद्र) और ऑनलाइन दोनों माध्यमों में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए आवेदन शुल्क 30 रुपये है।
> 
> सेवा का नाम: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र, विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 26.84 seconds*

#### 💬 Hinglish Response:
> OBC Certificate apply karne ke liye online fee aur kiosk fee dono ₹30.0 hain. Yeh fees Revenue aur disaster management Department ki taraf se hai. Aap Sewa Setu Kendra (kiosk) ya online portal se apply kar sakte hain.

*Latency: 11.77 seconds*

---

### Q37: Are income documents of parents required to prove the non-creamy layer status for OBC?

**Hindi:** *क्या ओबीसी के लिए गैर-क्रीमी लेयर स्थिति साबित करने के लिए माता-पिता के आय दस्तावेजों की आवश्यकता होती है?*

**Hinglish:** *Kya OBC non-creamy layer status prove karne ke liye parents ke income proof ki zaroori hoti hai?*

#### 🇬🇧 English Response:
> Yes, income documents of parents are required to prove the non-creamy layer status for an OBC certificate.
> 
> Based on the provided context, an "Income Proof" is a mandatory document for the OBC certificate application. Specifically, the following documents are required:
> 
> *   **Income Certificate Employer/Form 16** (Source 4)
> *   A document verifying the post and income of the applicant's parents if they are government employees (Source 3)
> 
> These documents are necessary to determine if the family's income falls below the threshold for the non-creamy layer.
> 
> Service: OBC Certificate
> Department: Revenue and disaster management Department
> Sewa Setu Chhattisgarh portal.

*Latency: 12.20 seconds*

#### 🇮🇳 Hindi Response:
> Haan, OBC certificate ke liye 'Income Proof' section mandatory hai. Iske liye ye supporting documents submit karne pad sakte hain:
> 
> *   Certificate From Patwari/Sarpanch/Parshad
> *   Income Certificate Employer/Form 16
> *   Ration Card
> *   Income From Land/House
> *   Other supporting documents
> 
> Ye documents applicant ki income prove karne ke liye zaroori hain.

*Latency: 17.01 seconds*

#### 💬 Hinglish Response:
> Haan, OBC non-creamy layer status prove karne ke liye income proof zaroori hai.
> 
> Service: OBC Certificate (ID: 5) ke liye, Income Proof (Mandatory: Yes) ki zaroorat hoti hai. Iske liye aap ye supporting documents de sakte hain:
> - Certificate From Patwari/Sarpanch/Parshad
> - Income Certificate Employer/Form 16
> - Ration Card
> - Income From Land/House
> - Application Form
> 
> Service: OBC Certificate, Department: Revenue and disaster management Department.

*Latency: 15.25 seconds*

---

### Q38: Who is the competent authority to issue the OBC Certificate in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र जारी करने के लिए सक्षम प्राधिकारी कौन है?*

**Hinglish:** *CG me OBC Certificate issue karne ke liye competent authority kaun hai?*

#### 🇬🇧 English Response:
> Based on the provided context, the **Competent Authority** to issue the OBC Certificate in Chhattisgarh is the officer or authority designated by the State Government through an official notification in the Gazette.
> 
> The certificate is signed by the **Certifying Officer** from the Office of the Competent Authority. This service is provided by the **Revenue and Disaster Management Department**.

*Latency: 21.12 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 16.99 seconds*

#### 💬 Hinglish Response:
> छत्तीसगढ़ में अन्य पिछड़ा वर्ग (OBC) प्रमाण-पत्र जारी करने के लिए सक्षम अधिकारी अनुविभागीय अधिकारी (राजस्व) है।
> 
> यह जानकारी राजस्व और आपदा प्रबंधन विभाग से संबंधित है।

*Latency: 24.49 seconds*

---

### Q39: Is an affidavit regarding the creamy layer status mandatory for the OBC application?

**Hindi:** *क्या ओबीसी आवेदन के लिए क्रीमी लेयर स्थिति के संबंध में शपथ पत्र अनिवार्य है?*

**Hinglish:** *Kya OBC application ke liye creamy layer status se related affidavit mandatory hai?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"HTTPSConnectionPool(host='api.sarvam.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NameResolutionError(\"HTTPSConnection(host='api.sarvam.ai', port=443): Failed to resolve 'api.sarvam.ai' ([Errno 11001] getaddrinfo failed)\"))"}

*Latency: 354.73 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, दिए गए संदर्भ के अनुसार, ओबीसी आवेदन के लिए शपथ पत्र अनिवार्य है।
> 
> स्रोत 2 में 'आवश्यक दस्तावेज' के अंतर्गत 'शपथ पत्र' को 'अनिवार्य: हाँ' के रूप में सूचीबद्ध किया गया है। यह शपथ पत्र आवेदक द्वारा अपनी सामाजिक स्थिति के संबंध में दिया गया एक औपचारिक घोषणा पत्र है, जिसमें क्रीमी लेयर की स्थिति भी शामिल होती है।
> 
> यह आवेदन प्रक्रिया का एक अनिवार्य हिस्सा है।
> 
> सेवा: अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 20.07 seconds*

#### 💬 Hinglish Response:
> Haan, OBC application ke liye affidavit zaroori hai.
> 
> Provided context ke according, 'REQUIRED DOCUMENTS' section mein SNo 2 ke under 'Affidavit (Mandatory: Yes)' mention hai. Yeh affidavit general declaration ke liye hota hai, jisme applicant confirm karta hai ki application mein di gayi information sahi hai aur rules ke according submit ki gayi hai.
> 
> Context mein yeh explicitly nahi likha hai ki affidavit specifically 'creamy layer status' ke baare mein hona chahiye. Yeh ek general affidavit hai jo application ki truthfulness declare karta hai. OBC certificate ke liye apply karne ka matlab hi yeh hai ki applicant non-creamy layer se belong karta hai, aur affidavit is application ko support karne ke liye ek supporting document hai.
> 
> Service: OBC Certificate (ID: 5)
> Department: Revenue and disaster management Department
> Where to Apply: Sewa Setu Kendra : ₹30.0 Online : ₹30.0
> How to Apply Link: https://sewasetu.cgstate.gov.in/home?lang=en

*Latency: 16.19 seconds*

---

### Q40: What is the first level of appeal if an OBC Certificate application is rejected by the Tehsildar?

**Hindi:** *यदि तहसीलदार द्वारा अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र आवेदन अस्वीकार कर दिया जाता है तो अपील का पहला स्तर क्या है?*

**Hinglish:** *Agar Tehsildar OBC Certificate reject kar de to first level of appeal kya hota hai?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 12.54 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 15.22 seconds*

#### 💬 Hinglish Response:
> Agar Tehsildar OBC Certificate reject kar de to first level of appeal ka matlab hai ki aap Collector ke paas ja sakte hain. Provided ki context mein Collector ko appellate authority bataya gaya hai. Tehsildar ke decision ke baad, agar aapko lagta hai ki yeh galat hai, to aap appeal kar sakte hain. Iske liye Collector hi final authority hain.

*Latency: 25.50 seconds*

---

## 6. Ordinary Gazette Notification for Name Change

### Q41: What is the required value of the non-judicial stamp paper for the name change affidavit?

**Hindi:** *नाम परिवर्तन हलफनामे के लिए आवश्यक गैर-न्यायिक स्टांप पेपर का आवश्यक मूल्य क्या है?*

**Hinglish:** *Name change ke affidavit ke liye kitne rupaye ka non-judicial stamp paper lagta hai?*

#### 🇬🇧 English Response:
> The required value of the non-judicial stamp paper for the name change affidavit is ₹ 50. This is for the 'Ordinary Gazette Notification for Name Change' service, provided by the Government Printing and Stationery Department.

*Latency: 21.83 seconds*

#### 🇮🇳 Hindi Response:
> सेवा सेतु पोर्टल के संदर्भ के अनुसार, नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना हेतु आवश्यक गैर-न्यायिक स्टांप पेपर का मूल्य 50 रुपये है।
> 
> आपको इस स्टांप पेपर पर प्रारूप-III में एक नोटरीकृत शपथ पत्र की आवश्यकता होगी।
> 
> सेवा: नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना (आईडी: 201)
> विभाग: मुद्रण एवं लेखन सामग्री विभाग, छत्तीसगढ़ राज्य।

*Latency: 14.64 seconds*

#### 💬 Hinglish Response:
> Name change affidavit के लिए non-judicial stamp paper का खर्च ₹50 होता है। यह stamp paper 3 महीने से पुराना नहीं होना चाहिए। यह affidavit Form-III में होना चाहिए। यह service Government Printing and Stationery Department द्वारा दी जाती है।

*Latency: 18.23 seconds*

---

### Q42: How many witnesses must sign the deed form for a name change in Form-II?

**Hindi:** *फॉर्म-II में नाम परिवर्तन के विलेख (deed) फॉर्म पर कितने गवाहों को हस्ताक्षर करने होंगे?*

**Hinglish:** *Form-II me name change deed form par kitne witnesses ke sign chahiye hote hain?*

#### 🇬🇧 English Response:
> Based on the provided context, for the Ordinary Gazette Notification for Name Change (ID: 201), you must provide the original copy of the deed form in Form-II with the names, signatures, and addresses of 02 witnesses.
> 
> **Information not available.**

*Latency: 4.73 seconds*

#### 🇮🇳 Hindi Response:
> Form-II में नाम परिवर्तन के विलेख पर 2 गवाहों के हस्ताक्षर करने होंगे। विलेख में इन 2 गवाहों के नाम, हस्ताक्षर और पते शामिल होने चाहिए।
> 
> यह जानकारी सेवा 'नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना' से संबंधित है, जो 'शासकीय मुद्रण एवं लेखन सामग्री विभाग' द्वारा प्रदान की जाती है।

*Latency: 23.91 seconds*

#### 💬 Hinglish Response:
> Form-II me name change deed form par 2 witnesses ke sign zaroori hain.
> 
> Yeh information 'Ordinary Gazette Notification for Name Change' service se related hai, jo Government Printing and Stationery Department dwara provide ki jaati hai. Form-Ii (deed form) mein 2 witnesses ke naam, sign aur address include karna mandatory hai.

*Latency: 14.19 seconds*

---

### Q43: What is the SBI challan fee amount required for name change publication?

**Hindi:** *नाम परिवर्तन प्रकाशन के लिए आवश्यक एसबीआई चालान शुल्क राशि क्या है?*

**Hinglish:** *Name change publication ke liye kitne rupaye ka SBI challan fees dena hota hai?*

#### 🇬🇧 English Response:
> The SBI challan fee amount required for name change publication is ₹430. This is specified in the required documents for the Ordinary Gazette Notification for Name Change service.
> 
> Information not available.

*Latency: 5.36 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन प्रकाशन के लिए आवश्यक एसबीआई चालान शुल्क 430 रुपये है।
> 
> यह शुल्क किसी भी स्टेट बैंक ऑफ इंडिया की शाखा से 430 रुपये के चालान के रूप में जमा करना अनिवार्य है। यह शुल्क 'सरकारी मुद्रण एवं लेखन सामग्री विभाग' के अंतर्गत 'नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना' सेवा के लिए है।

*Latency: 12.78 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 502"}

*Latency: 6.31 seconds*

---

### Q44: Is the original newspaper copy of the name change notice mandatory to submit?

**Hindi:** *क्या नाम परिवर्तन नोटिस की मूल समाचार पत्र प्रति जमा करना अनिवार्य है?*

**Hinglish:** *Kya name change notice ki original newspaper copy submit karna mandatory hai?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"HTTPSConnectionPool(host='api.sarvam.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NameResolutionError(\"HTTPSConnection(host='api.sarvam.ai', port=443): Failed to resolve 'api.sarvam.ai' ([Errno 11001] getaddrinfo failed)\"))"}

*Latency: 110.80 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"HTTPSConnectionPool(host='api.sarvam.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NameResolutionError(\"HTTPSConnection(host='api.sarvam.ai', port=443): Failed to resolve 'api.sarvam.ai' ([Errno 11001] getaddrinfo failed)\"))"}

*Latency: 2.22 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"HTTPSConnectionPool(host='api.sarvam.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NameResolutionError(\"HTTPSConnection(host='api.sarvam.ai', port=443): Failed to resolve 'api.sarvam.ai' ([Errno 11001] getaddrinfo failed)\"))"}

*Latency: 1050.56 seconds*

---

### Q45: What is the age limit or validation period for the newspaper notice from the date of application?

**Hindi:** *आवेदन की तिथि से समाचार पत्र के नोटिस के लिए आयु सीमा या सत्यापन अवधि क्या है?*

**Hinglish:** *Newspaper me notice aane ke baad kitne mahine ke andar apply karna hota hai?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 12.91 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.75 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.37 seconds*

---

### Q46: Who notarizes the name change affidavit to be submitted with the application?

**Hindi:** *आवेदन के साथ जमा किए जाने वाले नाम परिवर्तन हलफनामे को कौन नोटरीकृत करता है?*

**Hinglish:** *Application ke sath submit hone wale name change affidavit ko kaun notarize karta hai?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.30 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.65 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.71 seconds*

---

## 7. Out of Scope Queries

### Q47: How can I register my shop under the Shops and Establishment Act in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में मैं दुकान और स्थापना अधिनियम के तहत अपनी दुकान का पंजीकरण कैसे कर सकता हूं?*

**Hinglish:** *CG me Shops and Establishment Act ke under apni shop kaise register kare?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.30 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.47 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 4.31 seconds*

---

### Q48: What is the application procedure for the death certificate on the Sewa Setu portal?

**Hindi:** *सेवा सेतु पोर्टल पर मृत्यु प्रमाण पत्र के लिए आवेदन प्रक्रिया क्या है?*

**Hinglish:** *Sewa Setu portal par death certificate apply karne ka kya process hai?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 4.17 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 5.06 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.80 seconds*

---

### Q49: How do I link my ration card with my Aadhaar card in Chhattisgarh?

**Hindi:** *छत्तीसगढ़ में मैं अपने राशन कार्ड को अपने आधार कार्ड से कैसे लिंक करूं?*

**Hinglish:** *CG me ration card ko Aadhaar card se kaise link kare?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 4.42 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 4.98 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 3.97 seconds*

---

### Q50: What is the subsidy rate for micro-irrigation systems under the Chhattisgarh government schemes?

**Hindi:** *छत्तीसगढ़ सरकार की योजनाओं के तहत सूक्ष्म सिंचाई प्रणालियों के लिए सब्सिडी दर क्या है?*

**Hinglish:** *CG government schemes ke under micro-irrigation system par kitni subsidy milti hai?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 4.08 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 5.36 seconds*

#### 💬 Hinglish Response:
> Error: API returned status 500 - {"detail":"Sarvam AI returned status 402"}

*Latency: 4.13 seconds*

---

## Evaluation Summary & Metrics

- **Total Executed Queries:** 150
- **Total Time Taken:** 5646.92 seconds
- **Average Latency:** 37.65 seconds/query
