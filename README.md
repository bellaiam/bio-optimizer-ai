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
