# multi-agent-productivity-assistant
# 🚀 Multi-Agent Productivity Assistant

An AI-powered multi-agent system that helps users manage tasks, schedules, and information through coordinated agents and external tools.

---

## 🔷 Problem Statement

Build a multi-agent AI system that:
- Manages tasks and schedules
- Uses multiple tools and data sources
- Executes multi-step workflows
- Provides API-based interaction

---

## 🔷 Solution Overview

This project implements a **multi-agent architecture** where a central orchestrator coordinates multiple specialized agents:

- 🧠 Orchestrator Agent – controls workflow
- 📋 Task Agent – generates tasks
- 📅 Calendar Agent – schedules tasks
- 🔎 Research Agent – enriches tasks with external data

---

## 🔷 Architecture
User Input → FastAPI API (/run)
↓
Orchestrator Agent
↓
┌────────────┼────────────┬────────────┐
↓            ↓            ↓
Task Agent   Calendar Agent   Research Agent
↓            ↓                ↓
Database     Scheduling       External API (MCP-style)
---

## 🔷 Tech Stack

- Python
- FastAPI
- SQLite (Database)
- Requests (External API)
- Modular Multi-Agent Architecture

---

## 🔷 API Endpoint

### POST /run

#### Input:
Plan my workday
#### Output:
```json
{
  "input": "Plan my workday",
  "plan": [
    {
      "task": "Emails",
      "time": "9:00 AM"
    },
    {
      "task": "Meetings",
      "time": "1:00 PM"
    },
    {
      "task": "Deep Work",
      "time": "6:00 PM"
    }
  ]
}
🔷 Key Features
	•	Multi-agent coordination
	•	Tool integration (MCP-style)
	•	Structured data storage
	•	Workflow automation
	•	API-based system

⸻

🔷 Use Cases
	•	Workday planning
	•	Personal productivity
	•	Project management
	•	Learning schedule planning
	•	Daily task automation

⸻

🔷 Future Improvements
	•	Google Maps MCP integration
	•	BigQuery MCP tools
	•	Calendar API integration
	•	Cloud deployment (Cloud Run)
	•	Frontend dashboard

⸻

🔷 Demo Output

(Add your screenshot here)

⸻

🔷 Author

Mayur Chauhan
