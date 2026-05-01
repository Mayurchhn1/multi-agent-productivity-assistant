from app.llm_router import route_llm
from app.utils import extract_json
from app.decision_engine import get_context


def generate_plan(user_input: str, intent: str):
    # -----------------------------
    # 📊 GET BUSINESS CONTEXT
    # -----------------------------
    context = get_context(limit=5)

    deals = context.get("top_deals", [])
    pipeline = context.get("pipeline", {})

    # -----------------------------
    # 🧠 CONTEXT-AWARE PROMPT
    # -----------------------------
    prompt = f"""
You are a senior sales execution strategist.

User intent: {intent}
User input: {user_input}

Active deals:
{deals}

Pipeline summary:
{pipeline}

Generate a HIGH-IMPACT execution plan.

RULES:
- Max 5 tasks
- First task = highest revenue impact
- Use deal context if available
- Be specific and outcome-driven
- Avoid generic advice

Return STRICT JSON:

{{
  "mode": "{intent}",
  "summary": "1–2 line sharp summary",
  "plan": [
    {{
      "task": "Specific action tied to real deal",
      "time": "9:00 AM",
      "type": "Execution | Deep Work | Follow-up | Review",
      "priority": 1
    }}
  ]
}}
"""

    # -----------------------------
    # 🤖 CALL LLM
    # -----------------------------
    raw = route_llm([
        {"role": "system", "content": "Return ONLY valid JSON."},
        {"role": "user", "content": prompt}
    ])

    print("\n--- RAW LLM OUTPUT ---\n", raw, "\n----------------------\n")

    # -----------------------------
    # 🔍 PARSE RESPONSE
    # -----------------------------
    parsed = extract_json(raw) if raw else None

    # -----------------------------
    # 🛡️ FALLBACK SAFETY
    # -----------------------------
    if not parsed or "plan" not in parsed:
        return {
            "mode": intent,
            "summary": "Executing prioritized actions based on pipeline opportunities.",
            "plan": [
                {
                    "task": f"Contact highest-value deal: {deals[0]['client_name']}" if deals else f"Start executing: {user_input}",
                    "time": "9:00 AM",
                    "type": "Execution",
                    "priority": 1
                },
                {
                    "task": "Follow up with top 3 prospects",
                    "time": "11:00 AM",
                    "type": "Follow-up",
                    "priority": 2
                }
            ]
        }

    # -----------------------------
    # 🧹 CLEAN OUTPUT
    # -----------------------------
    clean_plan = []

    for i, item in enumerate(parsed.get("plan", [])[:5]):
        clean_plan.append({
            "task": item.get("task", f"Task {i+1}"),
            "time": item.get("time", "TBD"),
            "type": item.get("type", "Execution"),
            "priority": min(item.get("priority", i + 1), 3)
        })

    parsed["plan"] = clean_plan

    return parsed