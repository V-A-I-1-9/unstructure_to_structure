# Unstruct2Struct 🧠  
### Turn Messy Text into Clear, Actionable Structure

Unstruct2Struct is a lightweight AI-powered utility that converts unstructured,
messy human text into clean, structured, and actionable outputs.

It is designed for students, developers, and early professionals who want
clarity, direction, and execution-ready information — fast.

---

## 🚀 Live Application
👉 https://unstruct2struct.streamlit.app

---

## 🎯 Why Unstruct2Struct?

People often struggle with:
- Vague project ideas
- Messy notes and thoughts
- Unclear requirements
- Confusing instructions

Unstruct2Struct helps you move from **confusion → clarity → execution**.

This is not a chatbot.  
It is a **thinking utility**.

---

## ✨ Core Features

### 1️⃣ Messy Text → Action Plan
Convert vague ideas into:
- Clear goal
- Step-by-step execution plan
- Deliverables
- Time estimate

---

### 2️⃣ Problem Statement → Project Blueprint
Turn a rough idea into:
- Problem summary
- Target users
- Core features
- Tech stack
- MVP scope

---

### 3️⃣ Requirements → Checklist Generator
Transform requirements into:
- Structured checklist
- Execution-ready tasks
- Submission clarity

---

### 4️⃣ Text → Multiple Output Formats
Convert the same input into:
- JSON
- Bullet points
- Markdown

Perfect for documentation and reports.

---

## 🧠 How It Works

1. User provides unstructured text
2. AI understands intent and context
3. Prompt-engineered logic enforces structure
4. Output is normalized and formatted
5. User receives clean, usable results

The system uses **deterministic LLM outputs** with strict formatting rules.

---

## 🛠 Tech Stack

- Python
- Streamlit (Frontend)
- Groq LLM API
- Prompt Engineering
- JSON-based output contracts

---

## 📂 Project Structure

unstruct2struct/
│
├── app.py # Streamlit UI
├── llm_client.py # Groq API client
├── prompts.py # System prompts
├── transformers.py # Core transformation logic
├── formatter.py # Output formatting
├── schemas.py # Output contracts
├── utils.py # Helpers & normalization
├── requirements.txt
├── README.md
└── .gitignore

---

## Run Locally

pip install -r requirements.txt
streamlit run app.py

## Add your API key in

.streamlit/secrets.toml
GROQ_API_KEY = "your_api_key_here"

## Author

Vaibhav MS
