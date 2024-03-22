from fastapi import FastAPI
from openai import OpenAI
from ChatGPT import ChatGPT
from utils.keys import API_KEY

app = FastAPI()
client = OpenAI(api_key=API_KEY)
chat_gpt = ChatGPT()

@app.get("/")
async def root():
    return {"message": "Hola a la API de prueba de la IA!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/chat/{message}")
async def chat(message: str):
    print("- Usuario: ", message)
    response = chat_gpt.chat(message)
    print("- Bot: ",response, "\n")
    return response

