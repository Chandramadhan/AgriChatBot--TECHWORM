import os
import time
import gdown
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from langchain_community.tools import WikipediaQueryRun, ArxivQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper, ArxivAPIWrapper, DuckDuckGoSearchAPIWrapper
from langdetect import detect
from deep_translator import GoogleTranslator
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# LangChain tools
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="output")
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200))
arxiv = ArxivQueryRun(api_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200))
duckduckgo = DuckDuckGoSearchRun(api_wrapper=DuckDuckGoSearchAPIWrapper(region="in-en", time="y", max_results=2))
tools = [wiki, arxiv, duckduckgo]

# Load LLM
def load_llm():
    return ChatGroq(
        model_name="llama3-70b-8192",
        temperature=0.2,
        groq_api_key=os.getenv("GROQ_API_KEY"),
    )

# Translation utils
def translate_to_english(text):
    try:
        lang = detect(text)
        return text if lang == "en" else GoogleTranslator(source=lang, target="en").translate(text), lang
    except:
        return text, "unknown"

def translate_back(text, lang):
    return text if lang == "en" else GoogleTranslator(source="en", target=lang).translate(text)

# Download + load model from Drive
@st.cache_resource
def load_disease_model():
    model_path = "plant_disease_model.h5"
    if not os.path.exists(model_path):
        with st.spinner("⬇️ Downloading model..."):
            gdown.download(id="10yfX5js5e4qtwBCV4KanMCHwczf8AKaD", output=model_path, quiet=False)
    return load_model(model_path)

model = load_disease_model()

# Label map
label_map = {
    "Apple___Apple_scab": 0, "Apple___Black_rot": 1, "Apple___Cedar_apple_rust": 2, "Apple___healthy": 3,
    "Blueberry___healthy": 4, "Cherry_(including_sour)___Powdery_mildew": 5, "Cherry_(including_sour)___healthy": 6,
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": 7, "Corn_(maize)___Common_rust_": 8,
    "Corn_(maize)___Northern_Leaf_Blight": 9, "Corn_(maize)___healthy": 10,
    "Grape___Black_rot": 11, "Grape___Esca_(Black_Measles)": 12, "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": 13,
    "Grape___healthy": 14, "Orange___Haunglongbing_(Citrus_greening)": 15, "Peach___Bacterial_spot": 16,
    "Peach___healthy": 17, "Pepper,_bell___Bacterial_spot": 18, "Pepper,_bell___healthy": 19,
    "Potato___Early_blight": 20, "Potato___Late_blight": 21, "Potato___healthy": 22,
    "Raspberry___healthy": 23, "Soybean___healthy": 24, "Squash___Powdery_mildew": 25,
    "Strawberry___Leaf_scorch": 26, "Strawberry___healthy": 27, "Tomato___Bacterial_spot": 28,
    "Tomato___Early_blight": 29, "Tomato___Late_blight": 30, "Tomato___Leaf_Mold": 31,
    "Tomato___Septoria_leaf_spot": 32, "Tomato___Spider_mites Two-spotted_spider_mite": 33,
    "Tomato___Target_Spot": 34, "Tomato___Tomato_Yellow_Leaf_Curl_Virus": 35,
    "Tomato___Tomato_mosaic_virus": 36, "Tomato___healthy": 37
}
inv_label_map = {v: k for k, v in label_map.items()}

def predict_disease(img):
    try:
        img = img.resize((224, 224))
        img_array = keras_image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        pred = model.predict(img_array)
        class_index = np.argmax(pred[0])
        return f"Prediction: {inv_label_map.get(class_index, 'Unknown')}"
    except Exception as e:
        return f"Error during prediction: {str(e)}"

def get_conversational_agent():
    llm = load_llm()
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        memory=st.session_state.chat_memory,
        verbose=True,
        return_intermediate_steps=True,
        max_iterations=15,
        max_execution_time=60,
        early_stopping_method="generate",
        handle_parsing_errors=True
    )

# Streamlit UI
def main():
    st.markdown("""
        <style>
        .stApp {
            background: url("https://en.reset.org/app/uploads/2020/06/india_farming.jpg") no-repeat center center fixed;
            background-size: cover;
            background-color: rgba(0, 50, 0, 0.3);
            background-blend-mode: darken;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("🌾 Techworm (Multilingual + Disease Detection) 🌾")
    st.subheader("Smart Assistant for Farming + Plant Health")

    if "chat_memory" not in st.session_state:
        st.session_state.chat_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if st.button("Reset Chat"):
        st.session_state.chat_memory.clear()
        st.session_state.messages = []
        st.success("Chat cleared!")

    for message in st.session_state.messages:
        st.chat_message(message["role"]).markdown(message["content"])

    st.markdown("## 📷 Upload a plant image")
    uploaded_image = st.file_uploader("Choose image...", type=["jpg", "jpeg", "png"])
    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption='Uploaded Image', width=250)
        result = predict_disease(img)
        st.success(result)

    prompt = st.chat_input("Ask your question in any language...")
    if prompt:
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        try:
            translated, lang = translate_to_english(prompt)
            st.write(f"🔍 Language: {lang.upper()}")
            st.write(f"🔄 Translated: {translated}")

            agent = get_conversational_agent()

            def trim_chat_memory(max_length=5):
                history = st.session_state.chat_memory.load_memory_variables({})["chat_history"]
                if len(history) > max_length:
                    st.session_state.chat_memory.chat_memory.messages = history[-max_length:]
                return history

            trim_chat_memory()
            final_prompt = f"""
You are an agriculture expert. Answer only farming-related questions.
Be accurate, clear, and concise.

User's Question: {translated}
"""

            response = agent.invoke({"input": final_prompt})
            output = response["output"] if isinstance(response, dict) else str(response)
            final_response = translate_back(output, lang)

            st.chat_message("assistant").markdown(final_response)
            st.session_state.messages.append({"role": "assistant", "content": final_response})

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
