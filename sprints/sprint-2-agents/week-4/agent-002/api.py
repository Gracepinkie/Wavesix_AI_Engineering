from fastapi import FastAPI
from pydantic import BaseModel
from main import run_agent

app = FastAPI(title="Calculator Agent API")

class Query(BaseModel):
    question: str

@app.post("/calculate")
def calculate(query: Query):
    try:
        result = run_agent(query.question)
        return {"response": result}
    except Exception as e:
        return {"error": str(e)}

