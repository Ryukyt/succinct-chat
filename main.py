print("✅ APP STARTED")

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from openai import OpenAI
import os
import traceback

app = FastAPI()

# Initialize OpenAI client with the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def read_root():
    return {"status": "ok ✅"}

@app.post("/chat")
async def chat_with_character(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        print(f"📩 Received prompt: {prompt}")

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can change to "gpt-4o" if needed
            messages=[
                {"role": "system", "content": "You are a member of Succinct Labs."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content
        print("✅ Generated reply:", reply)
        return {"reply": reply}

    except Exception as e:
        print("❌ FULL ERROR:")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
