import json
import re

def extract_json(text: str):
    try:
        text = re.sub(r"```json|```", "", text).strip()

        try:
            return json.loads(text)
        except:
            pass

        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            return json.loads(text[start:end + 1])

        return None

    except:
        return None