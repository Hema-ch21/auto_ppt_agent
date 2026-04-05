import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROK_API_KEY = os.getenv("xai-hdmCCnVdwlZop9mUd8lYxvYPHC068WmK0T4bZngvDMVJnOWFFaX53lBXsW1rIekVWoFR12ei6StkjRNw")

def call_grok(prompt: str):

    if not GROK_API_KEY:
        return '{"slides":[{"title":"Error","content":"Missing API key"}]}'

    url = "https://api.x.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-1",
        "messages": [
            {"role": "system", "content": "Return ONLY valid JSON for PPT slides."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    # 🔥 DEBUG (IMPORTANT)
    try:
        data = response.json()
    except:
        return '{"slides":[{"title":"Error","content":"Invalid JSON response from API"}]}'

    # 🔥 CHECK ERROR FIRST
    if "choices" not in data:
        return f'{{"slides":[{{"title":"API Error","content":"{data}"}}]}}'

    return data["choices"][0]["message"]["content"]