import streamlit as st
from ollama import Client 

client = Client(host="http://localhost:11434") 

st.set_page_config(
    page_title="Custom LLM model by Saket and under guidance of Prakash Senapati - Ollama",
    layout="centered"
)

st.title("Mr. Prakash Senapati - Ollama App")

prompt = st.text_area("Enter your prompt:", height=200)

if st.button("Generate Response"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat(
                model="kimi-k2.5:cloud",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("Response Generated!")
            st.write(response["message"]["content"])