import sqlite3
from datetime import datetime

DB_NAME = "tasks.db"


# -----------------------------
# 🔧 INIT DB
# -----------------------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Plans
    cur.execute("""
    CREATE TABLE IF NOT EXISTS plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT,
        summary TEXT,
        created_at TEXT
    )
    """)

    # Tasks
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plan_id INTEGER,
        task TEXT,
        time TEXT,
        type TEXT,
        priority INTEGER,
        status TEXT DEFAULT 'pending'
    )
    """)

    # Deals
    cur.execute("""
    CREATE TABLE IF NOT EXISTS deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_name TEXT,
        stage TEXT,
        value REAL,
        last_action TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# 💾 SAVE PLAN
# -----------------------------
def save_plan(query, summary, plan):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    created_at = datetime.utcnow().isoformat()

    cur.execute(
        "INSERT INTO plans (query, summary, created_at) VALUES (?, ?, ?)",
        (query, summary, created_at)
    )

    plan_id = cur.lastrowid

    for item in plan:
        cur.execute(
            "INSERT INTO tasks (plan_id, task, time, type, priority) VALUES (?, ?, ?, ?, ?)",
            (
                plan_id,
                item.get("task"),
                item.get("time"),
                item.get("type"),
                item.get("priority"),
            )
        )

    conn.commit()
    conn.close()

    return plan_id


# -----------------------------
# 📜 GET PLANS  (FIXED)
# -----------------------------
def get_plans(limit=10):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT id, query, summary, created_at FROM plans ORDER BY id DESC LIMIT ?",
        (limit,)
    )

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "id": r[0],
            "query": r[1],
            "summary": r[2],
            "created_at": r[3],
        }
        for r in rows
    ]


# -----------------------------
# 📋 GET TASKS
# -----------------------------
def get_tasks(limit=25):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT id, task, status FROM tasks ORDER BY id DESC LIMIT ?",
        (limit,)
    )

    rows = cur.fetchall()
    conn.close()

    return [
        {"id": r[0], "task": r[1], "status": r[2]}
        for r in rows
    ]


# -----------------------------
# 🔄 UPDATE TASK
# -----------------------------
def update_task_status(task_id, status):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "UPDATE tasks SET status=? WHERE id=?",
        (status, task_id)
    )

    conn.commit()
    conn.close()

    return {"id": task_id, "status": status}


# -----------------------------
# 💼 DEALS
# -----------------------------
def fetch_active_deals_from_db(limit=20):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "SELECT client_name, stage, value, last_action FROM deals WHERE status='active' LIMIT ?",
        (limit,)
    )

    rows = cur.fetchall()
    conn.close()

    return [
        {
            "client_name": r[0],
            "stage": r[1],
            "value": r[2],
            "last_action": r[3],
        }
        for r in rows
    ]


def save_deal(client_name, stage, value, last_action, status):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO deals (client_name, stage, value, last_action, status) VALUES (?, ?, ?, ?, ?)",
        (client_name, stage, value, last_action, status)
    )

    conn.commit()
    conn.close()

    return {"status": "saved"}
