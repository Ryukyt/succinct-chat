from fastapi.responses import JSONResponse

@app.post("/chat")
async def chat_with_character(request: Request):
    try:
        data = await request.json()
        prompt = data.get("prompt")

        # Debug print
        print(f"Received prompt: {prompt}")

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
        print("Error occurred:", str(e))  # This will show up in Railway logs
        return JSONResponse(status_code=500, content={"error": str(e)})
