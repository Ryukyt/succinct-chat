print("✅ APP STARTED")

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os

app = FastAPI()

# Load OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def read_root():
    return {"status": "ok ✅"}

@app.post("/chat")
async def chat_with_character(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")

        print(f"User prompt: {prompt}")

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a member of Succinct Labs."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = completion.choices[0].message['content']
        return {"reply": reply}

    except Exception as e:
        print("❌ Error occurred:", str(e))
        return JSONResponse(status_code=500, content={"error": str(e)})
