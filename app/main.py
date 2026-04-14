from fastapi.responses import FileResponse
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.orchestrator import run_agent

app = FastAPI(
    title="Multi-Agent Productivity API",
    description="AI system to manage tasks, schedules, and workflows using multiple agents",
    version="1.0.0"
)

# ✅ FIX: CORS (VERY IMPORTANT)
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
def serve_home():
    return FileResponse(os.path.join(os.getcwd(), "..", "index.html"))

# ✅ FIX: use orchestrator (multi-agent)
@app.post("/run")
def run(req: QueryRequest):
    return run_agent(req.query)
