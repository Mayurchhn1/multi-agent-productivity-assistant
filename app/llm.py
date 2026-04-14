import os
import requests

def generate_ai_response(prompt):
    try:
        response = requests.post(
            "https://api.emergent.sh/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('EMERGENT_LLM_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a helpful AI sales assistant."},
                    {"role": "user", "content": prompt}
                ]
            },
            timeout=30  # ✅ IMPORTANT
        )

        data = response.json()

        if "choices" not in data:
            return f"Error: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Server error: {str(e)}"