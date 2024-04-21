import requests
import streamlit as st

def get_openai_response(input_text):
    """
    This function interact with the openai API.
    """
    response = requests.post("http://localhost:8000/essay/invoke", 
                             json={'input':{'topic':input_text}})
    return response.json()['output']['content']


def get_ollama_response(input_text):
    """
    This function will interact with the ollama.
    """
    response=requests.post("http://localhost:8000/poem/invoke",
                           json={'input':{'topic':input_text}})
    return response.json()['output']

st.title("Langchain with LLAMA2 API")
input_text = st.text_input("Write a esaay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))
if input_text1:
    st.write(get_ollama_response(input_text1))