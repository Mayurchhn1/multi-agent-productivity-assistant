from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.orchestrator import run_agent

app = FastAPI(
    title="Multi-Agent Productivity API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"status": "ok", "version": "FINAL-CLEAN"}

@app.post("/run")
def run(req: QueryRequest):
    return run_agent(req.query)
