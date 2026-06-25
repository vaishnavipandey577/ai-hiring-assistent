# ai-hiring-assistent
# 🤖 TalentScout — AI Hiring Assistant

> An intelligent interview preparation and hiring tool powered by **Groq's LLaMA 3.1** model, built with **Streamlit**.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-LLaMA%203.1-orange?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

---

## 📌 About the Project

**TalentScout** is an AI-powered hiring assistant that helps:
- 🎯 **Job Seekers** practice technical interview questions based on their tech stack
- 🧑‍💼 **Interviewers** generate relevant technical questions for candidates

It uses **Groq's ultra-fast inference API** with the **LLaMA 3.1 70B Versatile** model to generate customized interview questions and evaluate answers in real time.

---

## ✨ Features

- 📋 Candidate information form (name, experience, tech stack, location)
- 💡 AI-generated technical questions tailored to your stack & experience level
- ✅ One-by-one Q&A flow with answer reveal
- 🔁 Option to practice more questions after completing a set
- 📑 Full review of all questions and correct answers at the end
- 🔐 API key loaded securely from `.env` file
- 🌐 Model selector in sidebar (choose between LLaMA variants)
- ⚠️ Data privacy disclaimer — no data stored or shared

---

## 🖥️ Demo Screenshot

```
┌─────────────────────────────────────────────┐
│   TalentScout - AI Hiring Assistant         │
│─────────────────────────────────────────────│
│  👤 Candidate Information                   │
│  Name: John Doe    |  Experience: 2 years   │
│  Tech Stack: Python, Django, PostgreSQL      │
│  Role: Job Seeker                           │
│─────────────────────────────────────────────│
│  ❓ Question 1 of 3:                        │
│  What is Django ORM and how does it work?   │
│  ✍️ Your Answer: [________________]         │
│  [ Submit Answer ➡️ ]                       │
└─────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core language |
| Streamlit | Web UI framework |
| Groq API | LLM inference (LLaMA 3.1) |
| python-dotenv | Environment variable management |
| requests | HTTP API calls |

---

## 📁 Project Structure

```
talentscout/
├── app.py              # Main Streamlit application
├── .env                # Your API keys (never commit this!)
├── .env.example        # Template for environment variables
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- A free [Groq API Key](https://console.groq.com)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/talentscout.git
cd talentscout
```

---

### Step 2 — Create Virtual Environment

```bash
python -m venv venv
```

**Activate it:**

```bash
# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit requests groq python-dotenv
```

---

### Step 4 — Setup Environment Variables

Copy the example file:

```bash
cp .env.example .env
```

Open `.env` and add your Groq API key:

```env
GROQ_API_KEY=gsk_your_actual_api_key_here
GROQ_MODEL=llama-3.1-70b-versatile
```

> 🔑 **Get your free API key:** Go to [console.groq.com](https://console.groq.com) → API Keys → Create API Key → Copy & paste above.

---

### Step 5 — Run the App

```bash
# Recommended (works on all platforms)
python -m streamlit run app.py

# Or directly (if streamlit is in PATH)
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`

---

## 🤖 Available LLaMA Models

You can switch models in the sidebar or set a default in `.env`:

| Model | Speed | Quality | Best For |
|---|---|---|---|
| `llama-3.1-70b-versatile` | Fast | ⭐⭐⭐⭐⭐ Best | **Default — recommended** |
| `llama-3.1-8b-instant` | ⚡ Ultra Fast | ⭐⭐⭐ Good | Quick practice |
| `llama3-70b-8192` | Fast | ⭐⭐⭐⭐ High | Alternative high quality |
| `llama3-8b-8192` | ⚡ Very Fast | ⭐⭐⭐ Good | Lightweight usage |

---

## 🔐 Environment Variables

| Variable | Required | Default | Description |
|---|---|---|---|
| `GROQ_API_KEY` | ✅ Yes | — | Your Groq API key from console.groq.com |
| `GROQ_MODEL` | ❌ No | `llama-3.1-70b-versatile` | LLaMA model to use |

---

## 📦 requirements.txt

```txt
streamlit
requests
groq
python-dotenv
```

---

## 🔒 Security & Privacy

- ✅ API key stored in `.env` — never hardcoded in source
- ✅ `.env` must be added to `.gitignore` before pushing to GitHub
- ✅ No candidate data is stored or logged
- ✅ All interactions happen in-session only

**Add `.env` to `.gitignore`:**

```bash
echo ".env" >> .gitignore
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add: your feature"`
4. Push to your branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

Built with ❤️ using Groq + LLaMA + Streamlit.

---

## 🌟 Support

If you found this project helpful, please give it a ⭐ on GitHub!

> 💬 For issues or feature requests, open a [GitHub Issue](https://github.com/your-username/talentscout/issues).
