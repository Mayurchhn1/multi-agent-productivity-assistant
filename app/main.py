import json
import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel

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
    version="3.1.0",
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
# 📁 Storage Setup
# -----------------------------
DATA_FILE = "plans.json"

def read_data():
    try:
        if not os.path.exists(DATA_FILE):
            return []
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Read error: {str(e)}")
        return []

def write_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Write error: {str(e)}")


# -----------------------------
# 📦 Request Models
# -----------------------------
class QueryRequest(BaseModel):
    query: str

class SaveRequest(BaseModel):
    plan: dict


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
        logger.error(f"UI load error: {str(e)}")
        return {"status": "error"}


# -----------------------------
# 🔍 Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "FlowPlan AI",
        "version": "3.1.0"
    }


# -----------------------------
# 🤖 AI Endpoint
# -----------------------------
@app.post("/run", response_model=QueryResponse)
def run(req: QueryRequest):
    try:
        result = run_agent(req.query)

        if not result or "plan" not in result:
            raise ValueError("Invalid AI response")

        return {
            "input": req.query,
            "mode": result.get("mode", "general"),
            "summary": result.get("summary", ""),
            "plan": result.get("plan", [])
        }

    except Exception as e:
        logger.error(f"/run error: {str(e)}")
        return {
            "input": req.query,
            "mode": "error",
            "summary": "Something went wrong",
            "plan": []
        }


# -----------------------------
# 💾 Save Plan
# -----------------------------
@app.post("/save")
def save(req: SaveRequest):
    try:
        data = read_data()

        # Add timestamp
        req.plan["saved_at"] = str(os.times())

        data.insert(0, req.plan)
        write_data(data)

        return {"status": "saved"}

    except Exception as e:
        logger.error(f"/save error: {str(e)}")
        return {"status": "error"}


# -----------------------------
# 📜 Get History
# -----------------------------
@app.get("/history")
def history():
    try:
        data = read_data()
        return data[:5]  # last 5 plans

    except Exception as e:
        logger.error(f"/history error: {str(e)}")
        return []