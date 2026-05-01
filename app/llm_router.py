import os
import requests

print("🔥 LLM ROUTER FILE LOADED 🔥")


# -----------------------------
# 🚀 MAIN LLM CALL
# -----------------------------
def route_llm(messages):
    try:
        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            print("❌ Missing OPENROUTER_API_KEY")
            return None

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": messages,
                "temperature": 0.7
            },
            timeout=30
        )

        if response.status_code != 200:
            print("❌ HTTP ERROR:", response.text)
            return None

        data = response.json()

        content = data["choices"][0]["message"]["content"]

        print("\n📥 LLM RESPONSE:", content)

        return content

    except Exception as e:
        print("❌ LLM ERROR:", str(e))
        return None


# -----------------------------
# ❤️ HEALTH CHECK
# -----------------------------
def run_llm_healthcheck():
    if not os.getenv("OPENROUTER_API_KEY"):
        return {"status": "missing_key"}

    return {"status": "ok"}
