import os
import requests
import traceback

def generate_ai_response(prompt: str):
    try:
        res = requests.post(
            "https://api.emergent.sh/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('EMERGENT_LLM_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You output ONLY valid JSON."},
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=30
        )

        # ✅ Check HTTP status
        if res.status_code != 200:
            return {
                "error": True,
                "message": f"HTTP {res.status_code}: {res.text}"
            }

        data = res.json()

        # ✅ Validate structure
        if "choices" not in data:
            return {
                "error": True,
                "message": f"Invalid response: {data}"
            }

        content = data["choices"][0]["message"]["content"].strip()

        return {
            "error": False,
            "content": content
        }

    except Exception as e:
        traceback.print_exc()
        return {
            "error": True,
            "message": f"Server error: {str(e)}"
        }