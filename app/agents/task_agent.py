from app.db.database import add_task

def create_tasks(user_input):
    user_input = user_input.lower()

    if "work" in user_input:
        tasks = ["Emails", "Meetings", "Deep Work"]
    elif "gym" in user_input:
        tasks = ["Workout", "Shower", "Protein Meal"]
    elif "project" in user_input:
        tasks = ["Planning", "Execution", "Review"]
    elif "learn" in user_input:
        tasks = ["Watch Tutorials", "Practice", "Revise"]
    else:
        tasks = ["General Task 1", "General Task 2"]

    for t in tasks:
        add_task(t, "Not Scheduled")

    return tasks
