from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load or create data
if os.path.exists("data.json"):
    with open("data.json", "r") as f:
        data = json.load(f)
else:
    data = {"tasks": [], "schedule": []}

def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f)

# Task Agent
def task_agent(command):
    if "add task" in command:
        task = command.replace("add task", "").strip()
        data["tasks"].append(task)
        save_data()
        return f"Task added: {task}"
    elif "show tasks" in command:
        return data["tasks"] if data["tasks"] else "No tasks found"

# Schedule Agent
def schedule_agent(command):
    if "add meeting" in command:
        meeting = command.replace("add meeting", "").strip()
        data["schedule"].append(meeting)
        save_data()
        return f"Meeting added: {meeting}"
    elif "show schedule" in command:
        return data["schedule"] if data["schedule"] else "No meetings found"

# Main Agent
def main_agent(query):
    query = query.lower()

    if "task" in query:
        return task_agent(query)
    elif "meeting" in query or "schedule" in query:
        return schedule_agent(query)
    else:
        return "I manage tasks and schedules."

# API endpoint
@app.route("/agent", methods=["POST"])
def agent():
    user_input = request.json.get("query")
    response = main_agent(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
