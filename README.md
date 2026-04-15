# 🚀 AI Sales Copilot: Multi-Agent Decision Engine
**Developed for the Google Cloud Gen AI Academy 2026**

The **AI Sales Copilot** is a high-performance decision engine that transforms raw lead data into actionable sales strategies. Powered by **Google Gemini 1.5 Flash**, it uses a sequential multi-agent orchestration layer to deliver deterministic, business-ready insights.

---

## 🧠 Core Architecture: Multi-Agent Orchestration
Unlike traditional chatbots, this system separates reasoning into specialised agents:

1. **Strategic Insight Agent**: Analyses lead context, historical behaviour, and sentiment to identify the core opportunity.
2. **Action Agent**: Consumes the output of the Insight Agent to generate a prioritised list of tasks (e.g., follow-ups, qualification steps).
3. **Execution Agent**: Drafts high-impact outreach templates based on the final strategy.

### 🔄 The Feedback Loop
The backend utilises a **Sequential Pipeline** where Agent A's JSON output is validated and injected into Agent B's system prompt, ensuring zero context loss.

---

## 🛠️ Technical Stack
- **AI Model**: [Google Gemini 1.5 Flash](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)
- **Backend**: FastAPI (Python 3.10+)
- **Frontend**: React Native / Expo (Bento-style UI)
- **Database**: MongoDB (Query History Persistence)
- **Auth**: Google OAuth 2.0 (via Emergent Identity)

---

## 🚀 Key Features
- **Dynamic Strategy Generation**: Real-time sales roadmaps in <15 seconds.
- **Bento-Card UI**: Clean, digestible interface for complex AI data.
- **Secure Persistence**: Full query history with deletion and profile management.
- **Enterprise Ready**: Structured JSON responses for predictable integration.

---

## 🏁 Getting Started
1. **Clone the Repo**: `git clone [Your-Repo-Link]`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Run Locally**: `python3 main.py`
4. **Access the Web UI**: [Live Demo Link](https://task-automation-ai-10.preview.emergentagent.com/home)

---

### 💎 Google Cloud Integration
This project demonstrates the power of **Vertex AI** for agentic workflows. By leveraging Gemini's structured output mode, we eliminate non-deterministic "hallucinations" and provide reliable business logic.
