from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import openai
import os
import traceback

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def read_root():
    return {"status": "ok ✅"}

@app.post("/chat")
async def chat_with_character(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt", "")
        print(f"📩 Received prompt: {prompt}")

        # DEBUG: Show API Key status
        print("🔑 API Key is present:", bool(openai.api_key))

        # Generate completion
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a member of Succinct Labs."},
                {"role": "user", "content": prompt}
            ]
        )

        reply = completion.choices[0].message['content']
        print("✅ Generated reply:", reply)
        return {"reply": reply}

    except Exception as e:
        print("❌ FULL ERROR:")
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})
