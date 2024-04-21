from fastapi import FastAPI

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes

import uvicorn
import os

from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API server"
    )
# adding routes.
add_routes(
    app,# app.py
    ChatOpenAI(),
    path = "/openai"
    )

model = ChatOpenAI()
llm = Ollama(model = "llama2")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")# interacting with chat openai api.
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")# Interacting with llm model.

add_routes(
    app, 
    prompt1|model,
    path = "/essay"# the url ending with /essay
)

add_routes(
    app,
    prompt2|llm,
    path = "/poem"# the URL ending with /poem
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port = 8000)

