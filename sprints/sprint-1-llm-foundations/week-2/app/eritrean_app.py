import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# App setup
st.set_page_config(page_title="Eritrean Culture Chat", page_icon="🇪🇷", layout="centered")

# App branding
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color:#008000;'>🇪🇷 Eritrean Culture & Cuisine Chat ትግርኛ </h1>
    </div>
""", unsafe_allow_html=True)

# User input
question = st.text_input("💬 Type your question about Eritrean culture:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful cultural guide for Eritrean and Ethiopian culture, food, and history."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.7,
                    max_tokens=300
                )
                answer = response["choices"][0]["message"]["content"]
                st.success(answer)
            except Exception as e:
                st.error(f"Error: {e}")
