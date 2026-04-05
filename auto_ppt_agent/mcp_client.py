import requests

def fetch_mcp_data(topic: str):
    url = f"http://localhost:8000/info?topic={topic}"

    try:
        res = requests.get(url)

        if res.status_code == 200:
            return res.json()

        return {"points": ["No MCP data found"]}

    except Exception as e:
        return {"points": [str(e)]}