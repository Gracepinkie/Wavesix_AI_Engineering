from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class QuestionRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(request: QuestionRequest):
    question = request.question

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful cultural guide for Eritrean and Ethiopian culture, food, and history."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=300
        )
        answer = response.choices[0].message.content
        return {"answer": answer}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
