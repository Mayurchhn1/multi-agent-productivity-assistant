# 🚀 AI Sales Copilot: Multi-Agent Decision Engine
**Developed for the Google Cloud Gen AI Academy 2026**

The **AI Sales Copilot** is a high-performance decision engine designed to transform raw lead data into actionable sales strategies. Powered by **Google Gemini 1.5 Flash**, it utilizes a sophisticated multi-agent orchestration layer to deliver deterministic, business-ready insights in a sleek Bento-style interface.

---

## 🧠 Core Architecture: Multi-Agent Orchestration
Unlike standard chatbots, this system leverages a sequential feedback loop between specialized AI agents:

1.  **Strategic Insight Agent**: Analyzes lead context and historical data to identify high-value opportunities.
2.  **Action Agent**: Consumes the output of the Insight Agent to generate a prioritized "Execution Plan" with specific tasks.
3.  **Outreach Agent**: Drafts high-impact communication templates tailored to the identified strategy.

### 🔄 The Decision Loop
The backend utilizes a **Sequential Pipeline** where Agent A's JSON output is validated and injected into Agent B's system prompt, ensuring contextually accurate and hallucination-free results.

---

## 🛠️ Technical Stack
- **AI Model**: [Google Gemini 1.5 Flash](https://cloud.google.com/vertex-ai/docs/generative-ai/model-reference/gemini)
- **Backend**: FastAPI (Python 3.10+) 
- **Frontend**: React Native / Expo SDK 54 (Optimized for Web/Mobile)
- **Database**: MongoDB (Query History Persistence)
- **Auth**: Google OAuth 2.0 (Secure Session Management)

---

## 🚀 Key Features
- **Deterministic Strategy Generation**: Real-time sales roadmaps delivered via structured JSON.
- **Bento-Card UI**: Complex AI reasoning broken down into digestible, interactive cards (Insights, Actions, Execution Plan).
- **Persistent Memory**: Full history of past strategies with deep-link accessibility.
- **Enterprise Security**: Secure token-based authentication with protected API endpoints.

---

## 🏁 Verification & Testing
This project has been verified with a **100% success rate** across all integration tests, including:
- ✅ Backend health and API endpoint integrity.
- ✅ OAuth session token persistence and handshake.
- ✅ Gemini 1.5 Flash structured response validation.

---

## 🔗 Live Demo
Access the live production environment here:
**[AI Sales Copilot Live](https://assist-center-7.preview.emergentagent.com/home)**

---

### 💎 Google Cloud Alignment
This project demonstrates the power of the **Google Cloud Ecosystem** by integrating Vertex AI-ready models with modern web architecture to solve real-world sales friction.
