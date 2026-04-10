![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Deployment](https://img.shields.io/badge/Deployed-Render-blue)

# 🚀 AI Sales & Productivity Assistant

🌐 Live Demo: https://multi-agent-productivity-assistant-y8sv.onrender.com  
📄 API Docs: https://multi-agent-productivity-assistant-y8sv.onrender.com/docs  

---

## 🚀 What This Project Solves

Sales and business professionals often spend excessive time:
- Deciding when to follow up
- Planning their workday
- Prioritizing tasks

This assistant simplifies decision-making and improves productivity through a structured multi-agent system.

---

## 💼 Use Cases

### 1. Sales Follow-up Planning
- Identify lead type (Hot/Warm/Cold)
- Suggest next action
- Generate ready-to-use follow-up message

### 2. Daily Workday Planning
- Automatically structure your day
- Balance meetings, calls, and deep work

### 3. Task Prioritization
- Identify high-impact tasks
- Focus on revenue-generating activities

---

## 🎯 Key Features

- 🧠 Multi-agent decision system  
- 📊 Structured business-friendly output  
- ⚡ FastAPI-powered backend  
- 🔌 Ready for AI integration (Gemini / OpenAI)  
- 🌐 Live deployed API  

---

## 🧠 Architecture Diagram

```mermaid
flowchart TD
    A[User Input] --> B[Orchestrator]

    B --> C[Sales Agent]
    B --> D[Task Agent]
    B --> E[Planning Agent]

    C --> F[Analysis]
    D --> F
    E --> F

    F --> G[Structured Output]
    G --> H[API Response]

    ---
    ## 🛠️ Tech Stack

- Python  
- FastAPI  
- REST API  
- Render (Deployment)  

---

## 📡 API Usage

### Endpoint:
POST /run

### Example Output:
```json
{
  "input": "Client not responding after proposal",
  "analysis": {
    "lead_type": "Warm",
    "confidence": "80%",
    "priority": "Medium"
  },
  "action_plan": {
    "next_step": "Follow-up",
    "recommended_time": "1-2 days",
    "channel": "Call + WhatsApp"
  },
  "message_suggestion": "Hi, just following up on our discussion. Let me know a convenient time to connect."
}
