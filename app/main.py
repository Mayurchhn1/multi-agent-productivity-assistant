from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import logging

from app.orchestrator import run_agent

# -----------------------------
# 🔧 Logging Setup
# -----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------
# 🚀 App Init
# -----------------------------
app = FastAPI(
    title="FlowPlan AI",
    description="Turn intent into execution plans using AI",
    version="3.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# -----------------------------
# 🌐 CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# 📦 Request Model
# -----------------------------
class QueryRequest(BaseModel):
    query: str


# -----------------------------
# 🧠 Response Models
# -----------------------------
class TaskItem(BaseModel):
    task: str
    time: str
    type: str
    priority: int


class QueryResponse(BaseModel):
    input: str
    mode: str
    summary: str
    plan: list[TaskItem]


# -----------------------------
# 🏠 Serve UI
# -----------------------------
@app.get("/")
def serve_ui():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "index.html")

        if not os.path.exists(file_path):
            return {"status": "ok", "message": "Backend running (UI missing)"}

        return FileResponse(file_path)

    except Exception as e:
        logger.error(str(e))
        return {"status": "error"}


# -----------------------------
# 🔍 Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "FlowPlan AI",
        "version": "3.0.0"
    }


# -----------------------------
# 🤖 AI Endpoint
# -----------------------------
@app.post("/run", response_model=QueryResponse)
def run(req: QueryRequest):
    try:
        result = run_agent(req.query)

        return {
            "input": req.query,
            "mode": result.get("mode", "general"),
            "summary": result.get("summary", ""),
            "plan": result.get("plan", [])
        }

    except Exception as e:
        logger.error(str(e))
        return {
            "input": req.query,
            "mode": "error",
            "summary": "Something went wrong",
            "plan": []
        }