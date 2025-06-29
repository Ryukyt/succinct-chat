print("✅ APP STARTED")

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "✅ App is Live"}

@app.post("/chat")
async def chat_with_character(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    return JSONResponse(content={"reply": f"You said: {prompt}"})
