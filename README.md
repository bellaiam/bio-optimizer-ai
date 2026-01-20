🧬 Bio-Optimizer AI

Turning complex lab results into clear, actionable health insights using AI

Bio-Optimizer AI is a systems-based health analysis app that reads laboratory reports (PDFs), extracts biomarker values, and explains what they mean in plain, everyday language — without requiring a medical background.

This project bridges my background in biomedical science with my transition into data, machine learning, and software engineering, combining domain knowledge with practical AI tooling.

✨ What It Does

📄 Uploads lab reports in PDF format

🔍 Automatically extracts biomarker values

📊 Visualizes results against optimal ranges

🧠 Uses AI to explain:

What’s high or low

Why it matters

Simple, practical ways to improve

Focus: education and prevention — not diagnosis.

🧠 Why This Project

As a career changer moving from life sciences into tech, I wanted to build something that:

Works with messy, real-world data (PDF parsing)

Requires domain understanding, not just code

Demonstrates how AI can simplify complex information

Prioritizes user-centered explanations, not medical jargon

This project combines:

Data extraction

Visualization

Prompt engineering

Systems thinking

🛠 Tech Stack

Python

Streamlit – interactive UI

Plotly – visualizations

pdfplumber – PDF text extraction

Regex-based parsing – structured data extraction

Google Gemini (LLM) – explainability in plain language

🧪 Biomarker Systems Covered

Metabolic Health

Cardiovascular Health

Inflammation & Immune Response

Each system is analyzed individually and in relation to the others.

⚠️ Important Disclaimer

This app is for educational purposes only.
It does not provide medical diagnosis or treatment recommendations.

🔑 Gemini API Key (Required)

Bio-Optimizer AI uses Google’s Gemini AI to convert lab results into clear, human-readable explanations.

To keep this project:

Free to use

Secure

Independent of shared API limits

👉 Each user provides their own free Gemini API key.

The key is entered locally in the app

It is not stored

It is not shared or logged

✅ How to Get a Free Gemini API Key

Go to Google AI Studio
https://aistudio.google.com/app/apikey

Sign in with your Google account

Click “Create API Key”

Copy the generated key

🔐 How the App Uses the Key

Start the app

Paste your API key into the sidebar input

Run the analysis

No environment variables required.

❓ Why Not Include an API Key by Default?

Using a shared key would:

Risk hitting free-tier limits

Expose credentials publicly

Cause the app to stop working for everyone

Requiring individual keys keeps the project:

Reliable

Transparent

Safe for open-source use

🚀 How to Run Locally
git clone https://github.com/your-username/bio-optimizer-ai.git
cd bio-optimizer-ai
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py

📁 Sample Data

The repository includes a sample lab PDF with abnormal values for testing:

samples/sample_lab_report_abnormal_text.pdf

🔮 Future Improvements

Smarter PDF parsing across different lab formats

Additional biomarker systems (hormones, liver, kidney, micronutrients)

Trend analysis across multiple lab reports

Deployment with secure per-user API handling
