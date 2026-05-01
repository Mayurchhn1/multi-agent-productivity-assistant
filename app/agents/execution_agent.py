# -----------------------------
# 🚀 EXECUTION AGENT
# -----------------------------

def format_plan(plan_data: dict) -> dict:
    """
    Ensures final response is clean and structured
    """

    if not plan_data:
        return {
            "mode": "general",
            "summary": "No plan generated",
            "plan": []
        }

    return {
        "mode": plan_data.get("mode", "general"),
        "summary": plan_data.get("summary", ""),
        "plan": plan_data.get("plan", [])
    }
