import os
import json
import re
import traceback
import requests
from openai import OpenAI
from app.db.database import save_plan

# -----------------------------
# ⚙️ Provider Switch
# -----------------------------
USE_PROVIDER = os.getenv("LLM_PROVIDER", "ollama")


# -----------------------------
# 🌐 OpenRouter (Cloud)
# -----------------------------
def call_openrouter(prompt: str):
    try:
        client = OpenAI(
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )

        response = client.chat.completions.create(
            model="openai/gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Return ONLY valid JSON."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("OpenRouter Error:", str(e))
        return ""


# -----------------------------
# 🖥️ Ollama (Local)
# -----------------------------
def call_ollama(prompt: str):
    try:
        res = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "phi3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        data = res.json()
        return data.get("response", "")

    except Exception as e:
        print("Ollama Error:", str(e))
        return ""


# -----------------------------
# 🔍 JSON Extraction
# -----------------------------
def extract_json(text: str):
    try:
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL).strip()

        # direct parse
        try:
            return json.loads(text)
        except:
            pass

        # fallback extraction
        matches = re.findall(r"\{[\s\S]*\}", text)

        for m in matches:
            try:
                return json.loads(m)
            except:
                continue

        return None

    except Exception:
        return None


# -----------------------------
# 🧠 MAIN AGENT
# -----------------------------
def run_agent(user_input: str):
    try:
        # -----------------------------
        # 💼 CONSULTANT PROMPT
        # -----------------------------
        prompt = f"""
You are a high-performance sales execution consultant.

Return ONLY valid JSON.

{{
  "mode": "sales | work | learning | general",
  "summary": "Outcome-focused insight",
  "reasoning": "Why this plan works",
  "confidence": 0.85,
  "plan": [
    {{
      "task": "Specific action",
      "time": "Exact time",
      "type": "Execution | Follow-up | Deep Work | Review",
      "priority": 1
    }},
    {{
      "task": "Next step",
      "time": "Time",
      "type": "Execution",
      "priority": 2
    }}
  ]
}}

Rules:
- Max 5 tasks
- No generic advice
- Focus on real execution

User:
{user_input}
"""

        # -----------------------------
        # 🔁 CALL PRIMARY PROVIDER
        # -----------------------------
        if USE_PROVIDER == "ollama":
            raw_content = call_ollama(prompt)

            # fallback if weak response
            if not raw_content or len(raw_content) < 50:
                print("⚡ Switching to OpenRouter fallback...")
                raw_content = call_openrouter(prompt)
        else:
            raw_content = call_openrouter(prompt)

        print("\n--- RAW AI RESPONSE ---\n", raw_content, "\n----------------------\n")

        # -----------------------------
        # 🔍 PARSE
        # -----------------------------
        parsed = extract_json(raw_content)

        # -----------------------------
        # 🔄 RETRY (STRICT)
        # -----------------------------
        if not parsed:
            retry_prompt = f"""
ONLY JSON.

{{
  "mode": "sales",
  "summary": "short summary",
  "reasoning": "why it works",
  "confidence": 0.8,
  "plan": [
    {{
      "task": "action",
      "time": "now",
      "type": "Execution",
      "priority": 1
    }}
  ]
}}

User: {user_input}
"""
            raw_content = call_openrouter(retry_prompt)
            parsed = extract_json(raw_content)

        # -----------------------------
        # 🔒 FINAL FALLBACK
        # -----------------------------
        if not parsed or "plan" not in parsed:
            fallback = {
                "mode": "sales",
                "summary": "Start execution immediately to build momentum.",
                "reasoning": "Action reduces uncertainty and builds clarity.",
                "confidence": 0.5,
                "plan": [
                    {
                        "task": f"Start working on: {user_input}",
                        "time": "Now",
                        "type": "Execution",
                        "priority": 1
                    }
                ]
            }

            save_plan(user_input, fallback)
            return fallback

        # -----------------------------
        # 🛡️ CLEAN STRUCTURE
        # -----------------------------
        parsed["mode"] = parsed.get("mode", "general")
        parsed["summary"] = parsed.get("summary", "")
        parsed["reasoning"] = parsed.get("reasoning", "")
        parsed["confidence"] = parsed.get("confidence", 0.75)

        clean_plan = []
        for i, item in enumerate(parsed.get("plan", [])[:5]):
            clean_plan.append({
                "task": item.get("task", f"Task {i+1}"),
                "time": item.get("time", "TBD"),
                "type": item.get("type", "Execution"),
                "priority": item.get("priority", i + 1)
            })

        parsed["plan"] = clean_plan

        # -----------------------------
        # 💾 SAVE TO DATABASE (CRITICAL)
        # -----------------------------
        save_plan(user_input, parsed)

        return parsed

    except Exception:
        print("\n!!! RUN_AGENT ERROR !!!\n")
        traceback.print_exc()

        error_response = {
            "mode": "error",
            "summary": "AI failed to generate a valid execution plan.",
            "reasoning": "",
            "confidence": 0,
            "plan": []
        }

        save_plan(user_input, error_response)
        return error_response