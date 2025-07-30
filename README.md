# 🌾 Agri Bot (Multilingual) 🌾

Agri Bot is an AI-powered multilingual chatbot designed to support farmers and agricultural researchers by providing real-time, accurate, and localized farming knowledge. It combines the power of LLMs, translation APIs, and online data sources to deliver intelligent, language-friendly agricultural assistance through a Streamlit-based chat interface.

![Languages](https://img.shields.io/badge/Languages-7+-green)
![Built With](https://img.shields.io/badge/Built%20With-Streamlit-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/github/license/yourusername/agri-bot)

---

## 🚀 Features

- ✅ **Multilingual Support** — Communicate in English, Hindi, Tamil, Telugu, Bengali, Marathi, Punjabi
- 🤖 **LLM Integration** — Powered by Llama 3-70B via Groq API for context-aware farming conversations
- 🔍 **Live Information Retrieval** — Wikipedia, Arxiv, and DuckDuckGo integrated for real-time search
- 🧠 **Memory Management** — Uses LangChain's ConversationBufferMemory to track session context
- 🎨 **Minimal UI** — Clean and intuitive Streamlit interface with custom CSS for readability

---

## 🛠 Tech Stack

| Component        | Technology                         |
|------------------|-------------------------------------|
| Frontend         | Streamlit                          |
| Backend (LLM)    | LangChain, Groq API (Llama 3)      |
| Search Tools     | Wikipedia, Arxiv, DuckDuckGo       |
| Translation      | Google Translator API              |
| Memory Handling  | LangChain Buffer Memory            |
| Environment Mgmt | python-dotenv                      |

---

## 📁 Project Structure

agri-bot/
├── app.py # Main Streamlit app
├── requirements.txt # Python dependencies
├── .env.example # Example env vars
├── README.md # Project documentation
├── /assets # UI assets and screenshots
└── /utils # Utility functions (optional)


---

## 📦 Requirements

- Python 3.8 or higher
- A Groq-compatible OpenAI API Key
- Internet connection (for search/translation)

---

## 🔧 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/agri-bot.git
   cd agri-bot

    Install Dependencies

pip install -r requirements.txt

Set Up Environment Variables

Create a .env file in the root directory and add:

    GROQ_API_KEY=your_groq_api_key_here

▶️ Usage

Run the Streamlit app:

streamlit run app.py

Open the link in your browser (http://localhost:8501) to start chatting with the bot.
🌍 How It Works

graph TD
A[User Input in Native Language] --> B[Language Detection]
B --> C[Translate to English]
C --> D[LLM via LangChain + Groq API]
D --> E[Search Tools (Wikipedia, Arxiv, DDG)]
E --> F[Generate Response]
F --> G[Translate to User Language]
G --> H[Display in Streamlit UI]

🎨 UI Overview

    🧑‍🌾 Chat Panel – Type questions in your native language

    🌐 Language Selector – Pick your preferred language in the sidebar

    🔄 Bidirectional Translation – Input is translated to English → Processed → Re-translated

    📊 Styled Layout – Responsive design using Streamlit and custom CSS

🔬 Future Enhancements

    🎤 Voice input and TTS-based responses

    📚 Fine-tuned domain-specific agricultural models

    🪄 Enhanced error handling and fallback responses

    🌐 Deployment with multi-device responsive UI

    🧠 Vector database integration for long-term memory (e.g., FAISS, ChromaDB)

🧪 Example Query

Question (in Hindi): गेहूं की उन्नत किस्में कौन सी हैं?
🔁 Translates to → What are the high-yield varieties of wheat?
🤖 AI Response: HD 2967, PBW 725, DBW 187, and HD 3086 are among the improved varieties...
🔁 Translated back to Hindi → HD 2967, PBW 725, DBW 187, और HD 3086 गेहूं की उन्नत किस्मों में शामिल हैं।

🤝 Contributing

We welcome community contributions!
Steps to Contribute:

    Fork the repository

    Create a new branch: git checkout -b feature/your-feature

    Make your changes and commit: git commit -m "Add your feature"

    Push to your branch: git push origin feature/your-feature

    Open a Pull Request with a clear description

Please follow clean code practices and ensure tests (if any) pass before PR submission.
📄 License

This project is licensed under the MIT License.
See the LICENSE file for more details.
📎 Resources & Links

    LangChain Docs

    Groq API

    Streamlit

    Agricultural Wikipedia Portal

✨ Author

Chandra Madhan V
@Chandramadhan
Feel free to connect and suggest improvements.

    Built with ❤️ to empower farmers with multilingual AI.
