import logging
from typing import get_args
import streamlit as st
import requests
from src import constants

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

API_ENDPOINT = "http://127.0.0.1:8080/translate"
supported_lang_list = list(get_args(constants.SUPPORTED_LANG))

def translate(target_lang:str, user_input:str) -> str:
    output = ""
    try:
        payload = {
            "targetlang": target_lang,
            "english_text": user_input
        }
        response = requests.post(API_ENDPOINT, json=payload, timeout=60)
        response_data = response.json()
        output=response_data["translated_text"]
    except Exception as e:
        logger.exception("error occoured while calling translation service")
    return output

st.title("Translation chat bot")
option = st.selectbox(
    "Choose an target language:",
    supported_lang_list
)
user_input = st.text_input("Type english text: ")

if st.button("Send"):
    if user_input:
        output = translate(option, user_input)
        # Display response
        st.write("Response:")
        for line in output.split('\n'):
            st.write(line)
    else:
        st.warning("Please enter a message before sending.")
