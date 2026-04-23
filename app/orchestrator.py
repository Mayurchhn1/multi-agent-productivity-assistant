from app.agents.intent_agent import detect_intent
from app.agents.planner_agent import generate_plan
from app.agents.execution_agent import format_plan


def fallback(user_input: str):
    return {
        "mode": "general",
        "summary": "Starting with a simple execution plan.",
        "plan": [
            {
                "task": f"Start working on: {user_input}",
                "time": "Now",
                "type": "Execution",
                "priority": 3
            }
        ]
    }


def run_agent(user_input: str):
    try:
        print("🚀 MULTI-AGENT SYSTEM RUNNING")

        intent = detect_intent(user_input)

        raw_plan = generate_plan(user_input, intent)

        if not raw_plan:
            return fallback(user_input)

        final = format_plan(raw_plan)

        if not final:
            return fallback(user_input)

        return final

    except Exception as e:
        print("ERROR:", str(e))
        return fallback(user_input)