# SewaSetu RAG Chatbot Evaluation Report

This report presents the testing results of the chatbot in both English and Hindi across all 5 in-scope citizen services and out-of-scope scenarios. Queries were executed globally without specifying service serial numbers.

## Test Configuration
- **API Server:** `http://localhost:8000/api/chat`
- **Date & Time:** 2026-06-22 11:20:04
- **Total Query Runs:** 120 (60 English + 60 Hindi)

## Table of Contents
- [1. Domicile Certificate (Chhattisgarh Domicile Criteria)](#1-domicile-certificate-chhattisgarh-domicile-criteria)
- [2. Marriage Registration & Certificate](#2-marriage-registration-and-certificate)
- [3. Scheduled Castes (SC) Order 1950](#3-scheduled-castes-sc-order-1950)
- [4. Scheduled Tribes (ST) Order 1950](#4-scheduled-tribes-st-order-1950)
- [5. Social Status Act (Caste Certificate Rules)](#5-social-status-act-caste-certificate-rules)
- [6. Ordinary Gazette Notification for Name Change](#6-ordinary-gazette-notification-for-name-change)
- [7. Out of Scope Queries](#7-out-of-scope-queries)

---

## 1. Domicile Certificate (Chhattisgarh Domicile Criteria)

### Q1: What is the parent's continuous residence requirement for Chhattisgarh domicile?

**Hindi Version:** *छत्तीसगढ़ में मूल निवासी के लिए माता-पिता के लिए निरंतर निवास की आवश्यकता क्या है?*

#### 🇬🇧 English Response:
> Based on the provided context, for a parent to meet the continuous residence requirement for a Chhattisgarh domicile, one of the parents must be a resident of Chhattisgarh for a continuous 25 years.
> 
> Service: Domicile Certificate
> Department: Revenue and disaster management Department

*Latency: 9.78 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में मूल निवासी प्रमाण पत्र के लिए, माता-पिता के निरंतर निवास की आवश्यकता इस प्रकार है: या तो माता-पिता में से कोई छत्तीसगढ़ का निवासी हो, जो निरंतर २५ वर्ष से रह रहा हो।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की गई है।

*Latency: 36.46 seconds*

---

### Q2: If a parent owns property in Chhattisgarh for 5 years but the applicant did not study in Chhattisgarh, are they eligible for domicile?

**Hindi Version:** *यदि माता-पिता के पास छत्तीसगढ़ में 5 वर्षों से संपत्ति है, लेकिन आवेदक ने छत्तीसगढ़ में पढ़ाई नहीं की है, तो क्या वे मूल निवासी के लिए पात्र हैं?*

#### 🇬🇧 English Response:
> No, based on the provided context, the applicant are not eligible for a domicile certificate.
> 
> According to the criteria for a Chhattisgarh Domicile Certificate, both Criteria A and B must be met.
> 
> *   **Criteria A** includes the condition that either of the parents or the applicant holds a property in Chhattisgarh for the last 5 years.
> *   **Criteria B** requires the applicant to have three years of formal education in Chhattisgarh or have passed a board exam from the state.
> 
> Since the applicant did not study in Chhattisgarh, they have not met Criteria B. Therefore, even if the parent owns property in the state, the applicant is not eligible.
> 
> For the Domicile Certificate service, the Revenue and disaster management Department, both Criteria A and B must be met.

*Latency: 9.14 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, इस स्थिति में आवेदक मूल निवासी प्रमाण पत्र के लिए पात्र नहीं होगा।
> 
> राजस्व एवं आपदा प्रबंधन विभाग के मूल निवासी प्रमाण पत्र के लिए दिए गए संदर्भ के अनुसार, आवेदक को मानदंड A और B दोनों को पूरा करना आवश्यक है।
> 
> *   **मानदंड A:** आवेदक के माता-पिता में से किसी के पास पिछले 5 वर्षों से छत्तीसगढ़ में संपत्ति होनी चाहिए। आपकी स्थिति में यह शर्त पूरी होती है।
> *   **मानदंड B:** आवेदक को छत्तीसगढ़ में 3 वर्ष की औपचारिक शिक्षा पूरी करनी चाहिए या कक्षा 5, 8, 10, या 12 की बोर्ड परीक्षाओं में से किसी एक में उत्तीर्ण होना चाहिए। चूंकि आपने उल्लेख किया है कि आवेदक ने छत्तीसगढ़ में पढ़ाई नहीं की है, इसलिए यह शर्त पूरी नहीं होती है।
> 
> चूंकि मानदंड A और B दोनों का पूरा होना अनिवार्य है, इसलिए आवेदक इस प्रमाण पत्र के लिए पात्र नहीं है।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग के मूल निवासी प्रमाण पत्र से संबंधित है।

*Latency: 13.00 seconds*

---

### Q3: Are both Criteria A and B required to get a Domicile Certificate in Chhattisgarh, and are there any exceptions?

**Hindi Version:** *क्या छत्तीसगढ़ में मूल निवासी प्रमाण पत्र प्राप्त करने के लिए मानदंड A और B दोनों आवश्यक हैं, और क्या इसके कोई अपवाद हैं?*

#### 🇬🇧 English Response:
> हाँ, Chhattisgarh में Domicile Certificate प्राप्त करने के लिए, मुख्य मानदंडों (criteria) को पूरा करने हेतु Criteria A और B दोनों का पूरा होना अनिवार्य है।
> 
> **Criteria A** के अंतर्गत निम्नलिखित में से कोई एक शामिल है:
> *   CG में जन्म (Birth Certificate)
> *   या तो माता-पिता में से कोई 25 वर्षों से CG का निवासी हो
> *   या माता-पिता में से कोई CG सरकार या उसके किसी उपक्रम (undertaking) का कर्मचारी हो
> *   या आवेदक या उसके माता-पिता में से कोई CG में संपत्ति रखता हो (पिछले 5 वर्षों के लिए)
> 
> **Criteria B** के अंतर्गत निम्नलिखित में से कोई एक शामिल है:
> *   CG में 3 वर्ष की औपचारिक शिक्षा (formal education)
> *   या CG से किसी बोर्ड परीक्षा (Class 5, 8, 10, 12) में उत्तीर्ण होना
> 
> **Criteria C** के अंतर्गत आने वाले व्यक्तियों के लिए एक अपवाद है। Criteria C के अंतर्गत, Criteria A और B की आवश्यकता नहीं होती है। Criteria C उन विशिष्ट मामलों पर लागू होता है जहाँ:
> *   आवेदक का जीवनसाथी (spouse) CG का निवासी हो
> *   आवेदक या उसका जीवनसाथी CG सरकार का कर्मचारी हो
> *   आवेदक या उसके माता-पिता All India Services में हों और उन्हें CG कैडर आवंटित किया गया हो
> 
> Service: Domicile Certificate, Department: Revenue and disaster management Department.

*Latency: 14.15 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ में मूल निवासी प्रमाण पत्र प्राप्त करने के लिए मानदंड A और B दोनों आवश्यक हैं।
> 
> **मानदंड A और B:**
> *   **मानदंड A:** आवेदक का जन्म छत्तीसगढ़ में हुआ हो (जन्म प्रमाण पत्र) या उसके माता-पिता में से कोई 25 वर्षों से निरंतर छत्तीसगढ़ में निवासी हो, या माता-पिता में से कोई छत्तीसगढ़ सरकार या उसके उपक्रम में कर्मचारी हो, या माता-पिता या आवेदक के पास पिछले 5 वर्षों से छत्तीसगढ़ में संपत्ति हो।
> *   **मानदंड B:** आवेदक ने छत्तीसगढ़ में 3 वर्ष की औपचारिक शिक्षा प्राप्त की हो या उसने छत्तीसगढ़ से ही कक्षा 5, 8, 10, या 12वीं की बोर्ड परीक्षा उत्तीर्ण की हो।
> 
> **अपवाद:**
> मानदंड C के अंतर्गत आने वाले व्यक्तियों के लिए मानदंड A और B की आवश्यकता नहीं है। यदि कोई व्यक्ति मानदंड C के अंतर्गत आता है, तो उसे मानदंड A और B को पूरा करने की आवश्यकता नहीं होती है।
> 
> यह जानकारी राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़ के लिए है।

*Latency: 14.33 seconds*

---

### Q4: Is a person whose spouse is a domicile of Chhattisgarh eligible for domicile, and are criteria A and B required for them?

**Hindi Version:** *क्या वह व्यक्ति जिसका जीवनसाथी छत्तीसगढ़ का मूल निवासी है, मूल निवासी प्रमाण पत्र के लिए पात्र है, और क्या उनके लिए मानदंड A और B आवश्यक हैं?*

#### 🇬🇧 English Response:
> हाँ, जो व्यक्ति Chhattisgarh का निवासी है, उसका जीवनसाथी भी वहाँ का निवासी हो, तो वह व्यक्ति domicile certificate के लिए पात्र है।
> 
> हालाँकि, इस खास मामले में, Criteria A और B की ज़रूरत नहीं है। दिए गए context के मुताबिक, "Criteria C" (जिसमें वो मामले शामिल हैं जहाँ जीवनसाथी का domicile हो) के लिए, Criteria A और B की शर्तें लागू नहीं होती हैं।
> 
> यह जानकारी Revenue और disaster management Department द्वारा दी गई Domicile Certificate service के लिए है।

*Latency: 13.17 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, वह व्यक्ति जिसका जीवनसाथी छत्तीसगढ़ का मूल निवासी है, मूल निवासी प्रमाण पत्र (डोमिसाइल सर्टिफिकेट) के लिए पात्र है।
> 
> लेकिन, उनके लिए मानदंड A और B आवश्यक नहीं हैं।
> 
> इसका कारण यह है कि आपका प्रश्न "मानदंड तीन" (Criteria Three) के अंतर्गत आता है। इस विशेष श्रेणी में, यदि आवेदक या उसका जीवनसाथी छत्तीसगढ़ का मूल निवासी है, तो मानदंड A और B की आवश्यकता नहीं होती है।
> 
> *   **मानदंड A** में जन्म या माता-पिता का निवास शामिल है।
> *   **मानदंड B** में शिक्षा शामिल है।
> 
> ये दोनों केवल "मानदंड C" के लिए आवश्यक होते हैं।
> 
> यह जानकारी Sewa Setu Chhattisgarh पोर्टल के Domicile Certificate (ID: 7) से संबंधित है, जो राजस्व और आपदा प्रबंधन विभाग द्वारा संचालित है।

*Latency: 20.60 seconds*

---

### Q5: What are the board exams accepted under Criteria B for establishing domicile in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में मूल निवासी स्थापित करने के लिए मानदंड B के तहत कौन सी बोर्ड परीक्षाएं स्वीकार की जाती हैं?*

#### 🇬🇧 English Response:
> Based on the provided context for the Domicile Certificate service in Chhattisgarh, the board exams accepted under Criteria B are:
> 
> *   Class 5
> *   Class 8
> *   L०
> *   L२
> 
> This information is from the official document content for the Domicile Certificate service, managed by the Revenue and disaster management Department.

*Latency: 15.93 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में मूल निवासी स्थापित करने के लिए मानदंड B के तहत, निम्नलिखित बोर्ड परीक्षाओं को स्वीकार किया जाता है:
> 
> *   कक्षा 5
> *   कक्षा 8
> *   LKG
> *   L2
> 
> यह जानकारी 'डोमिसाइल सर्टिफिकेट' सेवा से संबंधित है, जो राजस्व और आपदा प्रबंधन विभाग द्वारा प्रदान की जाती है।

*Latency: 13.00 seconds*

---

### Q6: If an applicant is an All India Services officer allotted Chhattisgarh Cadre, do they need to meet Criteria A and B?

**Hindi Version:** *यदि कोई आवेदक अखिल भारतीय सेवा का अधिकारी है और उसे छत्तीसगढ़ कैडर आवंटित किया गया है, तो क्या उसे मानदंड A and B को पूरा करने की आवश्यकता है?*

#### 🇬🇧 English Response:
> No, for this specific case, the applicant does not need to meet Criteria A and B.
> 
> The context for the Domicile Certificate service states that for "Criteria Three," if the applicant or their parent is in the All India Services and has been allotted the CG Cadre, then Criteria A and B are not required. The document explicitly says: "For Criteria C, Criteria A and B are not required."
> 
> For the Domicile Certificate service, the Revenue and disaster management Department.

*Latency: 8.98 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, अगर कोई आवेदक छत्तीसगढ़ कैडर का allot हुआ है और वह अखिल भारतीय सेवा का अधिकारी है, तो उसे मानदंड A और B को पूरा करने की आवश्यकता नहीं है।
> 
> Sewasabh, 'मानदंड तीन' के तहत, अगर आवेदक या उसके माता-पिता अखिल भारतीय सेवा में हैं और उन्हें छत्तीसगढ़ कैडर allot हुआ है, तो उन्हें domicile certificate के लिए पात्र माना जाता है।
> 
> Context के अनुसार, मानदंड C (जिसमें यह शर्त शामिल है) के लिए मानदंड A और B की आवश्यकता नहीं होती है।
> 
> यह सेवा Domicile Certificate है, जिसे राजस्व और आपदा प्रबंधन विभाग द्वारा प्रबंधित किया जाता है।

*Latency: 15.67 seconds*

---

### Q7: List all required documents for applying for a Domicile Certificate in Chhattisgarh.

**Hindi Version:** *छत्तीसगढ़ में मूल निवासी प्रमाण पत्र के लिए आवेदन करने के लिए आवश्यक सभी दस्तावेजों की सूची क्या है?*

#### 🇬🇧 English Response:
> Based on the provided context, here are the required documents for applying for a Domicile Certificate in Chhattisgarh:
> 
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> For Criteria A and B, the following documents are needed:
> *   **Criteria A:** Birth Certificate, or proof that one parent is a resident of CG for 25 continuous years, or that one parent is an employee of CG Government, or that the applicant holds property in CG for the last 5 years.
> *   **Criteria B:** Three years of formal education in CG, or passing one of the board exams (Class 5, 8, 10, 12) from CG.
> 
> For Criteria C, the following documents are needed:
> *   If the applicant's spouse is a domicile of CG.
> *   If the applicant or the spouse is an employee of CG Government or its PSU.
> *   If the applicant or their parents are in all India services and have been allotted CG Cadre.
> 
> **Note:** Criteria A and B must be met together to get the certificate. For Criteria C, Criteria A and B are not required.
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> If you need further assistance, you can contact the Sewa Setu Kendra.
> 
> ---
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The provided context lists the documents required for the Domicile Certificate service. The specific documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context also specifies the criteria for eligibility, which are tied to the required documents. For Criteria A and B, the documents are as listed above. For Criteria C, the documents are related to the applicant's or spouse's employment or parent's service in the CG government.
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding documents for each criterion. The required documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context lists the required documents for the Domicile Certificate service. The documents are:
> 1.  Application
> 2.  Affidavit
> 3.  Educational certificates
> 4.  Service Certificate (if applicable)
> 5.  Property documents (if applicable)
> 6.  Proof of Residence for 25 years (if applicable)
> 7.  Birth Certificate (if available)
> 
> **Service:** Domicile Certificate
> **Department:** Revenue and disaster management Department
> 
> **Note:** The context provides a detailed breakdown of the criteria and the corresponding

*Latency: 36.95 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में मूल निवासी प्रमाण पत्र के लिए आवेदन करने हेतु निम्नलिखित दस्तावेजों की आवश्यकता होती है:
> 
> 1. **शपथ पत्र (Affidavit):** यह अनिवार्य है।
> 2. **निवास का प्रमाण:**
>    - **15 वर्ष के निवास का प्रमाण (अनिवार्य):**
>      - जन्म प्रमाण पत्र
>      - पिता/पालक का सेवा प्रमाण पत्र
>      - वोटिंग कार्ड
>      - राशन कार्ड
>      - बिजली का बिल
>      - घर या भूमि का दस्तावेज़
>      - जन्म सूचना प्रपत्र
>      - वार्ड सदस्य, स्थानीय विधायक/सांसद से प्रमाण पत्र
>    - **5 वर्ष के निवास का प्रमाण (अनिवार्य नहीं):**
>      - घर या भूमि का दस्तावेज़
>      - सेवा पुस्तिका
> 3. **शैक्षणिक प्रमाण पत्र (अनिवार्य):**
>    - माध्यमिक विद्यालय का प्रमाणपत्र (8वीं कक्षा)
>    - प्राथमिक विद्यालय का प्रमाणपत्र (5वीं कक्षा)
>    - हाई स्कूल (10वीं कक्षा) की अंकसूची
>    - उच्चतर माध्यमिक विधालय प्रमाण पत्र (12वीं कक्षा)
>    - एम-फिल
>    - स्कूल प्रमाणपत्र (3 साल की निरंतर अध्ययन के रूप में)
>    - स्नातकोत्तर प्रमाणपत्र
>    - तकनीकी विषयों में प्रमाणपत्र
> 4. **अन्य सहायक दस्तावेज:**
>    - आवेदन
>    - सेवा प्रमाण पत्र (यदि लागू हो)
>    - संपत्ति के दस्तावेज (यदि लागू हो)
>    - जन्म प्रमाण पत्र (यदि उपलब्ध हो)
> 
> जानकारी उपलब्ध नहीं है।

*Latency: 21.47 seconds*

---

### Q8: Does birth in Chhattisgarh alone qualify a person for a domicile certificate?

**Hindi Version:** *क्या केवल छत्तीसगढ़ में जन्म होना ही किसी व्यक्ति को मूल निवासी प्रमाण पत्र के लिए योग्य बनाता है?*

#### 🇬🇧 English Response:
> नहीं, केवल छत्तीसगढ़ में जन्म लेने से व्यक्ति को domicile certificate के लिए पात्र नहीं माना जाता है।
> 
> प्रदान किए गए संदर्भ के अनुसार, domicile certificate प्राप्त करने के लिए, एक आवेदक को मानदंडों के दो सेटों में से कम से कम एक शर्त को पूरा करना होगा:
> 
> 1. **मानदंड एक:** आवेदक का जन्म छत्तीसगढ़ में हुआ हो, या उसके माता-पिता में से कोई 25 वर्षों से निरंतर वहां निवासी हो, या वे छत्तीसगढ़ सरकार के कर्मचारी हों, या उनके पास 5 वर्षों से छत्तीसगढ़ में संपत्ति हो।
> 2. **मानदंड दो:** आवेदक ने छत्तीसगढ़ में कम से कम तीन वर्षों की औपचारिक शिक्षा पूरी की हो, या उन्होंने छत्तीसगढ़ से किसी बोर्ड परीक्षा (कक्षा 5, 8, 10, या 12) में उत्तीर्ण किया हो।
> 
> नोट में उल्लेख है कि आवेदक को पहले सेट की कम से कम एक शर्त और दूसरे सेट की कम से कम एक शर्त को पूरा करना होगा। इसलिए, केवल जन्म के आधार पर जन्म स्थान की शर्त को पूरा किया जा सकता है, लेकिन इसे दूसरे मानदंड की शर्त (जैसे, शिक्षा या बोर्ड परीक्षा) के साथ पूरा करना आवश्यक है।
> 
> सेवा का नाम: Domicile Certificate
> विभाग: राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़।

*Latency: 15.81 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, केवल छत्तीसगढ़ में जन्म लेना ही किसी व्यक्ति को मूल निवासी प्रमाण पत्र के लिए योग्य बनाने के लिए पर्याप्त नहीं है।
> 
> राजस्व और आपदा प्रबंधन विभाग, छत्तीसगढ़ द्वारा प्रदान की गई जानकारी के अनुसार, मूल निवासी प्रमाण पत्र के लिए निम्नलिखित शर्तें हैं:
> 
> 1. **पहली शर्त:** व्यक्ति को या तो छत्तीसगढ़ में जन्म लेना चाहिए (जन्म प्रमाण पत्र के साथ) या फिर उसके माता-पिता में से कोई एक पिछले २५ वर्षों से वहां निवासी होना चाहिए।
> 2. **या फिर** माता-पिता में से कोई एक छत्तीसगढ़ सरकार या उसके उपक्रमों में कर्मचारी होना चाहिए।
> 3. **या फिर** पिछले ५ वर्षों से व्यक्ति या उसके माता-पिता के पास छत्तीसगढ़ में संपत्ति होनी चाहिए।
> 4. **इसके अतिरिक्त**, शिक्षा से संबंधित शर्तें भी हैं, जैसे छत्तीसगढ़ में ३ वर्ष की औपचारिक शिक्षा या किसी बोर्ड परीक्षा (जैसे ५वीं, ८वीं, १०वीं, १२वीं) में उत्तीर्ण होना।
> 
> इसके अतिरिक्त, यदि व्यक्ति का जीवनसाथी मूल निवासी है, या वह स्वयं या उसका माता-पिता अखिल भारतीय सेवा (AIS) में है और उसे छत्तीसगढ़ कैडर आवंटित किया गया है, तो वह भी योग्य माना जा सकता है।
> 
> संक्षेप में, केवल जन्म स्थान ही एकमात्र आधार नहीं है; माता-पिता के निवास, रोजगार, संपत्ति, शिक्षा और अन्य विशिष्ट शर्तों पर भी विचार किया जाता है।

*Latency: 13.02 seconds*

---

## 2. Marriage Registration & Certificate

### Q9: What is the time limit for submitting the marriage registration memorandum to the Registrar in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में रजिस्ट्रार को विवाह पंजीकरण ज्ञापन सौंपने की समय सीमा क्या है?*

#### 🇬🇧 English Response:
> According to the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, the time limit for submitting the marriage registration memorandum to the Registrar is within thirty days from the date of the marriage.

*Latency: 14.29 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में विवाह पंजीकरण ज्ञापन सौंपने की समय सीमा विवाह की तिथि से तीस दिन है। यह ज्ञापन निर्धारित प्रारूप में, तीस दिन के भीतर विवाह संपन्न होने या संपन्न होने की तिथि से, संबंधित क्षेत्र के रजिस्ट्रार को देना अनिवार्य है।
> 
> यह जानकारी 'विवाह पंजीकरण एवं प्रमाण पत्र' सेवा के अंतर्गत आती है, जिसे नगरीय प्रशासन एवं विकास विभाग संचालित करता है।

*Latency: 17.41 seconds*

---

### Q10: What is the penalty under Rule 12 for willfully failing to submit the marriage memorandum?

**Hindi Version:** *विवाह ज्ञापन प्रस्तुत करने में जानबूझकर विफल रहने पर नियम 12 के तहत क्या जुर्माना है?*

#### 🇬🇧 English Response:
> Rule 12 के अनुसार, विवाह के ज्ञापन (memorandum) को स्वेच्छा से प्रस्तुत करने में विफल रहने पर दंड के रूप में जुर्माना लगाया जाता है, जो पाँच सौ रुपये तक बढ़ सकता है।
> 
> यह जानकारी छत्तीसगढ़ अनिवार्य विवाह पंजीकरण नियम, 2006 से ली गई है, जो "विवाह पंजीकरण और प्रमाण पत्र" (Marriage Registration & Certificate) सेवा और "शहरी प्रशासन और विकास विभाग" (Urban Administration and development Department) के अंतर्गत आती है।

*Latency: 9.90 seconds*

#### 🇮🇳 Hindi Response:
> सूचना उपलब्ध नहीं है।

*Latency: 20.17 seconds*

---

### Q11: What is the penalty under Rule 13 for destroying or tampering with the marriage register?

**Hindi Version:** *विवाह रजिस्टर को नष्ट करने या उससे छेड़छाड़ करने पर नियम 13 के तहत क्या जुर्माना है?*

#### 🇬🇧 English Response:
> Based on the provided context, the penalty for destroying or tampering with the marriage register is a fine of rupees two thousand. This fine is in addition to any punishment that may be awarded under other laws in force at the time.
> 
> This information is from the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, under the Urban Administration and development Department.

*Latency: 10.57 seconds*

#### 🇮🇳 Hindi Response:
> विवाह रजिस्टर को नष्ट करने या उससे छेड़छाड़ करने पर नियम 13 के तहत 2000 रुपये का जुर्माना है।
> 
> नियम 13 के अनुसार, जो व्यक्ति रजिस्टर को नष्ट करता है, उससे छेड़छाड़ करता है, या झूठी जानकारी देता है, उसे 2000 रुपये का जुर्माना और वर्तमान में लागू किसी भी अन्य कानून के तहत दंड दिया जा सकता है। यह जुर्माना नियम 13 के तहत लगाया जाता है।
> 
> सेवा का नाम: विवाह पंजीकरण एवं प्रमाण पत्र।
> विभाग: शहरी प्रशासन और विकास विभाग।

*Latency: 15.57 seconds*

---

### Q12: If a marriage is not registered, does it become invalid in the state of Chhattisgarh under these rules?

**Hindi Version:** *यदि विवाह पंजीकृत नहीं है, तो क्या वह इन नियमों के तहत छत्तीसगढ़ राज्य में अमान्य हो जाता है?*

#### 🇬🇧 English Response:
> नहीं, दिए गए नियमों के मुताबिक, Chhattisgarh में शादी को अमान्य नहीं माना जाता, बस इसलिए कि वह register नहीं हुई है।
> 
> Chhattisgarh Compulsory Registration of Marriages Rules, 2006 का Rule 9 साफ़ तौर पर कहता है: "इन नियमों के तहत की गई शादी को सिर्फ़ इस वजह से अमान्य नहीं माना जाएगा कि वह नियमों के तहत register नहीं हुई है।"
> 
> इसका मतलब है कि भले ही शादी register करना ज़रूरी है, लेकिन शादी की कानूनी हैसियत (validity) इस बात पर निर्भर नहीं करती कि वह register हुई है या नहीं।
> 
> यह जानकारी Chhattisgarh के Urban Administration and development Department द्वारा दी गई Marriage Registration & Certificate service से जुड़ी है।

*Latency: 11.29 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, छत्तीसगढ़ के नियमों के तहत, अगर शादी पंजीकृत नहीं है, तो वह अमान्य नहीं हो जाती।
> 
> यह बात छत्तीसगढ़ कंपल्सरी रजिस्ट्रेशन ऑफ मैरिज रूल्स, 2006 के नियम 9 में स्पष्ट रूप से लिखी गई है। नियम 9 में कहा गया है कि जो शादी इन नियमों के तहत आती है, उसके पंजीकृत न होने से वह अमान्य नहीं मानी जाती।

*Latency: 13.41 seconds*

---

### Q13: What is the appeal process, fee, and timeline if the Marriage Registrar refuses to register a marriage?

**Hindi Version:** *यदि विवाह रजिस्ट्रार विवाह पंजीकृत करने से इनकार करता है तो अपील प्रक्रिया, शुल्क और समय सीमा क्या है?*

#### 🇬🇧 English Response:
> Based on the provided context, here is the appeal process, fee, and timeline for a Marriage Registrar refusing to register a marriage:
> 
> **Appeal Process:**
> If the Marriage Registrar refuses to register a marriage, the aggrieved person can appeal to the Chief Registrar. The appeal must be made within 30 days from the date of receiving the refusal order. The appeal should be accompanied by a fee of Rs. 30.
> 
> **Fee:**
> The fee for appealing to the Chief Registrar is Rs. 30.
> 
> **Timeline:**
> The appeal to the Chief Registrar must be filed within 30 days of receiving the refusal order from the Marriage Registrar.
> 
> **Additional Information:**
> - The Chief Registrar will give an opportunity to be heard to both parties before passing an order.
> - After hearing, the Chief Registrar will either direct the Registrar to register the marriage or confirm the order of the original Registrar.
> - The decision of the Chief Registrar is final.
> 
> **Service Details:**
> This process is managed by the Urban Administration and development Department under the Sewa Setu Chhattisgarh portal. For more information, you can contact the Sewa Setu Kendra.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the pages.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it is not considered invalid solely because it was not registered. However, registration is mandatory under the rules.
> 
> **Note:**
> The context also mentions that if a marriage is not registered, it

*Latency: 25.87 seconds*

#### 🇮🇳 Hindi Response:
> अगर marriage registrar vivah panjikrit karne se mana kar de, to aapke paas appeal karne ka adhikar hai.
> 
> **1. Appeal Prakriya:**
> Aap Chief Registrar mein appeal kar sakte hain.
> 
> **2. Samay Seema:**
> Aapko vivah vivaran (order) milne ki tarikh se 30 din ke andar appeal karni hogi.
> 
> **3. Shulk:**
> Is appeal ke liye Rs. 30/- ki fee deni hogi.
> 
> Agar aapko Chief Registrar ka nirnay bhi pasand nahi aata, to aap District Judge mein appeal kar sakte hain. Yeh appeal bhi 30 din ke andar karni hogi.
> 
> Sewa Setu Chhattisgarh portal, Urban Administration and Development Department.

*Latency: 20.75 seconds*

---

### Q14: Who is the designated Marriage Registrar for a local area in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में किसी स्थानीय क्षेत्र के लिए मनोनीत विवाह रजिस्ट्रार कौन है?*

#### 🇬🇧 English Response:
> Based on the provided context, the designated Marriage Registrar for a local area in Chhattisgarh is the **Local Authority**.
> 
> This includes entities such as a Gram Panchayat, Municipality, or Municipal Corporation. The State Government also appoints a Chief Registrar for the entire state, who oversees the work of the local registrars.
> 
> The service is Marriage Registration & Certificate, handled by the Urban Administration and development Department.

*Latency: 9.44 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ के नियमों के अनुसार, किसी स्थानीय क्षेत्र के लिए मनोनीत विवाह रजिस्ट्रार उस क्षेत्र का "स्थानीय प्राधिकरण" (Local Authority) होता है।
> 
> इसका अर्थ है कि:
> *   ग्राम पंचायत, नगरपालिका या नगर निगम, जो भी संबंधित स्थानीय क्षेत्र के अंतर्गत आता है, उस क्षेत्र के लिए विवाह रजिस्ट्रार के रूप में कार्य करता है।
> *   राज्य सरकार पूरे राज्य के लिए मुख्य रजिस्ट्रार नियुक्त कर सकती है, लेकिन किसी विशिष्ट स्थानीय क्षेत्र के लिए, स्थानीय प्राधिकरण स्वयं ही रजिस्ट्रार के रूप में कार्य करता है।
> 
> सेवा का नाम: विवाह पंजीकरण एवं प्रमाण पत्र (ID: 3) विभाग: शहरी प्रशासन एवं विकास विभाग।

*Latency: 13.88 seconds*

---

### Q15: Under what rule and fee can a member of the public inspect the Register of Marriages?

**Hindi Version:** *जनता किस नियम और शुल्क के तहत विवाह रजिस्टर का निरीक्षण कर सकती है?*

#### 🇬🇧 English Response:
> Under Rule 8 of the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, a member of the public can inspect the Register of Marriages. The fee for this inspection is Rs. 20.
> 
> Service: Marriage Registration & Certificate (ID: 3)
> Department: Urban Administration and development Department.

*Latency: 12.15 seconds*

#### 🇮🇳 Hindi Response:
> जनता विवाह रजिस्टर का निरीक्षण **नियम 8** के अनुसार कर सकती है।
> 
> नियम 8 के अनुसार, विवाह का रजिस्टर सभी उचित समय पर निरीक्षण के लिए खुला रहेगा। इसके अलावा, प्रमाणित प्रति प्राप्त करने के लिए **20 रुपये** शुल्क देना होगा।

*Latency: 11.80 seconds*

---

### Q16: Does the definition of marriage under the Chhattisgarh Rules include remarriages, and does it apply to all religions?

**Hindi Version:** *क्या छत्तीसगढ़ नियमों के तहत विवाह की परिभाषा में पुनर्विवाह शामिल है, और क्या यह सभी धर्मों पर लागू होता है?*

#### 🇬🇧 English Response:
> Yes, the definition of marriage under the Chhattisgarh Rules includes remarriages and applies to all religions.
> 
> According to the definition in Rule 2 of the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, the term "Marriage" explicitly includes a remarriage. The same definition states that it applies "irrespective of the religion Or caste of either party to the marriage."
> 
> This information is from the official document for the "Marriage Registration & Certificate" service, provided by the Urban Administration and development Department.

*Latency: 13.21 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ के नियमों के तहत विवाह की परिभाषा में पुनर्विवाह शामिल है।
> 
> यह परिभाषा सभी धर्मों पर लागू होती है। नियम 2. परिभाषा के अनुसार, 'विवाह' में 'पुनर्विवाह' भी शामिल है।
> 
> इसमें कहा गया है: '...और भी इसमें पुनर्विवाह शामिल है;' और यह 'धर्म या जाति की परवाह किए बिना' लागू होता है।
> 
> इसका मतलब है कि चाहे कोई भी धर्म हो, पुनर्विवाह को विवाह की परिभाषा में माना गया है।
> 
> यह जानकारी छत्तीसगढ़ के अनिवार्य विवाह पंजीकरण नियमों के अनुसार है।

*Latency: 13.53 seconds*

---

### Q17: Can an employer update their office records regarding an employee's marital status without a marriage registration certificate?

**Hindi Version:** *क्या कोई नियोक्ता विवाह पंजीकरण प्रमाणपत्र के बिना किसी कर्मचारी की वैवाहिक स्थिति के संबंध में अपने कार्यालय के रिकॉर्ड को अपडेट कर सकता है?*

#### 🇬🇧 English Response:
> No, an employer cannot update their office records regarding an employee's marital status without a marriage registration certificate.
> 
> According to Rule 11 of the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, no employer or any government authority shall carry out any change in their office record, such as a change in the marital status of an employee, unless the employee submits a certified copy of the marriage registration certificate.
> 
> This is a mandatory requirement under the rules for the Urban Administration and development Department.

*Latency: 12.00 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, कोई भी नियोक्ता अपने कर्मचारी के वैवाहिक स्थिति से संबंधित अपने कार्यालय के रिकॉर्ड को विवाह पंजीकरण प्रमाणपत्र के बिना अपडेट नहीं कर सकता है।
> 
> दी गई जानकारी के अनुसार, नियम 11 के अनुसार:
> 
> "कोई भी नियोक्ता, सरकारी या अर्ध-सरकारी प्राधिकरण, कंपनी, सार्वजनिक क्षेत्र का उपक्रम, या स्थानीय प्राधिकरण अपने कर्मचारी के वैवाहिक स्थिति या नामांकन में बदलाव सहित किसी भी कार्यालय दस्तावेज़ में बदलाव नहीं करेगा, जब तक कि कर्मचारी या आवेदक, जो ऐसा बदलाव करना चाहता है, विवाह पंजीकरण का प्रमाणित प्रतिलिपि प्रस्तुत नहीं करता है।"
> 
> इसका अर्थ है कि नियोक्ता को कर्मचारी द्वारा विवाह पंजीकरण प्रमाणपत्र प्रस्तुत करने की प्रतीक्षा करनी होगी, इससे पहले कि वह कर्मचारी के रिकॉर्ड में कोई बदलाव कर सके।
> 
> Sewa Setu Chhattisgarh portal के 'Marriage Registration & Certificate' सेवा के अंतर्गत, यह नियम है।

*Latency: 14.02 seconds*

---

### Q18: Who is the final appellate authority if the Chief Registrar confirms the refusal to register a marriage?

**Hindi Version:** *यदि मुख्य रजिस्ट्रार विवाह पंजीकृत करने से इनकार करने के आदेश की पुष्टि करता है, तो अंतिम अपीलीय प्राधिकारी कौन होता है?*

#### 🇬🇧 English Response:
> According to the provided context, if the Chief Registrar confirms the refusal to register a marriage, the final appellate authority is the **District Judge**.
> 
> This is stated in Rule 6 of the Chhattisgarh Compulsory Registration of Marriages Rules, 2006, which says that any person aggrieved by the order of the Chief Registrar can appeal to the District Judge within 30 days, and the decision of the District Judge shall be final.
> 
> This service is provided by the Urban Administration and Development Department.

*Latency: 9.02 seconds*

#### 🇮🇳 Hindi Response:
> यदि मुख्य रजिस्ट्रार विवाह पंजीकृत करने से इनकार करने के आदेश की पुष्टि करता है, तो अंतिम अपीलीय प्राधिकारी **जिला न्यायाधीश** होता है।
> 
> 'चhattisgarh compulsory registration of marriages rules, 2006' के **नियम 6** के अनुसार, कोई भी व्यक्ति मुख्य रजिस्ट्रार के आदेश से असंतुष्ट होने पर, उस आदेश की तिथि से तीस दिनों के भीतर, संबंधित जिले के **जिला न्यायाधीश** के पास अपील कर सकता है।
> 
> जिला न्यायाधीश का निर्णय अंतिम होता है।
> 
> यह जानकारी 'अर्बन एडमिनिस्ट्रेशन एंड डेवलपमेंट डिपार्टमेंट' के अंतर्गत 'सेवा सेटू छत्तीसगढ़ पोर्टल' के लिए प्रासंगिक है।

*Latency: 13.85 seconds*

---

## 3. Scheduled Castes (SC) Order 1950

### Q19: According to Paragraph 3 of the Constitution (Scheduled Castes) Order 1950, which religions must a person profess to be deemed a Scheduled Caste?

**Hindi Version:** *संविधान (अनुसूचित जाति) आदेश 1950 के पैराग्राफ 3 के अनुसार, कोई व्यक्ति किस धर्म को मानने पर ही अनुसूचित जाति का सदस्य माना जा सकता है?*

#### 🇬🇧 English Response:
> Constitution (Scheduled Castes) Order, १९५० के अनुसार, किसी व्यक्ति को Scheduled Caste मानने के लिए उसे निम्नलिखित में से किसी एक धर्म का पालन करना होगा:
> 
> 1. हिंदू
> 2. सिख
> 3. बौद्ध
> 
> दिए गए संदर्भ में उल्लेख है: "पैराग्राफ 2 में जो कुछ भी निहित है, उसके बावजूद, कोई भी व्यक्ति जो हिंदू, सिख या बौद्ध के अतिरिक्त किसी अन्य धर्म का पालन करता है, उसे Scheduled Caste का सदस्य नहीं माना जाएगा।"
> 
> यह जानकारी Revenue and disaster management Department द्वारा प्रदान की जाने वाली SC/ST Certificate सेवा के लिए प्रासंगिक है।

*Latency: 15.50 seconds*

#### 🇮🇳 Hindi Response:
> पैराग्राफ 3 के अनुसार, किसी व्यक्ति को अनुसूचित जाति का सदस्य मानने के लिए, उसे हिंदू, सिख या बौद्ध धर्म को मानना चाहिए। जो व्यक्ति किसी और धर्म को मानता है, उसे अनुसूचित जाति का सदस्य नहीं माना जाता।

*Latency: 11.90 seconds*

---

### Q20: Is 'Audhelia' recognized as a Scheduled Caste in the State of Chhattisgarh under Part XVIIIL of the 1950 Order?

**Hindi Version:** *क्या 1950 के आदेश के भाग XVIIIL के तहत छत्तीसगढ़ राज्य में 'औधेलिया' (Audhelia) को अनुसूचित जाति के रूप में मान्यता प्राप्त है?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}

*Latency: 714.35 seconds*

#### 🇮🇳 Hindi Response:
> नमस्ते। आपके प्रश्न के संबंध में, प्रदान किए गए संदर्भ में 'औधेलिया' जाति का उल्लेख नहीं है। संदर्भ में अनुसूचित जातियों की सूचियाँ तो हैं, लेकिन 'औधेलिया' उनमें शामिल नहीं है।
> 
> जानकारी उपलब्ध नहीं है।
> 
> सेवा: अनुसूचित जाति/जनजाति प्रमाण पत्र (ID: 4) विभाग: राजस्व एवं आपदा प्रबंधन विभाग

*Latency: 26.09 seconds*

---

### Q21: Under which entry number are castes like Jatav, Mochi, Regar, Satnami, and Ramnami listed for Chhattisgarh in the SC Order 1950?

**Hindi Version:** *अनुसूचित जाति आदेश 1950 में छत्तीसगढ़ के लिए जाटव, मोची, रेगर, सतनामी और रामनामी जैसी जातियों को किस प्रविष्टि संख्या के तहत सूचीबद्ध किया गया है?*

#### 🇬🇧 English Response:
> दिलेल्या संदर्भाच्या आधारे, छत्तीसगडसाठी, जाटव, मोची, रेगार, सतनमी आणि रामनमी या जातींची यादी **37** या नोंदणी क्रमांकांतर्गत दिली आहे.
> 
> ही माहिती छत्तीसगडसाठी अधिकृत दस्तऐवज मजकुरात आढळते, जी रेव्हेन्यू आणि डिझास्टर मॅनेजमेंट विभागांतर्गत एससी/एसटी प्रमाणपत्र (आयडी: 4) या सेवेसाठी आहे.

*Latency: 22.84 seconds*

#### 🇮🇳 Hindi Response:
> आपके प्रश्न के अनुसार, संविधान (अनुसूचित जाति) आदेश, 1950 के अंतर्गत छत्तीसगढ़ के लिए सूचीबद्ध जातियाँ प्रविष्टि संख्या 27 के अंतर्गत आती हैं।
> 
> स्रोत सामग्री में प्रविष्टि संख्या 27 में जाटव, मोची, रेगर, सतनामी और रामनामी जैसी जातियाँ शामिल हैं। यह जानकारी 'SC/ST Certificate' सेवा (ID: 4) और 'राजस्व और आपदा प्रबंधन विभाग' से संबंधित है।

*Latency: 24.09 seconds*

---

### Q22: Are 'Kolupulvandlu', 'Pambada', and 'Pambala' recognized as Scheduled Castes in Andhra Pradesh, and what is their entry number?

**Hindi Version:** *क्या 'कोलुपुलवांडलू', 'पामबाड़ा' और 'पामबाला' को आंध्र प्रदेश में अनुसूचित जाति के रूप में मान्यता दी गई है, और उनकी प्रविष्टि संख्या क्या है?*

#### 🇬🇧 English Response:
> Yes, based on the provided context, 'Kolupulvandlu', 'Pambada', and 'Pambala' are recognized as Scheduled Castes in Andhra Pradesh. They are listed together in entry number 30.
> 
> Service: SC/ST Certificate
> Department: Revenue and disaster management Department

*Latency: 15.99 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, 'कोलुपुलवांडलू', 'पामबाड़ा' और 'पामबाला' को आंध्र प्रदेश में अनुसूचित जाति के रूप में मान्यता दी गई है। उनकी entry number 52 है।
> 
> Constitution (Scheduled Castes) Order, 1950 के अनुसार, Andhra Pradesh की official list में ये castes entry number 52 के under आती हैं। Entry number 52 में ये castes listed हैं:
> 
> 1. कोलुपुलवांडलू
> 2. पामबाड़ा
> 3. पामंदा
> 4. पामबाला
> 
> यह जानकारी 'SC/ST Certificate' सेवा के लिए है, जो 'राजस्व और आपदा प्रबंधन विभाग' के अंतर्गत आती है।

*Latency: 19.10 seconds*

---

### Q23: Which entry in the Scheduled Castes list for Chhattisgarh includes 'Dumar, Dome, Domar, and Doris'?

**Hindi Version:** *छत्तीसगढ़ के लिए अनुसूचित जाति की सूची में किस प्रविष्टि में 'डुमार, डोम, डोमार और डोरिस' शामिल हैं?*

#### 🇬🇧 English Response:
> Based on the provided context, the entry in the Scheduled Castes list for Chhattisgarh that includes 'Dumar, Dome, Domar, and Doris' is **Bagri, Bagdi**.
> 
> The source lists it as:
> '२. Bagri, Bagdi २३. Dom, Dumar, Dome, Domar, Doris ३. Bahna, Bahana'
> 
> This information is from the SC/ST Certificate service under the Revenue and disaster management Department.

*Latency: 12.34 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ के अनुसूचित जाति की सूची में, प्रविष्टि संख्या 4 में 'डुमार, डोम, डोमार और डोरिस' शामिल हैं।
> 
> स्रोत 1 के अनुसार, प्रविष्टि 4 है: "Dom, Dumar, Dome, Domar, Doris"।
> 
> यह प्रविष्टि "राजस्व और आपदा प्रबंधन विभाग" के अंतर्गत "अनुसूचित जाति/अनुसूचित जनजाति प्रमाण पत्र" सेवा के लिए है।

*Latency: 15.09 seconds*

---

### Q24: Is 'Banchada' recognized as a Scheduled Caste in Chhattisgarh, and under which entry number?

**Hindi Version:** *क्या छत्तीसगढ़ में 'बांछड़ा' (Banchada) को अनुसूचित जाति के रूप में मान्यता प्राप्त है, और किस प्रविष्टि संख्या के तहत?*

#### 🇬🇧 English Response:
> हाँ, प्रदान किए गए संदर्भ के अनुसार, 'बंचड़ा' को छत्तीसगढ़ में अनुसूचित जाति के रूप में मान्यता प्राप्त है। इसे आधिकारिक दस्तावेज़ सूचियों में प्रविष्टि संख्या 26 के रूप में सूचीबद्ध किया गया है।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की जाने वाली SC/ST प्रमाण पत्र सेवा का हिस्सा है।

*Latency: 20.68 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, छत्तीसगढ़ में बांछड़ा समुदाय को अनुसूचित जाति के रूप में मान्यता प्राप्त है। यह सूची में प्रविष्टि संख्या 26 के अंतर्गत आता है। यह सूची छत्तीसगढ़ राज्य के लिए है, जो संविधान (अनुसूचित जाति) आदेश, 1950 के अंतर्गत आती है।
> 
> सेवा: SC/ST प्रमाणपत्र (ID: 4)
> विभाग: राजस्व और आपदा प्रबंधन विभाग

*Latency: 16.68 seconds*

---

### Q25: Are 'Kalbelia', 'Sapera', and 'Kubutar' listed under the Scheduled Castes list for Chhattisgarh, and under which entry?

**Hindi Version:** *क्या छत्तीसगढ़ के लिए अनुसूचित जाति की सूची में 'कालबेलिया', 'सपेरा' और 'कबूतर' शामिल हैं, और किस प्रविष्टि के तहत?*

#### 🇬🇧 English Response:
> हो, 'Kalbelia', 'Sapera', र 'Kubutar' Chhattisgarh-को SC/ST Certificate service-को official document content-मा एउटै entry-मा list गरिएको छ।
> 
> Source 1-को "Official Document Content" section-अनुसार, entry यस्तो छ:
> `16. Meghwal 15. Chidar 39. Moghia 16. Chikwa, Chikvi 40. Muskhan 17. Chitar ४१. Nat, Kalbelia, Sapera, Navdigar, Kubutar १८. Dahait, Dahayat Dahat 42. Pardhi...`
> 
> यस entry-मा यी तीनै castes-लाई एउटै group-मा list गरिएको छ।
> 
> यो information **SC/ST Certificate** service-को **Revenue and disaster management Department**-का लागि provide गरिएको हो।

*Latency: 20.67 seconds*

#### 🇮🇳 Hindi Response:
> आपके प्रश्न के संबंध में, प्रदान किए गए संदर्भ में छत्तीसगढ़ की अनुसूचित जाति सूची की जानकारी उपलब्ध नहीं है। जानकारी उपलब्ध नहीं है।

*Latency: 14.22 seconds*

---

### Q26: How many distinct entries are listed under Part XVIIIL for Chhattisgarh in the Constitution (Scheduled Castes) Order, 1950?

**Hindi Version:** *संविधान (अनुसूचित जाति) आदेश, 1950 में छत्तीसगढ़ के लिए भाग XVIIIL के तहत कितनी अलग प्रविष्टियां सूचीबद्ध हैं?*

#### 🇬🇧 English Response:
> Based on the provided context, there are 16 distinct entries listed under Part XVIIIL for Chhattisgarh in the Constitution (Scheduled Castes) Order, 1950. These entries are: Audhelia, Dohor, Bagri, Bagdi, Dom, Dumar, Dome, Domar, Doris, Bahna, Bahana, Ganda, Gandi, Balahi, Balai, Ghasi, Ghasia, Banchada, Holiya, Barahar, Basod, Kanjar, Bargunda, Katia, Patharia, Basor, Burud, Bansor, Bansodi, Bansphor, Basar, Khatik, Bedia, Koli, Kori, Beldar, Sunkar, Khangar, Kanera, Mirdha, Bhangi, Mehtar, Balmiki, Lalbegi, Dharkar, Kuchbandhia, Bhanumati, Mahar, Mehra, Mehar, Chadar, Mang, Mang Garodi, Mang Garudi, Dankhani, Mang, Chamar, Chamari, Bairwa, Bhambhi, Jatav, Mochi, Mang Mahasi, Madari, Garudi, Radhe Mang Regar, Nona, Rohidas, Ramnami Satnami, Meghwal, Surjyabanshi, Surjyaramnami, Ahirwar, Chamar, Moghia, Mangan, Raidas, Muskhan, Chidar, Nat, Kalbelia, Sapera, Navdigar, Kubutar, Chikwa, Chikvi, Pasi, Chitar, Rujjhar, Dahait, Dahayat, Dahat, Sansi, Sansia, Dewar, Silawat, Dhanuk, Zamral, Dhed, Dher.
> 
> Information not available.

*Latency: 6.43 seconds*

#### 🇮🇳 Hindi Response:
> संविधान (अनुसूचित जाति) आदेश, 1950 में छत्तीसगढ़ के लिए भाग XVIIIL के तहत सूचीबद्ध अलग-अलग प्रविष्टियों की संख्या 41 है।
> 
> यह जानकारी 'SC/ST Certificate' सेवा और 'राजस्व और आपदा प्रबंधन विभाग' से संबंधित है।

*Latency: 19.46 seconds*

---

## 4. Scheduled Tribes (ST) Order 1950

### Q27: Name any five Scheduled Tribes listed for Chhattisgarh in the Constitution (Scheduled Tribes) Order, 1950.

**Hindi Version:** *संविधान (अनुसूचित जनजाति) आदेश, 1950 में छत्तीसगढ़ के लिए सूचीबद्ध किन्हीं पांच अनुसूचित जनजातियों के नाम बताइए।*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 25.86 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।
> सेवा का नाम: SC/ST प्रमाणपत्र (ID: 4), विभाग: राजस्व और आपदा प्रबंधन विभाग।

*Latency: 12.56 seconds*

---

### Q28: Under which entry number is 'Halba, Halbi' listed as a Scheduled Tribe for Chhattisgarh in the 1950 Order?

**Hindi Version:** *1950 के आदेश में छत्तीसगढ़ के लिए 'हलबा, हलबी' को किस प्रविष्टि संख्या के तहत अनुसूचित जनजाति के रूप में सूचीबद्ध किया गया है?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 28.13 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 13.89 seconds*

---

### Q29: Is 'Bhil Mina' recognized as a Scheduled Tribe in Chhattisgarh under Part XX of the Scheduled Tribes Order?

**Hindi Version:** *क्या अनुसूचित जनजाति आदेश के भाग XX के तहत छत्तीसगढ़ में 'भील मीना' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है?*

#### 🇬🇧 English Response:
> Based on the provided context, the specific list of Scheduled Tribes for Chhattisgarh is not included. The document lists tribes for other states like Andhra Pradesh and Assam. In the list for Andhra Pradesh, 'Bhil' is mentioned, but 'Bhil Mina' is not explicitly listed. Therefore, the information to confirm if 'Bhil Mina' is a Scheduled Tribe in Chhattisgarh is not available in the provided context. For official details, you can refer to the service 'SC/ST Certificate' under the 'Revenue and disaster management Department'.

*Latency: 24.31 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, प्रदान किए गए संदर्भ के अनुसार, संविधान (अनुसूचित जनजाति) आदेश, 1950 के तहत छत्तीसगढ़ में 'भील मीना' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त नहीं है।
> 
> संविधान (अनुसूचित जनजाति) आदेश, 1950 के तहत छत्तीसगढ़ के लिए आधिकारिक दस्तावेजों में भील और मीना सहित सूचीबद्ध जनजातियों की सूची में 'भील' या 'मीना' शब्द शामिल नहीं हैं। यह जानकारी प्रदान किए गए उपयोगकर्ता नियमावली (user manual) के पृष्ठ 16 पर उपलब्ध सूची से ली गई है।
> 
> सेवा: अनुसूचित जनजाति प्रमाण पत्र (ID: 4), राजस्व और आपदा प्रबंधन विभाग।

*Latency: 18.05 seconds*

---

### Q30: What geographical limits or specific districts are mentioned for the 'Gond' tribe in the Chhattisgarh Scheduled Tribes list?

**Hindi Version:** *छत्तीसगढ़ अनुसूचित जनजाति की सूची में 'गोंड' जनजाति के लिए कौन सी भौगोलिक सीमाएं या विशिष्ट जिले बताए गए हैं?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))"}

*Latency: 70.32 seconds*

#### 🇮🇳 Hindi Response:
> Error: API returned status 500 - {"detail":"HTTPSConnectionPool(host='api.sarvam.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NameResolutionError(\"HTTPSConnection(host='api.sarvam.ai', port=443): Failed to resolve 'api.sarvam.ai' ([Errno 11001] getaddrinfo failed)\"))"}

*Latency: 2.27 seconds*

---

### Q31: Under entry 5 of Andhra Pradesh in the Scheduled Tribes list, which sub-tribes of Gadabas are recognized?

**Hindi Version:** *अनुसूचित जनजाति सूची में आंध्र प्रदेश की प्रविष्टि 5 के तहत गदबा (Gadabas) की कौन सी उप-जनजातियां मान्यता प्राप्त हैं?*

#### 🇬🇧 English Response:
> Error: API returned status 500 - {"detail":"HTTPSConnectionPool(host='api.sarvam.ai', port=443): Max retries exceeded with url: /v1/chat/completions (Caused by NameResolutionError(\"HTTPSConnection(host='api.sarvam.ai', port=443): Failed to resolve 'api.sarvam.ai' ([Errno 11001] getaddrinfo failed)\"))"}

*Latency: 131.76 seconds*

#### 🇮🇳 Hindi Response:
> अनुसूचित जनजाति सूची में आंध्र प्रदेश की प्रविष्टि 5 के तहत गदबा (Gadabas) की मान्यता प्राप्त उप-जनजातियां हैं:
> 
> 1. **गदबा (Gadabas)**
> 2. **गदबा (Gadabas)**
> 
> *(नोट: प्रदान किए गए संदर्भ में इस विशिष्ट प्रश्न का उत्तर देने के लिए आवश्यक जानकारी नहीं है।)*
> 
> सेवा नाम: अनुसूचित जाति/जनजाति प्रमाण पत्र
> विभाग: राजस्व एवं आपदा प्रबंधन विभाग, छत्तीसगढ़
> 
> नोट: प्रदान किया गया संदर्भ मुख्य रूप से छत्तीसगढ़ में अनुसूचित जाति/जनजाति प्रमाण पत्र और अन्य पिछड़ा वर्ग (OBC) प्रमाण पत्र के लिए उपयोगकर्ता नियमावली (user manuals) से संबंधित है। इसमें आंध्र प्रदेश की प्रविष्टि 5 के तहत गदबा (Gadabas) की उप-जनजातियों के बारे में जानकारी नहीं है।

*Latency: 15.06 seconds*

---

### Q32: Is 'Kawar, Kanwar, Kaur, Cherwa, Rathia, Tanwar, Chattri' recognized as a Scheduled Tribe in Chhattisgarh, and what is its entry number?

**Hindi Version:** *क्या छत्तीसगढ़ में 'कवर, कंवर, कौर, चेरवा, रथिया, तंवर, छत्री' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है, और इसकी प्रविष्टि संख्या क्या है?*

#### 🇬🇧 English Response:
> Based on the provided context, the specific list of Scheduled Tribes you mentioned ('Kawar, Kanwar, Kaur, Cherwa, Rathia, Tanwar, Chattri') and its entry number are not available.
> 
> The context contains user manuals and official document templates for the Chhattisgarh government's social status certification process, but it does not include the official list of recognized Scheduled Tribes or their corresponding entry numbers in the state.
> 
> For the most accurate and up-to-date information on the list of Scheduled Tribes and their entry numbers, you may need to refer to the official government notifications or the state's official schedule.
> 
> For the service of Scheduled Caste/Scheduled Tribe Certificate, the department is the Revenue & Disaster Management Department.

*Latency: 16.10 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 18.54 seconds*

---

### Q33: For which specific districts is the tribe 'Dhulia, Paiko, Putiya' recognized under entry 35 of Andhra Pradesh Scheduled Tribes?

**Hindi Version:** *आंध्र प्रदेश अनुसूचित जनजाति की प्रविष्टि 35 के तहत 'धूलिया, पैको, पुतिया' जनजाति को किन विशिष्ट जिलों के लिए मान्यता दी गई है?*

#### 🇬🇧 English Response:
> Based on the provided context, the tribe 'Dhulia, Paiko, Putiya' is recognized under entry 35 of the Andhra Pradesh Scheduled Tribes list. The specific districts where this tribe is recognized are:
> 
> 1.  **Bhimtal**
> 2.  **Kausani**
> 3.  **Munsiyari**
> 4.  **Pithoragarh**
> 
> These districts are listed in the context as part of the entry for the tribe 'Dhulia, Paiko, Putiya'.
> 
> Information not available.

*Latency: 6.46 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 13.11 seconds*

---

### Q34: Is 'Sahariya, Saharia, Seharia, Sehria, Sosia, Sor' recognized as a Scheduled Tribe in Chhattisgarh, and under which entry number?

**Hindi Version:** *क्या छत्तीसगढ़ में 'सहरिया, सहारिया, सेहारिया, सेहरिया, सोसिया, सोर' को अनुसूचित जनजाति के रूप में मान्यता प्राप्त है, और किस प्रविष्टि संख्या के तहत?*

#### 🇬🇧 English Response:
> Based on the provided context, the answer is:
> 
> No, 'Sahariya, Saharia, Seharia, Sehria, Sosia, Sor' is not explicitly listed as a recognized Scheduled Tribe in the provided documents. The documents mention specific castes and tribes, such as 'Scheduled Castes/Scheduled Tribes and Other Backward Classes (Regulation of Social Status Certification) Act, 2013', but do not provide a comprehensive list of all recognized Scheduled Tribes in Chhattisgarh.
> 
> The context does not specify an entry number for these names. The documents primarily focus on the process and format for issuing Social Status Certificates for Scheduled Castes/Scheduled Tribes and Other Backward Classes, rather than listing the specific tribes themselves.
> 
> Information not available.

*Latency: 4.71 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 31.26 seconds*

---

## 5. Social Status Act (Caste Certificate Rules)

### Q35: Under the Chhattisgarh Social Status Certification Act 2013, on whom does the burden of proof lie to establish caste status?

**Hindi Version:** *छत्तीसगढ़ सामाजिक प्रास्थिति प्रमाणीकरण अधिनियम 2013 के तहत, जाति की प्रास्थिति साबित करने के लिए सबूत का भार किस पर होता है?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 25.55 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ सामाजिक प्रास्थिति प्रमाणीकरण अधिनियम 2013 के अनुसार, जाति की प्रास्थिति साबित करने का सबूत का भार अधिनियम के तहत गठित प्राधिकारियों पर होता है। इन प्राधिकारियों, जैसे जिला स्तरीय प्रमाणपत्र सत्यापन समिति या उच्च शक्ति प्रमाणीकरण छानबीन समिति, के पास दीवानी न्यायालय की शक्तियां होती हैं। इसका अर्थ है कि यदि सामाजिक प्रास्थिति प्रमाणपत्र पर कोई विवाद होता है, तो इन प्राधिकारियों के पास दावे की सत्यता की जांच करने का अधिकार होता है।
> 
> यह सेवा राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की जाती है।

*Latency: 16.65 seconds*

---

### Q36: What are the minimum and maximum terms of imprisonment and fine for a person who obtains a false caste certificate under Section 10(1)?

**Hindi Version:** *धारा 10(1) के तहत झूठा जाति प्रमाण पत्र प्राप्त करने वाले व्यक्ति के लिए कारावास और जुर्माने की न्यूनतम और अधिकतम अवधि क्या है?*

#### 🇬🇧 English Response:
> Based on the provided context, for a person who obtains a false Social Status Certificate, the penalties are as follows:
> 
> *   **Imprisonment:** Rigorous imprisonment for a minimum of three months, which can extend up to two years.
> *   **Fine:** A fine ranging from a minimum of two thousand rupees to a maximum of twenty thousand rupees.
> 
> This information is from the Chhattisgarh government's user manual for the Scheduled Caste/Tribe Certificate service, managed by the Revenue and Disaster Management Department.

*Latency: 12.84 seconds*

#### 🇮🇳 Hindi Response:
> धारा 10(1) के अनुसार, यदि कोई व्यक्ति झूठा जाति प्रमाण पत्र प्राप्त करता है, तो उसे निम्नलिखित दंड का सामना करना पड़ सकता है:
> 
> *   **कारावास:** कठोर कारावास, जिसकी अवधि **तीन माह से कम नहीं** होगी, लेकिन **दो वर्ष तक** का हो सकेगा।
> *   **जुर्माना:** जुर्माना, जो **दो हजार रुपये से कम नहीं** होगा और **बीस हजार रुपये तक** का हो सकता है।
> 
> यह दंड राजस्व एवं आपदा प्रबंधन विभाग द्वारा जारी अनुसूचित जाति/जनजाति और अन्य पिछड़ा वर्ग प्रमाण पत्र के लिए है।

*Latency: 19.75 seconds*

---

### Q37: Under Section 11 of the 2013 Act, are the offenses under Section 10 cognizable and bailable?

**Hindi Version:** *2013 के अधिनियम की धारा 11 के तहत, क्या धारा 10 के तहत अपराध संज्ञेय और जमानतीय हैं?*

#### 🇬🇧 English Response:
> दिए गए संदर्भ के आधार पर, यद्यपि प्रश्न में "धारा 11" का उल्लेख है, किंतु दस्तावेज़ में "धारा 10" के अंतर्गत आने वाले अपराधों के संबंध में जानकारी दी गई है।
> 
> संदर्भ के अनुसार, धारा 10 के अंतर्गत अपराध **संज्ञेय (cognizable) और गैर-जमानती (non-bailable)** हैं।
> 
> पाठ में उल्लेख है: "इस अधिनियम के अंतर्गत दंडनीय अपराधों को संज्ञेय, गैर-जमानती और संक्षिप्त रूप में विचारण योग्य (may be tried summarily) माना जाएगा।"
> 
> यह जानकारी **राजस्व एवं आपदा प्रबंधन विभाग** के अंतर्गत **अनुसूचित जाति/जनजाति प्रमाण पत्र** सेवा से संबंधित है।

*Latency: 12.40 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, 2013 के अधिनियम की धारा 11 के अनुसार, धारा 10 के तहत अपराध संज्ञेय और जमानत योग्य हैं।
> 
> अधिनियम की धारा 11 में स्पष्ट रूप से कहा गया है: "दण्ड प्रक्रिया संहिता, १९७३ में अंतर्विष्ट किसी बात के होते हुए भी, इस अधिनियम की धारा १० के अधीन दण्डनीय किसी अपराध का... संज्ञान नहीं लेगा।"
> 
> इसका अर्थ है कि धारा 10 के तहत दंडनीय अपराधों को संज्ञेय (पुलिस बिना वारंट के गिरफ्तार कर सकती है), जमानत योग्य (अभियुक्त को जमानत का अधिकार है) और संक्षिप्त विचारण योग्य माना जाएगा।
> 
> यह सेवा राजस्व एवं आपदा प्रबंधन विभाग के अंतर्गत आती है।

*Latency: 17.07 seconds*

---

### Q38: Can a court take cognizance of a false certificate issued by a Competent Authority under Section 12 without government approval?

**Hindi Version:** *क्या कोई न्यायालय सरकार की मंजूरी के बिना धारा 12 के तहत सक्षम प्राधिकारी द्वारा जारी किए गए झूठे प्रमाण पत्र का संज्ञान ले सकता है?*

#### 🇬🇧 English Response:
> Based on the provided context, the answer is not clear-cut as the documents contain conflicting information. The text describes the penalty for issuing a false certificate under Section 12, but the process for a court to take cognizance is mentioned in other sections.
> 
> One part of the context states that a court can take cognizance of an offence "except upon 0 complaint, in writing made by the High Power Certification Scrutiny Committee". This would not require direct government approval.
> 
> However, another part of the same context states that a court can take cognizance "except with the previous sanction of the Government".
> 
> Therefore, while the context allows for the possibility of a court taking cognizance without direct government approval (via a complaint from the Committee), it also explicitly requires government approval in another instance. The provided documents are contradictory on this specific point.
> 
> Information not available.

*Latency: 21.39 seconds*

#### 🇮🇳 Hindi Response:
> नहीं, court ऐसी case khud se नहीं ले सकता।
> 
> दिए गए context के अनुसार, Section 12 के under, कोई भी court इस offence का संज्ञान तब तक नहीं लेगा जब तक कि High Level Verification और Scrutiny Committee या उनके द्वारा अधिकृत किसी व्यक्ति द्वारा लिखित शिकायत न की जाए।
> 
> इसका मतलब है कि court का action government के approval (committee के through) के बिना possible नहीं है। Committee को पहले case की जांच करनी होगी और फिर court में शिकायत भेजनी होगी।
> 
> यह process Revenue & Disaster Management Department द्वारा handle किया जाता है।

*Latency: 24.52 seconds*

---

### Q39: What is the time limit for an applicant to file an appeal against the rejection of a caste certificate, and how long does the appellate authority have to decide?

**Hindi Version:** *जाति प्रमाण पत्र की अस्वीकृति के खिलाफ अपील दायर करने की समय सीमा क्या है, और अपीलीय प्राधिकारी के पास निर्णय लेने के लिए कितना समय होता है?*

#### 🇬🇧 English Response:
> प्रदत्त संदर्भ के आधार पर, अपीलीय प्राधिकरण (Appellate Authority) के पास निर्णय लेने के लिए तीन महीने की अवधि होती है।
> 
> हालाँकि, संदर्भ में उस समय सीमा (time limit) का उल्लेख नहीं है जिसके भीतर आवेदक को अस्वीकृति के विरुद्ध अपील दायर करनी चाहिए।
> 
> सूचना उपलब्ध नहीं है।

*Latency: 12.11 seconds*

#### 🇮🇳 Hindi Response:
> जाति प्रमाण पत्र की अस्वीकृति के विरुद्ध अपील दायर करने की समय सीमा और अपीलीय प्राधिकारी द्वारा निर्णय लेने की समय सीमा के बारे में दी गई जानकारी में स्पष्ट रूप से नहीं बताया गया है।
> 
> संदर्भ के अनुसार, आवेदन जमा करने के 22 कार्य दिवसों के भीतर प्रमाण पत्र अस्वीकृत कर दिए जाते हैं, और विभिन्न प्रमाण पत्रों के लिए अपीलीय प्राधिकारी का विवरण भी उपलब्ध है (जैसे SC/ST प्रमाण पत्र के लिए कलेक्टर, स्थायी जाति प्रमाण पत्र के लिए कमिश्नर)।
> 
> जानकारी उपलब्ध नहीं है।
> सेवा का नाम: जाति प्रमाण पत्र। विभाग: राजस्व एवं आपदा प्रबंधन विभाग।

*Latency: 14.04 seconds*

---

### Q40: Within what time frame must the District Level Certificate Verification Committee report its findings to an employer or educational institution under Section 6(2)?

**Hindi Version:** *धारा 6(2) के तहत जिला स्तरीय प्रमाणपत्र सत्यापन समिति को नियोक्ता या शैक्षणिक संस्थान को अपने निष्कर्षों की रिपोर्ट कितने समय में देनी होगी?*

#### 🇬🇧 English Response:
> Based on the provided context, the District Level Certificate Verification Committee must report its findings to an employer or educational institution within one month.
> 
> This requirement applies when the committee receives a reference from such an entity for the verification of a Social Status Certificate. The report must be submitted within one month from the date the committee receives the reference.
> 
> This process is governed by the Revenue & Disaster Management Department.

*Latency: 12.72 seconds*

#### 🇮🇳 Hindi Response:
> जिला स्तरीय प्रमाणपत्र सत्यापन समिति के लिए यह अनिवार्य है कि वह अपने निष्कर्षों की रिपोर्ट नियोक्ता, शैक्षणिक संस्थान या संबंधित प्राधिकरण को संदर्भ प्राप्त होने की तारीख से एक महीने के भीतर सूचित करे।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की गई है।

*Latency: 13.31 seconds*

---

### Q41: According to Section 4(2) of the Act, what is the validity period of a social status certificate issued by the Competent Authority?

**Hindi Version:** *अधिनियम की धारा 4(2) के अनुसार सक्षम प्राधिकारी द्वारा जारी सामाजिक प्रास्थिति प्रमाणपत्र की वैधता अवधि क्या है?*

#### 🇬🇧 English Response:
> According to the provided context, a Social Status Certificate issued by the Competent Authority has a permanent validity.
> 
> The document states: "A Social Status Certificate issued by the Competent Authority under sub-section (l ) of this Section, shall be a document of permanent nature, the validity of which shall not be limited by time."
> 
> This information pertains to the 'Scheduled Caste/Tribe Certificate (ID: 4)' service under the 'Revenue and Disaster Management Department'.

*Latency: 14.71 seconds*

#### 🇮🇳 Hindi Response:
> सक्षम प्राधिकारी द्वारा जारी सामाजिक प्रास्थिति प्रमाणपत्र की वैधता अवधि समय द्वारा सीमित नहीं है। यह एक स्थायी प्रकृति का दस्तावेज है। यह सेवा राजस्व एवं आपदा प्रबंधन विभाग द्वारा संचालित की जाती है।

*Latency: 12.76 seconds*

---

### Q42: Under what condition can a duplicate social status certificate be issued to an applicant according to Section 4(2)?

**Hindi Version:** *धारा 4(2) के अनुसार आवेदक को किस स्थिति में डुप्लीकेट सामाजिक प्रास्थिति प्रमाण पत्र जारी किया जा सकता है?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 41.84 seconds*

#### 🇮🇳 Hindi Response:
> आवेदक को डुप्लीकेट सामाजिक प्रास्थिति प्रमाण पत्र तब जारी किया जा सकता है जब वह मूल प्रमाण पत्र खो जाने की घोषणा करता है।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग की सेवा से संबंधित है।

*Latency: 16.64 seconds*

---

### Q43: If a social status certificate is cancelled under Section 8, what happens to the degrees or diplomas earned using that certificate according to Section 9(4)?

**Hindi Version:** *यदि धारा 8 के तहत सामाजिक प्रास्थिति प्रमाणपत्र रद्द कर दिया जाता है, तो धारा 9(4) के अनुसार उस प्रमाणपत्र का उपयोग करके प्राप्त की गई डिग्री या डिप्लोमा का क्या होता है?*

#### 🇬🇧 English Response:
> According to Section 9(4) of the provided context, if a social status certificate is cancelled under Section 8, any degree, diploma, or other educational qualification acquired by a person by obtaining admission against a reserved seat in an educational institution on the basis of that cancelled certificate "shall be deemed to have been cancelled and never been awarded."
> 
> This means the educational qualification is considered invalid and as if it was never obtained.
> 
> This information is available in the provided context for services like Other Backward Class (OBC) Certificate and Scheduled Caste/Tribe Certificate. The department for these services is the Revenue and Disaster Management Department.
> 
> Service: Other Backward Class (OBC) Certificate / Scheduled Caste/Tribe Certificate
> Department: Revenue and Disaster Management Department

*Latency: 9.44 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 27.25 seconds*

---

### Q44: What is the consequence if a person is elected to a local authority or constitutional body based on a caste certificate that is later cancelled under Section 8?

**Hindi Version:** *यदि कोई व्यक्ति ऐसे जाति प्रमाण पत्र के आधार पर स्थानीय प्राधिकरण या संवैधानिक निकाय के लिए चुना जाता है जिसे बाद में धारा 8 के तहत रद्द कर दिया जाता है, तो इसका क्या परिणाम होता है?*

#### 🇬🇧 English Response:
> Based on the provided context, if a person is elected to a local authority or any other statutory body based on a caste certificate that is later cancelled under Section 8, they will be disqualified.
> 
> The consequence is that the person is disqualified from being a member of such local authority, cooperative society, or any other statutory body or institution from the date the certificate is cancelled. Furthermore, the reserved seat they held is deemed to have fallen vacant immediately.
> 
> This information applies to both the Other Backward Class (OBC) certificate and the Scheduled Caste/Scheduled Tribe (SC/ST) certificate services, which are managed by the Revenue and Disaster Management Department of Chhattisgarh.

*Latency: 12.61 seconds*

#### 🇮🇳 Hindi Response:
> यदि किसी व्यक्ति को जाति प्रमाण पत्र के आधार पर स्थानीय प्राधिकरण या संवैधानिक निकाय के लिए चुना जाता है, जिसे बाद में धारा 8 के तहत रद्द कर दिया जाता है, तो उस प्रमाण पत्र के निरस्तीकरण को उस तिथि से उस निकाय के सदस्य के रूप में उनकी स्थिति समाप्त होने के रूप में माना जाता है।
> 
> इसका अर्थ यह है कि जिस आरक्षित सीट पर वे चुने गए थे, उसे उसी समय रिक्त माना जाता है।
> 
> यह जानकारी राजस्व एवं आपदा प्रबंधन विभाग द्वारा प्रदान की गई है।

*Latency: 11.44 seconds*

---

## 6. Ordinary Gazette Notification for Name Change

### Q45: What is the fee and challan head for name change publication in the ordinary gazette?

**Hindi Version:** *साधारण राजपत्र में नाम परिवर्तन प्रकाशन के लिए शुल्क और चालान हेड क्या है?*

#### 🇬🇧 English Response:
> Jaankari uplabd nahi hai.

*Latency: 8.65 seconds*

#### 🇮🇳 Hindi Response:
> साधारण राजपत्र में नाम परिवर्तन के लिए शुल्क 30.0 रुपये है।
> 
> चालान के लिए हेड 0058 – मुद्रण तथा लेखन सामग्री, 102 – राजपत्र आदि के प्रकाशन एवं अन्य प्रातियां है।
> 
> सेवा सेतु केंद्र, शासकीय मुद्रण एवं लेखन सामग्री विभाग, सेवा सेतु पोर्टल।

*Latency: 17.31 seconds*

---

### Q46: What are the required documents to apply for Ordinary Gazette Notification for Name Change?

**Hindi Version:** *नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना के लिए आवेदन करने के लिए आवश्यक दस्तावेज क्या हैं?*

#### 🇬🇧 English Response:
> To apply for the Ordinary Gazette Notification for Name Change, you need to provide the following required documents:
> 
> 1.  **Original Copy of a Challan of ₹ 430/-**: This must be from any branch of the State Bank of India, specifically under the head '0058 Printing And Stationery, 102 Publication Of Gazette, Etc., And Other Receipts'. This document is mandatory.
> 
> 2.  **Notarized Affidavit**: This should be in Form-III on a ₹ 50 Non-Judicial Stamp Paper, and it must not be more than 3 months old from the date of application. This is also mandatory.
> 
> 3.  **Original Copy of the Publication of the Notice for Name Change**: This should be in Form-I and must be in a local newspaper, not more than 3 months old from the date of application. This is mandatory.
> 
> 4.  **Original Copy of the Deed Form in Form-II**: This must include the names, signatures, and addresses of 02 witnesses. This is mandatory.
> 
> 5.  **Old Name & New Name Verification Document**: This is mandatory.
> 
> 6.  **All Types of Documents/Identity Cards/Ids Mentioned in the Affidavit**: This is mandatory.
> 
> 7.  **Identity Card of the Applicant**: This must be an identity card issued by the government. This is mandatory.
> 
> 8.  **Identity Card of Witnesses**: This must be an identity card issued by the government for the witnesses. This is mandatory.
> 
> You can apply for this service at a Sewa Setu Kendra or online through the official Sewa Setu portal. The online fee is ₹30.0.
> 
> For more details, you can visit the official specification page or the application form fields.
> 
> Information not available.

*Latency: 8.21 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 44.89 seconds*

---

### Q47: How old can the notarized affidavit and newspaper notice be for the name change gazette application?

**Hindi Version:** *नाम परिवर्तन राजपत्र आवेदन के लिए नोटरीकृत हलफनामा और समाचार पत्र का नोटिस कितना पुराना हो सकता है?*

#### 🇬🇧 English Response:
> Based on the provided context, for the Ordinary Gazette Notification for Name Change service, both the notarized affidavit and the newspaper notice should not be more than 03 months old from the date of application.
> 
> This information is specified in the required documents list for the service.
> 
> This information is for the Ordinary Gazette Notification for Name Change service under the Government Printing and Stationery Department.

*Latency: 13.31 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन राजपत्र आवेदन के लिए, नोटरीकृत शपथ पत्र और समाचार पत्र का नोटिस, आवेदन की तारीख से 3 महीने से अधिक पुराना नहीं होना चाहिए।
> 
> यह जानकारी 'नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना' सेवा (ID: 201) से संबंधित है, जो शासकीय मुद्रण एवं लेखन सामग्री विभाग द्वारा प्रदान की जाती है।

*Latency: 26.51 seconds*

---

### Q48: Under which form number and stamp paper value should the notarized affidavit be submitted for a name change?

**Hindi Version:** *नाम परिवर्तन के लिए नोटरीकृत हलफनामा किस फॉर्म संख्या और स्टांप पेपर मूल्य के तहत जमा किया जाना चाहिए?*

#### 🇬🇧 English Response:
> Based on the provided context, the notarized affidavit for a name change in the Sewa Setu Chhattisgarh portal should be submitted on a ₹50 non-judicial stamp paper. The specific form number is Form-III.
> 
> **Service:** Ordinary Gazette Notification for Name Change (ID: 201)
> **Department:** Government Printing and Stationery Department
> 
> **Required Documents:**
> - A Notarized Affidavit In Form-III On A ₹ 50 Non-Judicial Stamp Paper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Details of documents related to name change [Type: textarea, Data: Alfa Numeric] (Row: 17, Col: 1)
> 
> For the format of the affidavit, you can refer to the provided link: [https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf](https://sewasetu.cgstate.gov.in/resources/docFormat/23842.pdf)
> 
> Information not available.

*Latency: 6.88 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन के लिए नोटरीकृत हलफनामा प्ररूप-तीन (Form-iii) के प्रारूप में जमा करना होगा। यह 50 रू. के नॉन-ज्यूडिशियल स्टाम्प पेपर पर होना चाहिए, जो आवेदन की तारीख से 3 महीने से अधिक पुराना न हो। यह दस्तावेज़ अनिवार्य है।
> 
> सेवा: साधारण राजपत्र अधिसूचना (ID: 201), विभाग: शासकीय मुद्रण एवं लेखन सामग्री विभाग।

*Latency: 11.78 seconds*

---

### Q49: What is the processing time limit (SLA) for the Ordinary Gazette Notification for Name Change?

**Hindi Version:** *नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना के लिए प्रसंस्करण समय सीमा (SLA) क्या है?*

#### 🇬🇧 English Response:
> The processing time limit (SLA) for the Ordinary Gazette Notification for Name Change (ID: 201) is 29 days.

*Latency: 11.08 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना के लिए प्रसंस्करण समय सीमा 29 दिन है। यह सेवा 'साधारण राजपत्र अधिसूचना के लिए नाम परिवर्तन' (ID: 201) है, जो 'शासकीय मुद्रण एवं लेखन सामग्री विभाग' द्वारा प्रदान की जाती है।

*Latency: 10.31 seconds*

---

### Q50: Which department is responsible for issuing the Ordinary Gazette Notification for Name Change?

**Hindi Version:** *नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना जारी करने के लिए कौन सा विभाग जिम्मेदार है?*

#### 🇬🇧 English Response:
> The Ordinary Gazette Notification for Name Change is handled by the Government Printing and Stationery Department. The service ID for this is 201.

*Latency: 10.19 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन के लिए साधारण राजपत्र अधिसूचना जारी करने के लिए जिम्मेदार विभाग **शासकीय मुद्रण एवं लेखन सामग्री विभाग** है।
> 
> सेवा: साधारण राजपत्र अधिसूचना, विभाग: शासकीय मुद्रण एवं लेखन सामग्री विभाग।

*Latency: 21.16 seconds*

---

### Q51: Is the publication of the name change notice required in a local newspaper, and which form is used for it?

**Hindi Version:** *क्या स्थानीय समाचार पत्र में नाम परिवर्तन नोटिस का प्रकाशन आवश्यक है, और इसके लिए किस फॉर्म का उपयोग किया जाता है?*

#### 🇬🇧 English Response:
> Based on the provided context, the publication of the name change notice in a local newspaper is required for the "Ordinary Gazette Notification for Name Change" service.
> 
> The required form for this publication is **Form-I**.
> 
> The context specifies that the original copy of the publication of the notice for name change in Form-I in a local newspaper (should not be more than 3 months old from the date of application) is a mandatory document.
> 
> **Service:** Ordinary Gazette Notification for Name Change (ID: 201)
> **Department:** Government Printing and Stationery Department
> **Time Limit / SLA:** 29 Days
> 
> You can apply for this service at a Sewa Setu Kendra or online through the provided link.
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Notice For Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field: Change Type [Type: drop down, Data: Alfa Numeric] (Row: 3, Col: 1)
> 
> **Required Documents:**
> - SNo 3: The Original Copy Of The Publication Of The Name Change In Form-I In A Local Newspaper (Should Not Be More Than 03 Months Old From The Date Of Application). (Mandatory: Yes)
> 
> **Application Form Fields:**
> - Field: Language of publication of notification [Type: drop down, Data: Alfa Numeric] (Row: 2, Col: 1)
> - Field

*Latency: 43.20 seconds*

#### 🇮🇳 Hindi Response:
> हाँ, स्थानीय समाचार पत्र में नाम परिवर्तन नोटिस का प्रकाशन आवश्यक है। इसके लिए फॉर्म-I (प्ररूप-एक) का उपयोग किया जाता है।
> 
> यह सेवा 'साधारण राजपत्र अधिसूचना' है, जो 'शासकीय मुद्रण एवं लेखन सामग्री विभाग' द्वारा प्रदान की जाती है।

*Latency: 13.28 seconds*

---

### Q52: What form is used for the deed of name change and how many witnesses are required?

**Hindi Version:** *नाम परिवर्तन के विलेख (deed) के लिए किस फॉर्म का उपयोग किया जाता है और कितने गवाहों की आवश्यकता होती है?*

#### 🇬🇧 English Response:
> Based on the provided context, the deed form for a name change is referred to as "Form-Ii" and requires **02 witnesses**.
> 
> The required documents section for the "Ordinary Gazette Notification for Name Change" service lists:
> - SNo 4: The Original Copy Of The Deed Form In Form-Ii With The Names, Signatures And Addresses Of 02 Witnesses. (Mandatory: Yes)
> 
> The application form also includes a field for "Son/Daughter Name (after change) in Hindi" and "Son/Daughter Name (after change) in English" which would be part of the deed, but the specific requirement for witnesses is clearly stated as 2.
> 
> Information not available.

*Latency: 9.95 seconds*

#### 🇮🇳 Hindi Response:
> नाम परिवर्तन के विलेख के लिए फॉर्म-II का उपयोग किया जाता है। इसमें 2 गवाहों की आवश्यकता होती है।
> 
> यह जानकारी 'साधारण गजट सूचना (नाम परिवर्तन)' सेवा से संबंधित है।

*Latency: 14.26 seconds*

---

## 7. Out of Scope Queries

### Q53: How do I apply for a new passport in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में नया पासपोर्ट आवेदन कैसे करें?*

#### 🇬🇧 English Response:
> To apply for a new passport in Chhattisgarh, you need to follow the process outlined by the concerned government department. The provided context does not contain specific information about passport applications. Therefore, I am unable to provide details on how to apply for a new passport.
> 
> Information not available.

*Latency: 6.54 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में नया पासपोर्ट आवेदन करने के लिए, आपको नीचे दिए गए चरणों का पालन करना होगा:
> 
> 1. **ई-निस्ट्रिक्ट पोर्ाल पर पंजीयन:**
>    - अपने कंप्यूटर या लैपटॉप में ब्राउज़र खोलें और `cgedistrict.cgstate.gov.in` टाइप करें।
>    - होमपेज खुलेगा, जहाँ "ई-डिस्ट्रिक्ट पोटटल" पर क्लिक करें।
>    - "इलेक्ट्रॉनिक रजिस्ट्रेशन" बटन पर क्लिक करके नया पंजीकरण करें।
> 
> 2. **पंजीकरण के बाद लॉगिन:**
>    - पंजीकरण के बाद, आपको एक पासवर्ड प्राप्त होगा, जो आपके पंजीकृत मोबाइल नंबर पर भेजा जाएगा।
>    - इस पासवर्ड की सहायता से आप लॉगिन कर सकते हैं।
> 
> 3. **आवेदन प्रक्रिया:**
>    - लॉगिन करने के बाद, "मूल निवासी प्रमाण पत्र" सेवा का चयन करें।
>    - चरण 1: ई-निस्ट्रिक्ट पोर्ाल पर पंजीयन करें।
>    - चरण 2: पंजीक त यूज़र लॉक्रगि करें।
>    - चरण 5: मूल निवतसी प्रमतण पत्र के र्लए आवेदि करें।
>    - चरण 6: आवश्यक दस्ततवेज़ अपलोि करित।
>    - चरण 7: पूवतावलोकि और आवेदि जमत करित।
>    - चरण 8: शुल्क कत भुगर्ति।
>    - चरण 9: पतवर्ी सुरक्षिर् रखित।
>    - चरण 10: आवेदि की स्थिवर् देखित।
> 
> 4. **शुल्क:**
>    - पासपोर्ट आवेदन के लिए ऑनलाइन शुल्क ₹30.0 है।
> 
> 5. **संपर्क:**
>    - सेवा सेतु केंद्र से संपर्क किया जा सकता है।
> 
> यह जानकारी Sewa Setu Chhattisgarh पोर्टल के आधिकारिक विनिर्देशों पर आधारित है।

*Latency: 7.81 seconds*

---

### Q54: What is the procedure to get a new driving license in Raipur?

**Hindi Version:** *रायपुर में नया ड्राइविंग लाइसेंस प्राप्त करने की प्रक्रिया क्या है?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 4.40 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 10.96 seconds*

---

### Q55: How to apply for a voter ID card online?

**Hindi Version:** *ऑनलाइन वोटर आईडी कार्ड के लिए आवेदन कैसे करें?*

#### 🇬🇧 English Response:
> To apply for a voter ID card online, you can use the official portal provided by the Election Commission of India. Here's how you can do it:
> 
> 1.  **Visit the Official Portal**: Go to the Election Commission of India's website: [https://www.elections.gov.in/](https://www.elections.gov.in/).
> 
> 2.  **Navigate to the Voter ID Section**: Look for the "Voter Services" or "Voter ID" section on the website.
> 
> 3.  **Find the Online Application Form**: Search for the option to apply for a new voter ID or update your existing details.
> 
> 4.  **Fill in the Application Form**: You will need to provide your personal details, such as:
>     *   Your full name
>     *   Date of birth
>     *   Address
>     *   Gender
>     *   Aadhaar number (if applicable)
> 
> 5.  **Upload Required Documents**: You will need to upload scanned copies of documents like:
>     *   Proof of address (e.g., utility bills, rent agreement)
>     *   Proof of age (e.g., birth certificate, school leaving certificate)
>     *   Aadhaar card (if you have one)
> 
> 6.  **Pay the Application Fee**: The fee for a new voter ID card is typically ₹25, but it can vary. You can pay the fee online using methods like debit card, credit card, or net banking.
> 
> 7.  **Submit and Track**: After submitting the form, you can track the status of your application online.
> 
> **Important Note**: The process and fees might vary slightly depending on your state. For Chhattisgarh, the Sewa Setu portal is used for various services, but the voter ID application is typically handled by the Election Commission.
> 
> If you need more specific details for Chhattisgarh, you can contact the Sewa Setu Kendra or the Election Commission's helpline.
> 
> For more information, you can visit the official Election Commission of India website.
> 
> **Service Name**: Voter ID Card Application
> **Department**: Election Commission of India
> 
> Information not available.

*Latency: 10.47 seconds*

#### 🇮🇳 Hindi Response:
> ऑनलाइन वोटर आईडी कार्ड के लिए आवेदन करने के लिए, आपको Sewa Setu Chhattisgarh पोर्टल पर जाना होगा।
> 
> **आवेदन प्रक्रिया:**
> 
> 1.  **पोर्टल पर जाएं:** आप https://sewasetu.cgstate.gov.in/home?lang=en पर जा सकते हैं।
> 2.  **लॉग-इन करें:** अपने Sewa Setu खाते में लॉग-इन करें।
> 3.  **सेवा चुनें:** "वोटर आईडी कार्ड" सेवा चुनें।
> 4.  **आवेदन भरें:** ऑनलाइन फॉर्म में सभी आवश्यक विवरण भरें।
> 5.  **दस्तावेज़ अपलोड करें:** आवश्यक दस्तावेज़ों की स्कैन की गई प्रतियां अपलोड करें।
> 6.  **सबमिट करें:** आवेदन जमा करें।
> 
> **आवश्यक दस्तावेज़:**
> 
> - जन्म प्रमाण पत्र
> - पते का प्रमाण (जैसे बिजली बिल, राशन कार्ड)
> - फोटो (पासपोर्ट आकार)
> - फॉर्म 6 (वोटर पंजीकरण फॉर्म)
> 
> **शुल्क:**
> 
> - ऑनलाइन शुल्क ₹30.0 है।
> 
> **समय सीमा:**
> 
> - सेवा 7 दिनों के भीतर प्रदान की जाएगी।
> 
> अधिक जानकारी के लिए आप Sewa Setu हेल्पलाइन से संपर्क कर सकते हैं।

*Latency: 8.75 seconds*

---

### Q56: What is the application fee for a birth certificate in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में जन्म प्रमाण पत्र के लिए आवेदन शुल्क क्या है?*

#### 🇬🇧 English Response:
> The application fee for a birth certificate in Chhattisgarh is ₹30.0.
> 
> This fee applies whether you apply through the Sewa Setu Kendra or online.
> 
> For more details, you can visit the official portal: https://sewasetu.cgstate.gov.in/home?lang=en
> 
> Information not available.

*Latency: 6.63 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 14.13 seconds*

---

### Q57: How can I register a company or start a new business in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में कंपनी का पंजीकरण कैसे करें या नया व्यवसाय कैसे शुरू करें?*

#### 🇬🇧 English Response:
> Based on the provided context, I'm unable to answer your question about registering a company or starting a new business in Chhattisgarh. The context contains information about marriage registration, and certificates for Scheduled Castes/Scheduled Tribes and Other Backward Classes, but does not include any details about company registration or business setup processes.
> 
> Information not available.

*Latency: 6.35 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में कंपनी का पंजीकरण करने या नया व्यवसाय शुरू करने के लिए, आपको निम्नलिखित चरणों का पालन करना होगा:
> 
> 1. **कंपनी पंजीकरण के लिए:**
>    - **कंपनी अधिनियम, 2013** के तहत कंपनी का पंजीकरण करें।
>    - **निगमन प्रमाणपत्र (Certificate of Incorporation)** प्राप्त करें।
>    - **PAN कार्ड** और **GST पंजीकरण** प्राप्त करें।
>    - **बैंक खाता** खोलें।
> 
> 2. **व्यवसाय शुरू करने के लिए:**
>    - **व्यवसाय पंजीकरण (Udyam Registration)** करें।
>    - **GST पंजीकरण** करें।
>    - **ट्रेड लाइसेंस** प्राप्त करें।
>    - **श्रम पंजीकरण** (यदि आवश्यक हो) करें।
> 
> **महत्वपूर्ण जानकारी:**
> - कंपनी पंजीकरण के लिए **कंपनी रजिस्ट्रार (RoC)** से संपर्क करें।
> - व्यवसाय शुरू करने के लिए **नगरीय प्रशासन और विकास विभाग** से संपर्क करें।
> 
> **सेवा का नाम:** कंपनी पंजीकरण एवं व्यवसाय प्रारंभ करना
> **विभाग:** नगरीय प्रशासन एवं विकास विभाग
> 
> जानकारी उपलब्ध नहीं है।

*Latency: 8.53 seconds*

---

### Q58: What are the rules and guidelines for traffic violations in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में यातायात उल्लंघन के क्या नियम और दिशा-निर्देश हैं?*

#### 🇬🇧 English Response:
> Information not available.

*Latency: 5.75 seconds*

#### 🇮🇳 Hindi Response:
> जानकारी उपलब्ध नहीं है।

*Latency: 12.59 seconds*

---

### Q59: How do I check my PF balance or EPF claim status in Chhattisgarh?

**Hindi Version:** *छत्तीसगढ़ में मैं अपना पीएफ बैलेंस या ईपीएफ दावा स्थिति कैसे जांचूं?*

#### 🇬🇧 English Response:
> To check your PF balance or EPF claim status in Chhattisgarh, you can use the following methods:
> 
> 1. **Online Method**:
>    - Visit the official EPFO portal (epfindia.gov.in).
>    - Log in with your UAN (Universal Account Number) and password.
>    - Check your balance or claim status under the relevant sections.
> 
> 2. **Offline Method**:
>    - Visit the nearest EPFO office in Chhattisgarh.
>    - Submit a written application for balance inquiry or claim status.
>    - Provide necessary documents like your UAN, ID proof, and address proof.
> 
> 3. **Mobile App**:
>    - Download the EPFO Member e-Sewa app.
>    - Log in with your UAN and password.
>    - Track your balance or claim status.
> 
> 4. **Missed Call Service**:
>    - Call the EPFO helpline number (1800-118-005) and follow the IVR instructions to check your balance.
> 
> 5. **SMS Service**:
>    - Send an SMS to 7738299899 with your UAN to receive your balance details.
> 
> **Note**: For specific details or assistance, you can contact the EPFO office in Chhattisgarh or visit the official EPFO website.
> 
> **Service**: Employee Provident Fund (EPF) Services  
> **Department**: Employee Provident Fund Organisation (EPFO)  
> **Contact**: 1800-118-005 (Helpline)  
> **Website**: epfindia.gov.in  
> 
> If you need further assistance, you can visit the EPFO office in Chhattisgarh or use the online methods mentioned above.

*Latency: 9.45 seconds*

#### 🇮🇳 Hindi Response:
> छत्तीसगढ़ में अपना पीएफ बैलेंस या ईपीएफ दावा स्थिति जांचने के लिए, आप आधिकारिक ई-डिस्ट्रिक्ट पोर्टल का उपयोग कर सकते हैं। यहाँ बताया गया है कि आप इसे कैसे कर सकते हैं:
> 
> 1. **ई-डिस्ट्रिक्ट पोर्टल पर जाएं**: अपने कंप्यूटर या लैपटॉप पर वेब ब्राउज़र में `cgedistrict.cgstate.gov.in` टाइप करें।
> 2. **लॉग इन करें**: होमपेज पर, "नागरिक लॉगिन" बटन पर क्लिक करें और अपने क्रेडेंशियल दर्ज करें।
> 3. **ई-डिस्ट्रिक्ट पोर्टल पर पंजीकरण करें**: यदि आप नए उपयोगकर्ता हैं, तो आपको "नागरिक पंजीकरण" प्रक्रिया का पालन करके पंजीकरण करना होगा।
> 4. **अपना बैलेंस या दावा स्थिति जांचें**: लॉग इन करने के बाद, आप अपने पीएफ बैलेंस या ईपीएफ दावा स्थिति की जांच करने के लिए संबंधित सेवा का चयन कर सकते हैं।
> 
> **नोट**: प्रदान किए गए संदर्भ में पीएफ बैलेंस या ईपीएफ दावा स्थिति की जांच के लिए विशिष्ट विवरण नहीं हैं। अधिक विस्तृत जानकारी के लिए, आप ई-डिस्ट्रिक्ट पोर्टल पर उपलब्ध सेवाओं की सूची देख सकते हैं या पोर्टल पर सहायता अनुभाग देख सकते हैं।
> 
> **सेवा का नाम**: ई-डिस्ट्रिक्ट पोर्टल
> **विभाग**: राजस्व और आपदा प्रबंधन विभाग
> 
> जानकारी उपलब्ध नहीं है।

*Latency: 8.80 seconds*

---

### Q60: What is the process to link Aadhaar card with my mobile number?

**Hindi Version:** *आधार कार्ड को अपने मोबाइल नंबर से लिंक करने की प्रक्रिया क्या है?*

#### 🇬🇧 English Response:
> To link your Aadhaar card with your mobile number, you can use the official Aadhaar linking process. Here's how it works:
> 
> 1.  **Visit the UIDAI Website**: Go to the official Aadhaar linking website: [https://uidai.gov.in/](https://uidai.gov.in/).
> 
> 2.  **Navigate to the Linking Section**: On the website, find and click on the "Aadhaar Linking" option.
> 
> 3.  **Enter Your Details**: You will need to provide:
>     *   Your 12-digit Aadhaar number.
>     *   The mobile number you want to link.
> 
> 4.  **Receive and Enter OTP**: An OTP (One-Time Password) will be sent to your registered mobile number. Enter this OTP to proceed.
> 
> 5.  **Complete the Linking**: After verifying your details, your mobile number will be linked to your Aadhaar.
> 
> **Important Note**: The process is straightforward and does not require any physical documents or visits to a service center. You can complete this online from the comfort of your home.
> 
> If you face any issues, you can contact the UIDAI helpline at 1947 for assistance.
> 
> For more details, you can also refer to the official UIDAI website.
> 
> **Service**: Aadhaar Linking
> **Department**: Unique Identification Authority of India (UIDAI)
> **Contact**: 1947
> 
> If you need further help, feel free to ask!

*Latency: 7.23 seconds*

#### 🇮🇳 Hindi Response:
> आधार कार्ड को मोबाइल नंबर से लिंक करने की प्रक्रिया:
> 
> आधार कार्ड को मोबाइल नंबर से लिंक करने के लिए आपको UIDAI की आधिकारिक वेबसाइट पर जाना होगा। इसके लिए:
> 
> 1. **UIDAI वेबसाइट पर जाएं**: `uidai.gov.in` पर जाएं।
> 2. **ई-आधार सेवा**: "My Aadhaar" अनुभाग में "Aadhaar Linking" विकल्प चुनें।
> 3. **मोबाइल नंबर दर्ज करें**: अपने आधार नंबर और मोबाइल नंबर डालें।
> 4. **OTP**: आपके मोबाइल पर OTP आएगा, उसे दर्ज करें।
> 5. **सत्यापन**: OTP के माध्यम से प्रक्रिया पूरी करें।
> 
> यह प्रक्रिया ऑनलाइन पूरी की जा सकती है। यदि आपको कोई समस्या आती है, तो आप UIDAI की हेल्पलाइन पर संपर्क कर सकते हैं।

*Latency: 15.11 seconds*

---

## Evaluation Summary & Metrics

- **Total Executed Queries:** 120
- **Total Time Taken:** 2724.91 seconds
- **Average Latency:** 22.71 seconds/query
