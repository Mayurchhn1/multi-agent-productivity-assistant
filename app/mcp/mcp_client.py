import requests

def fetch_data(query):
    try:
        res = requests.get(
            f"https://api.duckduckgo.com/?q={query}&format=json"
        )
        data = res.json()
        return data.get("Abstract", "No extra info found")
    except:
        return "External data unavailable"
