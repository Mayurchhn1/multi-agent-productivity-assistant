import json
import re
import os
from openai import OpenAI
import traceback

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# -----------------------------
# 🔍 Safe JSON Extraction
# -----------------------------
def extract_json(text: str):
    try:
        # Remove markdown blocks (```json ... ```)
        text = re.sub(r"```json|```", "", text).strip()

        # 1️⃣ Try direct parsing
        try:
            return json.loads(text)
        except:
            pass

        # 2️⃣ Extract full JSON block
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            return json.loads(text[start:end + 1])

        return None

    except Exception:
        return None


# -----------------------------
# 🧠 Main AI Execution Engine
# -----------------------------
def run_agent(user_input: str):
    try:
        prompt = f"""
You are an elite execution strategist.

Convert user intent into a HIGH-QUALITY execution plan.

User Input:
{user_input}

Return STRICT JSON ONLY:

{{
  "mode": "sales | work | learning | general",
  "summary": "1–2 line sharp summary",
  "plan": [
    {{
      "task": "Specific action (clear + executable)",
      "time": "realistic time (e.g. 9:00 AM)",
      "type": "Deep Work | Execution | Follow-up | Review",
      "priority": 1
    }}
  ]
}}

RULES:
- Max 5 tasks
- First task = highest impact
- Tasks must follow logical sequence
- No generic advice (avoid: research, analyze, plan)
- Each task must be immediately actionable
- Output MUST be valid JSON only
"""

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You output ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
        )

        raw_content = response.choices[0].message.content.strip()

        # 🔍 Debug log (visible in Render logs)
        print("\n--- RAW AI RESPONSE ---\n", raw_content, "\n----------------------\n")

        parsed = extract_json(raw_content)

        # -----------------------------
        # 🔒 HARD FALLBACK (CRITICAL)
        # -----------------------------
        if not parsed or "plan" not in parsed:
            return {
                "mode": "general",
                "summary": "Starting with a simple execution plan to build momentum.",
                "plan": [
                    {
                        "task": f"Start working on: {user_input}",
                        "time": "Now",
                        "type": "Execution",
                        "priority": 3
                    }
                ]
            }

        # -----------------------------
        # 🛡️ STRUCTURE SAFETY
        # -----------------------------
        parsed["mode"] = parsed.get("mode", "general")
        parsed["summary"] = parsed.get("summary", "")

        plan = parsed.get("plan", [])
        if not isinstance(plan, list):
            plan = []

        # Limit to 5 tasks
        parsed["plan"] = plan[:5]

        return parsed

    except Exception as e:
    print("\n!!! RUN_AGENT ERROR !!!\n")
    traceback.print_exc()

    return {
        "mode": "error",
        "summary": "AI failed to generate a valid execution plan. Try again.",
        "plan": []
    }