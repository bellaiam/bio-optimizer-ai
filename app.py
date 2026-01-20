import streamlit as st
import google.generativeai as genai
import plotly.graph_objects as go
import pdfplumber
import re

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Bio-Optimizer AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Bio-Optimizer AI")
st.subheader("Understand your lab results & get simple lifestyle guidance")

st.caption(
    "This tool explains lab results in plain language and suggests lifestyle improvements. "
    "It does NOT provide medical diagnosis or treatment."
)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    st.markdown("[Get a free Gemini API key](https://aistudio.google.com/app/apikey)")
    gemini_key = st.text_input("Your Gemini API Key", type="password")

    explanation_style = st.selectbox(
        "Explanation style",
        ["Plain & simple (recommended)", "More detailed"]
    )

    st.info(
        "Your API key is used only in your browser session. "
        "Each user uses their own free tier."
    )

# -----------------------------
# Biomarker definitions
# -----------------------------
BIOMARKERS = {
    "Metabolic Health (Blood Sugar & Insulin)": {
        "Fasting Glucose (mg/dL)": {"min": 70, "max": 90},
        "HbA1c (%)": {"min": 4.8, "max": 5.4},
        "Insulin (µIU/mL)": {"min": 2, "max": 8},
    },
    "Heart & Cholesterol Health": {
        "Total Cholesterol (mg/dL)": {"min": 140, "max": 190},
        "LDL (mg/dL)": {"min": 50, "max": 100},
        "HDL (mg/dL)": {"min": 50, "max": 90},
        "Triglycerides (mg/dL)": {"min": 50, "max": 100},
    },
    "Inflammation & Immune System": {
        "CRP (mg/L)": {"min": 0, "max": 1.0},
        "ESR (mm/hr)": {"min": 0, "max": 10},
        "WBC (10^9/L)": {"min": 4.0, "max": 9.0},
    },
}

flat_markers = [m for system in BIOMARKERS.values() for m in system]

# -----------------------------
# PDF Upload
# -----------------------------
st.markdown("## 📂 Step 1: Upload Lab Results (Optional)")
uploaded_file = st.file_uploader("Upload your lab PDF (tables not required)", type="pdf")

pdf_text = ""
pdf_numbers = {}

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pdf_text += text + "\n"

    for marker in flat_markers:
        pattern = re.compile(
            rf"{re.escape(marker)}\s*[:\n]?\s*(\d+(\.\d+)?)",
            re.IGNORECASE
        )
        match = pattern.search(pdf_text)
        if match:
            pdf_numbers[marker] = float(match.group(1))

    if pdf_numbers:
        st.success("✅ Lab values detected from PDF")
        st.write(pdf_numbers)
    else:
        st.warning("⚠️ No values detected — you can enter them manually below.")

# -----------------------------
# Manual Input
# -----------------------------
st.markdown("## 🧪 Step 2: Enter or Review Your Lab Values")

user_data = {}

for system, markers in BIOMARKERS.items():
    with st.expander(system, expanded=True):
        for marker, ref in markers.items():
            user_data[marker] = st.number_input(
                marker,
                value=pdf_numbers.get(marker, float(ref["min"])),
                step=0.1
            )

# -----------------------------
# Visualization
# -----------------------------
st.markdown("## 📊 Your Results vs Optimal Ranges")

user_vals = [user_data[m] for m in flat_markers]
optimal_mins = [
    BIOMARKERS[next(sys for sys in BIOMARKERS if m in BIOMARKERS[sys])][m]["min"]
    for m in flat_markers
]

fig = go.Figure()
fig.add_trace(go.Bar(name="Your Value", x=flat_markers, y=user_vals))
fig.add_trace(go.Bar(name="Optimal Minimum", x=flat_markers, y=optimal_mins))
fig.update_layout(
    height=500,
    barmode="group",
    xaxis_tickangle=-45
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# AI Analysis
# -----------------------------
st.markdown("## 🤖 Step 3: Get Your Personalized Explanation")

if st.button("Explain My Results 🚀", use_container_width=True):
    if not gemini_key:
        st.warning("Please enter your Gemini API key.")
    else:
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel("gemini-2.5-flash")

        if explanation_style == "Plain & simple (recommended)":
            tone = """
Use simple, everyday language.
Avoid medical jargon.
Explain what this means for daily life.
Focus on practical habits someone can actually do.
Be encouraging, not alarming.
"""
        else:
            tone = """
Use clear but slightly more detailed explanations.
Still avoid heavy medical terminology.
"""

        prompt = f"""
You are a friendly health coach.

{tone}

User lab results:
{user_data}

Optimal reference ranges:
{BIOMARKERS}

Optional lab context:
{pdf_text if pdf_text else "No PDF provided"}

Tasks:
1. Clearly explain which areas are not optimal.
2. Explain what this means in real life (energy, weight, heart health, inflammation).
3. Suggest practical lifestyle changes:
   - food choices
   - movement
   - sleep
   - stress
4. Use bullet points and short sections.
5. Do NOT diagnose or prescribe medication.
"""

        with st.spinner("Analyzing your results..."):
            response = model.generate_content(prompt)
            st.markdown("### 🧠 Your Health Explained")
            st.write(response.text)

st.divider()
st.caption("Educational use only. Always consult a healthcare professional for medical decisions.")
