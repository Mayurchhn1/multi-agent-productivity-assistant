from app.mcp.mcp_client import fetch_data

def enrich_task(task):
    info = fetch_data(task)
    return f"{task} ({info[:50]}...)"
