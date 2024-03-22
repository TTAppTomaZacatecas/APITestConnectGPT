from openai import OpenAI
from utils.keys import API_KEY

client = OpenAI(api_key=API_KEY)

class ChatGPT:
    response = []

    def __init__(self):
        self.conversation = []

    def chat(self, message):
        self.conversation.append({"role": "system", "content": "Tú te llamarás Pancracio y hablarás como un guia de turista"})
        self.conversation.append({"role": "user", "content": message})

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.conversation
        )

        self.conversation.append({"role": "assistant", "content": completion.choices[0].message.content})

        return completion.choices[0].message.content

