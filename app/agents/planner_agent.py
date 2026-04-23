from app.llm_router import route_llm
from app.orchestrator import extract_json


def generate_plan(user_input: str, intent: str):
    prompt = f"""
You are an elite execution strategist.

User intent: {intent}

User Input:
{user_input}

Return STRICT JSON:

{{
  "mode": "{intent}",
  "summary": "1–2 line summary",
  "plan": [
    {{
      "task": "Specific action",
      "time": "realistic time",
      "type": "Execution | Deep Work | Follow-up | Review",
      "priority": 1
    }}
  ]
}}

RULES:
- Max 5 tasks
- First task = highest impact
- Must be actionable
"""

    raw = route_llm([
        {"role": "system", "content": "You output ONLY valid JSON."},
        {"role": "user", "content": prompt}
    ])

    if not raw:
        return None

    return extract_json(raw)