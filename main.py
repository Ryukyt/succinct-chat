from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat_with_character(request: Request):
    data = await request.json()
    prompt = data.get("prompt")

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or gpt-4o
        messages=[{"role": "system", "content": "You are a member of Succinct Labs."},
                  {"role": "user", "content": prompt}]
    )

    return {"reply": completion.choices[0].message['content']}
