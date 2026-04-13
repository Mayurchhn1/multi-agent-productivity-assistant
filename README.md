 ![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)
![Deployment](https://img.shields.io/badge/Deployed-Replit-blue)

# ⚡ AI Productivity Assistant  
### Multi-Agent Decision Engine for Smarter Execution

🌐 **Live Demo:** https://592fb534-088a-42ef-9ccd-465d1dd6b11b-00-3ka2nxvaf4wzn.sisko.replit.dev/  
📄 **API Docs:** https://592fb534-088a-42ef-9ccd-465d1dd6b11b-00-3ka2nxvaf4wzn.sisko.replit.dev/docs   

## 📸 Demo Preview

![App Screenshot](multi_agent_assistant_output.png)
---

## 🚀 Problem

Sales and business professionals often struggle with:

- Deciding the next best action  
- Planning their workday effectively  
- Prioritizing high-impact tasks  

This leads to delays, missed opportunities, and decision fatigue.

---

## 💡 Solution

AI Productivity Assistant is a **multi-agent decision system** that transforms input into structured execution:

- 🧠 Insight (What’s happening?)  
- 📋 Action (What to do next?)  
- 📅 Execution (How to execute?)  

👉 Not a chatbot — a system designed for real-world decision-making.

---

## 💼 Use Cases

### 1. Sales Follow-up Strategy
- Identify lead status (Hot/Warm/Cold)  
- Suggest next steps  
- Generate actionable follow-up approach  

### 2. Daily Work Planning
- Structure the day intelligently  
- Balance meetings, calls, and focused work  

### 3. Task Prioritization
- Identify high-impact activities  
- Focus on revenue-driving actions  

---

## 🎯 Key Features

- 🧠 Multi-agent architecture  
- 📊 Structured, business-ready outputs  
- ⚡ FastAPI backend  
- 🔌 AI-ready (Gemini / OpenAI integration)  
- 🌐 Live deployed API  

---

## 🧠 Architecture

```mermaid
flowchart TD
    A[User Input] --> B[Orchestrator]

    B --> C[Sales Agent]
    B --> D[Task Agent]
    B --> E[Planning Agent]

    C --> F[Insight]
    D --> F[Action]
    E --> F[Execution]

    F --> G[Structured Output]
    G --> H[API Response]