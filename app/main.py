from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os
import logging

from app.orchestrator import run_agent
from app.db.database import (
    init_db,
    get_plans,
    get_tasks,
    update_task_status,
    fetch_active_deals_from_db,
    save_deal,
)
from app.decision_engine import get_context
from app.llm_router import run_llm_healthcheck

# -----------------------------
# 🔧 Logging
# -----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -----------------------------
# 🚀 App Init
# -----------------------------
app = FastAPI(title="FlowPlan AI", version="4.0.0")

init_db()

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
# 📦 Models
# -----------------------------
class QueryRequest(BaseModel):
    query: str


class TaskStatusRequest(BaseModel):
    status: str


class DealRequest(BaseModel):
    client_name: str
    stage: str
    value: float
    last_action: str
    status: str = "active"


# -----------------------------
# 🏠 UI
# -----------------------------
@app.get("/")
def serve_ui():
    file_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return {"status": "ok", "message": "UI not found"}


# -----------------------------
# ❤️ Health
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "FlowPlan AI",
        "version": "4.0.0"
    }


@app.get("/llm/status")
def llm_status():
    return run_llm_healthcheck()


# -----------------------------
# 🤖 RUN AGENT
# -----------------------------
@app.post("/run")
def run(req: QueryRequest):
    try:
        logger.info(f"Query: {req.query}")
        result = run_agent(req.query)

        return {
            "mode": result.get("mode", "general"),
            "summary": result.get("summary", ""),
            "plan": result.get("plan", []),
        }

    except Exception as e:
        logger.error(f"/run error: {str(e)}")
        return {"error": str(e)}


# -----------------------------
# 📜 HISTORY
# -----------------------------
@app.get("/history")
def history(limit: int = Query(10)):
    try:
        return {"data": get_plans(limit)}
    except Exception as e:
        return {"error": str(e)}


# -----------------------------
# 📋 TASKS
# -----------------------------
@app.get("/tasks")
def tasks(limit: int = Query(20)):
    return {"data": get_tasks(limit)}


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, req: TaskStatusRequest):
    return update_task_status(task_id, req.status)


# -----------------------------
# 💼 DEALS (FIXED)
# -----------------------------
@app.get("/deals")
def get_deals(limit: int = Query(20)):
    return {"data": fetch_active_deals_from_db(limit)}


@app.post("/deals")
def create_deal(req: DealRequest):
    return save_deal(
        client_name=req.client_name,
        stage=req.stage,
        value=req.value,
        last_action=req.last_action,
        status=req.status,
    )


# -----------------------------
# 📊 DASHBOARD
# -----------------------------
@app.get("/dashboard")
def dashboard():
    try:
        context = get_context(limit=5)

        return {
            "top_priorities": context.get("top_deals", []),
            "pipeline": context.get("pipeline", {}),
            "recent_actions": get_tasks(limit=5),
        }

    except Exception as e:
        logger.error(f"/dashboard error: {str(e)}")
        return {"error": "Failed to load dashboard"}
