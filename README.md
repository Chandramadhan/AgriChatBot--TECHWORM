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
