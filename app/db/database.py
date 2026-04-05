import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    title TEXT,
    status TEXT,
    scheduled_time TEXT
)
""")

def add_task(title, time):
    cursor.execute(
        "INSERT INTO tasks (title, status, scheduled_time) VALUES (?, ?, ?)",
        (title, "pending", time)
    )
    conn.commit()

def get_tasks():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()
