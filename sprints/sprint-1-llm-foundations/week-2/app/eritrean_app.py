import streamlit as st
import requests

st.set_page_config(page_title="Eritrean Culture Chat", page_icon="🇪🇷", layout="centered")

st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color:#008000;'>🇪🇷 Eritrean Culture & Cuisine Chat ባህላዊ </h1>
    </div>
""", unsafe_allow_html=True)

question = st.text_input("💬 Type your question about Eritrean culture:")

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            try:
                # ✅ Send the correct key expected by FastAPI
                res = requests.post("http://localhost:8000/chat", json={"question": question})
                res.raise_for_status()
                st.success(res.json()["answer"])
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
                st.error("Please check your FastAPI server or API key.")
