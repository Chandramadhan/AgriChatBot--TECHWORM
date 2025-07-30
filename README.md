# 🌾 Agri Bot (Multilingual) 🌾

Agri Bot is an AI-powered multilingual chatbot built to assist farmers and agricultural enthusiasts by delivering accurate, real-time farming insights. It leverages LLMs (Llama 3-70B via Groq API), advanced search tools, and translation APIs to serve users across diverse languages and regions.

![Language Support](https://img.shields.io/badge/languages-7+-green)
![Built with Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)
![License](https://img.shields.io/github/license/yourusername/agri-bot)

---

## 🚀 Features

- 🌐 **Multilingual Support**: Hindi, English, Tamil, Telugu, Bengali, Marathi, Punjabi
- 🧠 **AI-Powered Conversations**: Uses Llama 3-70B via Groq API
- 🔍 **Live Data Retrieval**: Integrates Wikipedia, Arxiv, DuckDuckGo
- 💬 **Context-Aware Memory**: Remembers previous user inputs (LangChain memory)
- 🎨 **User-Friendly UI**: Built with Streamlit + custom CSS for clean visuals

---

## 🛠️ Tech Stack

| Layer         | Tools/Tech Used                              |
|---------------|-----------------------------------------------|
| Frontend      | Streamlit                                     |
| LLM Backend   | LangChain, Llama 3 (via Groq API), OpenAI     |
| Search Tools  | Wikipedia API, Arxiv, DuckDuckGo Search       |
| Translation   | Google Translator API                         |
| Memory Store  | LangChain ConversationBufferMemory            |

---

## 📦 Prerequisites

- Python 3.8 or higher
- Groq-compatible OpenAI API key
- Recommended to use a virtual environment

Install core dependencies:

```bash
pip install streamlit langchain openai langdetect deep-translator python-dotenv

🔧 Installation Guide

    Clone the repo

git clone https://github.com/yourusername/agri-bot.git
cd agri-bot

Install dependencies

pip install -r requirements.txt

Set up environment variables
Create a .env file in the root directory:

    GROQ_API_KEY=your_groq_api_key

▶️ Running the App

streamlit run app.py

You’ll see a local link like http://localhost:8501 to open in your browser.
🎨 UI Overview

    🧑‍🌾 Chat Panel: Ask farming-related questions in your native language

    🌍 Sidebar Language Selector: Choose your preferred language

    🔄 Automatic Translation: Input is translated → processed → output retranslated

    💡 Real-time Query Resolution: Instant fetch from Wikipedia/Arxiv/DDG

🔍 How It Works

graph LR
A[User Input] --> B[Language Detection]
B --> C[Translate to English]
C --> D[AI Model via Groq API]
D --> E[Generate Answer]
E --> F[Translate to User Language]
F --> G[Display Response in Streamlit]

🚧 Future Improvements

    🎙 Voice input & TTS (text-to-speech) support

    📈 Fine-tune models for agriculture domain

    📱 Mobile-first UI experience

    🧠 Integrate vector DB (like FAISS) for domain-specific memory

🤝 Contributing

We welcome contributions! Please read CONTRIBUTING.md for setup, branching, and commit guidelines.
📄 License

This project is licensed under the MIT License.
🌐 Links

    🔗 Live Demo (if hosted)

    📘 Documentation

    🧑‍💻 Author: @yourusername


---

## 📁 Recommended Files to Add:

1. **`.env.example`**
```env
GROQ_API_KEY=your_api_key_here🔧 Installation Guide

    Clone the repo

git clone https://github.com/yourusername/agri-bot.git
cd agri-bot

Install dependencies

pip install -r requirements.txt

Set up environment variables
Create a .env file in the root directory:

    GROQ_API_KEY=your_groq_api_key

▶️ Running the App

streamlit run app.py

You’ll see a local link like http://localhost:8501 to open in your browser.
🎨 UI Overview

    🧑‍🌾 Chat Panel: Ask farming-related questions in your native language

    🌍 Sidebar Language Selector: Choose your preferred language

    🔄 Automatic Translation: Input is translated → processed → output retranslated

    💡 Real-time Query Resolution: Instant fetch from Wikipedia/Arxiv/DDG

🔍 How It Works

graph LR
A[User Input] --> B[Language Detection]
B --> C[Translate to English]
C --> D[AI Model via Groq API]
D --> E[Generate Answer]
E --> F[Translate to User Language]
F --> G[Display Response in Streamlit]

🚧 Future Improvements

    🎙 Voice input & TTS (text-to-speech) support

    📈 Fine-tune models for agriculture domain

    📱 Mobile-first UI experience

    🧠 Integrate vector DB (like FAISS) for domain-specific memory

🤝 Contributing

We welcome contributions! Please read CONTRIBUTING.md for setup, branching, and commit guidelines.
📄 License

This project is licensed under the MIT License.
🌐 Links

    🔗 Live Demo (if hosted)

    📘 Documentation

    🧑‍💻 Author: @yourusername


---

## 📁 Recommended Files to Add:

1. **`.env.example`**
```env
GROQ_API_KEY=your_api_key_here
