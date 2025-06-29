print("APP STARTED ✅")

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/chat")
async def chat_with_character(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    return JSONResponse(content={"reply": f"You said: {prompt}"})
