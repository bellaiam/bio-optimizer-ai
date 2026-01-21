# 🧬 Bio-Optimizer AI — an ML-powered data application that turns real-world lab PDFs into clear, actionable insights

Built to bridge **biomedical science** with **data engineering** and **machine learning**, focusing on messy data extraction, system-level analysis, and explainable AI.  

Turning complex lab results into clear, actionable health insights using AI.

---

## **About Bio-Optimizer AI**

**Bio-Optimizer AI** is a systems-based health analysis app that:

- Reads laboratory reports (PDFs)  
- Extracts biomarker values  
- Explains results in **plain, everyday language** — no medical background required  

This project bridges my background in biomedical science with my transition into data, ML, and software engineering, combining **domain expertise** with practical AI tooling.

---

## ✨ **What It Does**

- 📄 **Uploads lab reports in PDF format**  
- 🔍 **Automatically extracts biomarker values**  
- 📊 **Visualizes results** against optimal ranges  
- 🧠 Uses AI to explain:
  - What’s high or low  
  - Why it matters  
  - Simple, practical ways to improve  

**Focus:** education and prevention — *not diagnosis*

---

## 🧠 **Why This Project**

As a career changer moving from life sciences into tech, I wanted to build something that:

- Works with **messy, real-world data** (PDF parsing)  
- Requires **domain understanding**, not just coding skills  
- Demonstrates how **AI can simplify complex information**  
- Prioritizes **user-centered explanations** over medical jargon  

This project combines:

- Data extraction  
- Visualization  
- Prompt engineering  
- Systems thinking  

---

## 🛠 **Tech Stack**

- **Python**  
- **Streamlit** – interactive UI  
- **Plotly** – data visualizations  
- **pdfplumber** – PDF text extraction  
- **Regex-based parsing** – structured data extraction  
- **Google Gemini (LLM)** – explainability in plain language  

---

## 🧪 **Biomarker Systems Covered**

- Metabolic Health  
- Cardiovascular Health  
- Inflammation & Immune Response  

Each system is analyzed **individually** and **in relation to the others**.

---

## ⚠️ **Important Disclaimer**

This app is for **educational purposes only**.  
It does **not** provide medical diagnosis or treatment recommendations.

---

## 🔑 **Gemini API Key (Required)**

Bio-Optimizer AI uses **Google Gemini** to convert lab results into **clear, human-readable explanations**.  

To keep this project:

- Free to use  
- Secure  
- Independent of shared API limits  

👉 **Each user provides their own free Gemini API key**  

- The key is entered **locally** in the app  
- It is **not stored**  
- It is **not shared or logged**  

---

### ✅ **How to Get a Free Gemini API Key**

1. Go to **Google AI Studio**: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)  
2. Sign in with your **Google account**  
3. Click **“Create API Key”**  
4. Copy the generated key  

---

### 🔐 **How the App Uses the Key**

1. Start the app  
2. Paste your API key into the **sidebar input**  
3. Run the analysis  

No environment variables required.

---

### ❓ **Why Not Include an API Key by Default?**

Using a shared key would:  

- Risk hitting **free-tier limits**  
- Expose credentials **publicly**  
- Cause the app to **stop working for everyone**  

Requiring individual keys keeps the project:

- Reliable  
- Transparent  
- Safe for open-source use  

---

## 🚀 **How to Run Locally**

```bash
git clone https://github.com/your-username/bio-optimizer-ai.git
cd bio-optimizer-ai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

```
<img width="1246" height="685" alt="Screenshot 2026-01-20 at 10 30 36 AM" src="https://github.com/user-attachments/assets/07a6d9a9-ec19-4520-9bea-feb491c588c5" />

<img width="1254" height="687" alt="Screenshot 2026-01-20 at 10 28 07 AM" src="https://github.com/user-attachments/assets/a8f80679-e185-4467-9387-3f0ac6e3464a" />
<img width="1239" height="670" alt="Screenshot 2026-01-20 at 10 28 18 AM" src="https://github.com/user-attachments/assets/a56d2fa7-144d-4434-8a15-7988a4972e6b" />
<img width="1233" height="659" alt="Screenshot 2026-01-20 at 10 28 31 AM" src="https://github.com/user-attachments/assets/9fc55472-e237-487e-ad32-aa31314b0a0e" />
<img width="1253" height="694" alt="Screenshot 2026-01-20 at 10 28 46 AM" src="https://github.com/user-attachments/assets/a64f9942-2666-4521-90f9-24a4466a3b4c" />
<img width="1242" height="520" alt="Screenshot 2026-01-20 at 10 28 58 AM" src="https://github.com/user-attachments/assets/b391ee86-1a8b-4ce9-b283-9f21f76e19ab" />
<img width="1233" height="693" alt="Screenshot 2026-01-20 at 10 29 10 AM" src="https://github.com/user-attachments/assets/32a950fa-b56c-43ff-ba2f-e11fe3cbb27a" />
<img width="1266" height="652" alt="Screenshot 2026-01-20 at 10 29 23 AM" src="https://github.com/user-attachments/assets/ec90e385-e81e-489d-8c2a-c177dd2518df" />






