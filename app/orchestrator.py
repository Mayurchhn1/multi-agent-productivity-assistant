from app.agents.task_agent import create_tasks
from app.agents.calendar_agent import schedule_tasks
from app.agents.research_agent import enrich_task

def run_agent(user_input):
    # Step 1: Create tasks
    tasks = create_tasks(user_input)

    # Step 2: Enrich tasks with external info
    enriched_tasks = [enrich_task(t) for t in tasks]

    # Step 3: Schedule tasks
    schedule = schedule_tasks(enriched_tasks)

    return {
        "input": user_input,
        "plan": schedule
    }
