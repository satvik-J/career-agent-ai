---
title: career_conversation
app_file: app.py
sdk: gradio
sdk_version: 5.49.1
---

# 🤖 AI Portfolio Assistant

An intelligent, agentic AI chatbot that represents my professional profile and answers questions about my education, technical skills, projects, certifications, and career experience.

Unlike a traditional chatbot, this project includes a self-evaluation pipeline where a secondary LLM reviews generated responses for quality and automatically regenerates responses that fail evaluation.

---

## 🚀 Features

- 💬 Conversational AI powered by OpenAI GPT-4o Mini
- 🧠 Context-aware responses using my LinkedIn profile and professional summary
- ✅ LLM-as-a-Judge response evaluation using Pydantic structured outputs
- 🔄 Automatic response regeneration when quality checks fail
- 🖥️ Interactive Gradio web interface
- 📁 Modular Python architecture for scalability and maintainability

---

## 🏗️ Project Architecture

```
CareerAgent AI/
│
├── app.py                 # Gradio interface
├── agent.py               # Core conversational agent
├── evaluator.py           # LLM response evaluation pipeline
├── prompts.py             # Prompt templates
├── knowledge.py           # Loads portfolio knowledge
├── config.py              # OpenAI configuration
│
├── data/
│   ├── linkedin.pdf
│   └── summary.txt
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

- Python
- OpenAI SDK
- GPT-4o Mini
- Gradio
- Pydantic
- python-dotenv
- PyPDF

---

## 🧠 How It Works

1. The user asks a question.
2. The AI agent generates a response using portfolio knowledge.
3. A secondary LLM evaluates the generated response.
4. If the response passes evaluation, it is returned to the user.
5. If the response fails, the agent regenerates a better response using evaluator feedback.

This evaluation workflow improves response reliability and demonstrates an agentic AI architecture.

---

## 📂 Knowledge Sources

The assistant answers questions using:

- Professional summary
- LinkedIn profile
- Education
- Projects
- Technical skills
- Certifications
- Career achievements

---

## ▶️ Running Locally

Clone the repository

```bash
git clone <repository-url>
cd personal-ai-agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENAI_API_KEY=your_api_key
```

Run the application

```bash
python app.py
```

---

## 📌 Future Improvements

- Tool Calling
- Recruiter lead capture
- Notification workflows
- Resume download
- GitHub & LinkedIn integration
- Multi-agent architecture
- RAG support using vector databases

---

## 👤 Author

**Satvik J**

B.Tech Computer Science Student

AI • Machine Learning • Full Stack Development • Agentic AI