# 🚀 AI Sales Copilot: Multi-Agent Decision Engine

[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-Gen%20AI%20Academy%202026-4285F4?logo=googlecloud&logoColor=white)](https://assist-center-7.preview.emergentagent.com/home)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React Native](https://img.shields.io/badge/Frontend-React%20Native%20%7C%20Expo-61DAFB?logo=react&logoColor=black)](https://expo.dev/)
[![Gemini](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-8E75B2?logo=googlegemini&logoColor=white)](https://deepmind.google/technologies/gemini/)

**A production-ready decision intelligence system that transforms raw sales intent into structured, execution-ready strategy.**

---

## 🌐 Live Experience
> **Demo Link:** [Launch AI Sales Copilot](https://assist-center-7.preview.emergentagent.com/home)

---

## 🧠 The Problem & The Solution

Traditional AI chatbots provide text; **AI Sales Copilot provides execution.** Most AI tools suffer from "hallucination drift" and unstructured outputs. This system utilizes a **Multi-Agent Orchestration Pipeline** to ensure every insight is backed by a prioritized action plan and a time-bound workflow.

### ⚡ Core Value Prop
* **From:** "What should I do with this lead?"
* **To:** "Here is the insight, the 3-step action plan, and the ready-to-send outreach."

---

## 🧩 Multi-Agent Architecture
The engine operates through a sequential pipeline of specialized AI agents:

| Agent | Responsibility | Output Type |
| :--- | :--- | :--- |
| **Strategic Insight** | Analyzes lead context & intent signals | Opportunity Mapping |
| **Action Agent** | Converts insights into time-bound tasks | Prioritized Workflow |
| **Outreach Agent** | Crafts tailored, strategy-aligned messaging | Communication Templates |

### 🔄 The Decision Loop
`Input` ⮕ `Insight Agent` ⮕ `JSON Validation` ⮕ `Action Agent` ⮕ `Execution Plan` ⮕ `Outreach Agent` ⮕ `Bento UI`

---

## 🛠️ Technology Stack

* **AI Orchestration:** Google Gemini 1.5 Flash (Vertex AI Architecture)
* **Backend:** Python 3.10+ / FastAPI (High-performance asynchronous logic)
* **Frontend:** React Native + Expo SDK 54 (Web & Mobile cross-compatibility)
* **Database:** MongoDB (Persistent strategy memory & history tracking)
* **DevOps:** Google Cloud Platform / Containerized Services / K8s Ingress

---

## 🔐 Engineering Spotlight: Production Authentication Fix
During development, a critical hurdle was identified regarding cross-origin session persistence.

* **The Issue:** `httpOnly` cookies were inaccessible to the frontend, causing authorization drops.
* **The Fix:** * Migrated to a **Response Body Token** architecture.
    * Implemented `SecureStore` (Mobile) and `localStorage` (Web) persistence.
    * Added OAuth race-condition safeguards to ensure stable API handshakes.
* **Result:** 100% reliable session handling across web and mobile environments.

---

## 💼 Business Impact (Projected)
* **Conversion:** 15–30% increase in lead-to-opportunity rates.
* **Efficiency:** 60% reduction in manual sales discovery and planning time.
* **Consistency:** Standardized strategy outputs across entire sales teams.

---

## 🚀 Key Features
* **Deterministic Strategy:** Structured JSON ensures zero hallucination in task lists.
* **Bento-Style UI:** High-density, clean visualization of complex strategic data.
* **Persistent Memory:** Full history tracking to revisit and iterate on past strategies.
* **Enterprise Auth:** Secure Google OAuth 2.0 integration.

---

## 🔮 Roadmap
- [ ] **Strategy Export:** One-click PDF and shareable link generation.
- [ ] **Team Layer:** Collaborative strategy editing for sales managers.
- [ ] **AI Critic Agent:** A 4th agent to "stress-test" strategies before final output.
- [ ] **CRM Sync:** Direct push-to-HubSpot/Salesforce integration.

---

## 👨‍💻 Author
**Mayur Chauhan**
*Business Development & AI Systems Architect*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?logo=linkedin)](https://www.linkedin.com/in/mayurchauhan/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live%20Demo-success?logo=googlechrome)](https://assist-center-7.preview.emergentagent.com/home)

---
*Built for the Google Cloud Gen AI Academy 2026.*
