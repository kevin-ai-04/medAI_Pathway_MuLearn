import os
import streamlit as st
import requests
from webscraper2 import search_and_scrape  # Assuming this is your custom module
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

API_KEY = os.environ.get("GOOGLE_API_KEY")
CSE_ID = os.environ.get("GOOGLE_CSE_ID")

st.title("MedAI")

with st.sidebar:
    st.sidebar.write("Add Links:")

    med_name = st.sidebar.text_area("Enter Name of Medicine")
    upload_button = st.sidebar.button("Upload")

    with st.expander("About"):
        st.write("[GitHub](https://github.com/kevin-ai-04)")

if upload_button:
    print("medname:", med_name)
    if med_name:
        with st.sidebar:
            with st.spinner("Uploading..."):
                try:
                    search_and_scrape(med_name, API_KEY, CSE_ID)
                    st.success("Uploaded!!")
                except ValueError as e:
                    st.error(f'Error in url: {e}')
    else:
        st.sidebar.error('Empty url value')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter Question Here"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    #sending to url
    url = f'http://{api_host}:{api_port}/'
    data = {"query": prompt}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        with st.chat_message("assistant"):
            text = response.json()
            response = st.write(text)
        st.session_state.messages.append({"role": "assistant", "content": text})


