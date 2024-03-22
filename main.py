from fastapi import FastAPI
from openai import OpenAI

from ChatGPT import ChatGPT
from utils.keys import API_KEY

app = FastAPI()
client = OpenAI(api_key=API_KEY)
chat_gpt = ChatGPT()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/chat/{message}")
async def chat(message: str):
    return chat_gpt.chat(message)

