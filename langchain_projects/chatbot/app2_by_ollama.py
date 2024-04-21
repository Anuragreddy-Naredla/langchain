from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# if we keep 'true' in langchain_tracing_v2 it will automatically it will do the tracing 
os.environ["LANGCHAIN_TRACING_V2"]='true'# Langsmith tracking.
# which helps us to where the entire monitoring results should be stored
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# PromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries"), ("user", "Question:{question}")
    ])

st.title("Langchain with OLLAMA")
input_text = st.text_input("Search the topic u want")

# OPENAI LLM.
llm = Ollama(model="llama2")

# This will be responsible for getting the ouput itself.
output_parser = StrOutputParser()
# we are combining the prompt, llm and output parser.
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))



