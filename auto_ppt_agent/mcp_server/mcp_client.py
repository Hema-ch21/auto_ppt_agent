import requests

def fetch_mcp_data(topic: str):
    try:
        url = f"http://localhost:8000/info?topic={topic}"
        res = requests.get(url)

        if res.status_code == 200:
            return res.json()

        return {"content": "No MCP data", "points": []}

    except Exception as e:
        return {"content": str(e), "points": []}