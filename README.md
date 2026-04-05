![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Deployment](https://img.shields.io/badge/Deployed-Render-blue)

# 🚀 Multi-Agent Productivity Assistant

An AI-powered multi-agent system that helps users manage tasks, schedules, and workflows using coordinated agents and external tools.

---

## 🔷 Problem Statement

Build a system that:
- Manages tasks and schedules  
- Uses multiple tools and data sources  
- Executes multi-step workflows  
- Provides API-based interaction  

---

## 🔷 Solution Overview

A modular **multi-agent architecture**:

- 🧠 Orchestrator Agent – controls workflow  
- 📋 Task Agent – generates tasks  
- 📅 Calendar Agent – schedules tasks  
- 🔎 Research Agent – enriches tasks  

---

## 🔷 Architecture

User Input  
↓  
FastAPI API (/run)  
↓  
Orchestrator Agent  
↓  
Task Agent → Calendar Agent → Research Agent  
↓  
Database + External API  

---

## 🔷 Tech Stack

- Python  
- FastAPI  
- SQLite  
- Requests  
- Multi-Agent Architecture  

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
## 🔷 Key Features

- Multi-agent coordination
- Tool integration (MCP-style)
- Structured data storage
- Workflow automation
- API-based system

---

## 🔷 Use Cases

- Workday planning
- Personal productivity
- Project management
- Learning schedule planning
- Daily task automation

---

## 🔷 Future Improvements

- Google Maps MCP integration
- BigQuery MCP tools
- Calendar API integration
- Cloud deployment (Cloud Run)
- Frontend dashboard

---

## 📊 Demo Output

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
👤 Author

Mayur Chauhan