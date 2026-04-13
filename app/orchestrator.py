from app.llm import generate_ai_response

def run_agent(query):
    print("🚀 MULTI-AGENT RUNNING")

    sales = generate_ai_response(f"Sales insight: {query}")
    tasks = generate_ai_response(f"Action tasks: {query}")
    planning = generate_ai_response(f"Execution plan: {query}")

    return {
        "input": query,
        "sales": sales,
        "tasks": tasks,
        "planning": planning
    }
