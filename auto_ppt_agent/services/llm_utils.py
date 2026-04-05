# services/llm_utils.py
# -----------------------------------
# Utility to safely parse LLM JSON output
# -----------------------------------

import json

def safe_parse(text):
    try:
        return json.loads(text)
    except:
        return None