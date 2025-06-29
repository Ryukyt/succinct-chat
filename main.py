print("✅ APP STARTED")

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import requests
import traceback
import os

app = FastAPI()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

@app.get("/")
def read_root():
    return {"status": "ok ✅"}

@app.post("/chat")
async def chat_with_character(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        print(f"📩 Prompt: {prompt}")

        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "mixtral-8x7b",
                "messages": [
                    {"role": "system", "content": "You are a friendly and insightful member of the Succinct Labs community."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7
            }
        )

        res = response.json()
        print("🧾 Full Groq response:", res)

        if "choices" in res and res["choices"]:
            reply = res["choices"][0]["message"]["content"]
            print("✅ Reply:", reply)
            return {"reply": reply}
        else:
            return JSONResponse(status_code=500, content={"error": "Invalid response from Groq", "details": res})

    except Exception as e:
        print("❌ ERROR:")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})


