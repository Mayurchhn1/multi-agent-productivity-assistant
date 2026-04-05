from fastapi import FastAPI
from app.orchestrator import run_agent

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Multi-Agent Productivity Assistant Running"}

@app.post("/run")
def run(query: str):
    result = run_agent(query)
    return result
