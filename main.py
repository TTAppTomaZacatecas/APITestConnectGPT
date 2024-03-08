from fastapi import FastAPI
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key="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")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/chat/{message}")
async def chat(message: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "Tú te llamarás Pancracio y hablarás como un guia de turista."},
            {"role": "user", "content": message}
        ]
    )
    return completion.choices[0].message.content

