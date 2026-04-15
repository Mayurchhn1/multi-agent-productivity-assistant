# ⚡ AI Productivity Assistant: Multi-Agent Decision Engine
### Replace Hours of Planning with Seconds of AI Execution

[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![Gemini 1.5](https://img.shields.io/badge/Google_Cloud-Gemini_1.5-4285F4.svg)](https://deepmind.google/technologies/gemini/)
[![Deployment](https://img.shields.io/badge/Deployed-Emergent.sh-7B61FF.svg)](https://app.emergent.sh/home)

---

## 🌐 Live System
🚀 **Live Demo:** https://task-automation-ai-10.preview.emergentagent.com/home  
📄 **API Docs (Swagger):** https://task-automation-ai-10.preview.emergentagent.com/docs  

---

## 🚀 The Vision: Beyond Chatbots

Most AI tools today are passive — they generate answers.

This system is built differently.

Developed for the **Google Cloud Gen AI Academy (APAC Edition)**, this project introduces a **Multi-Agent Decision Engine** that converts business goals into structured, execution-ready workflows.

Instead of just responding, the system:
- Understands business context  
- Prioritizes high-impact actions  
- Generates clear execution plans  

👉 It doesn’t just assist — it **thinks, decides, and executes**

---

## ⚡ What Makes This Different?

| Traditional AI | This System |
|---------------|------------|
| Gives answers | Drives execution |
| Single response | Multi-agent reasoning |
| Unstructured text | Structured outputs |
| Passive assistance | Action-oriented intelligence |

---

## 🧠 The Multi-Agent Core

The system uses **three specialized AI agents**, each solving a critical part of the decision process:

### 🧠 Strategic Insight Agent — *The What*
- Understands intent and context  
- Detects urgency and opportunity  
- Evaluates lead quality  

---

### 📋 Actionable Priority Agent — *The When*
- Ranks tasks based on impact  
- Identifies high-value actions  
- Filters low-priority work  

---

### 📅 Workflow Execution Agent — *The How*
- Creates execution-ready plans  
- Generates communication templates  
- Defines timelines and next steps  

---

👉 Final Output: **Structured, actionable, execution-ready plan**

---

## ⚡ Example Output

**Input:**  
"Follow up with a warm lead who hasn’t responded in 3 days"

**AI Output:**

| Insight | Action | Execution |
|--------|--------|----------|
| Lead is warm but cooling | Send personalized follow-up | Email + WhatsApp + Reminder |
| Risk of drop-off | Re-engage with urgency | Schedule call within 24 hrs |

👉 Not just insight — **clear execution guidance**

---

## 🛠️ Architecture

```mermaid
flowchart TD
    A[User Business Goal] --> B{Gemini 1.5 Orchestrator}
    
    subgraph Agentic_Layer [Multi-Agent Decision Engine]
    B --> C[Strategic Insight Agent]
    B --> D[Actionable Priority Agent]
    B --> E[Workflow Execution Agent]
    end

    C & D & E --> F[Structured Output Engine]
    F --> G[FastAPI Backend]
    G --> H[Execution-Ready Output]
