import json
import re
from llm.ollama_client import query_llm


def extract_first_json_array(text):
    """
    Robust JSON extractor using bracket counting
    """

    start = text.find("[")
    if start == -1:
        return None

    bracket_count = 0

    for i in range(start, len(text)):
        if text[i] == "[":
            bracket_count += 1
        elif text[i] == "]":
            bracket_count -= 1

            if bracket_count == 0:
                try:
                    return json.loads(text[start:i+1])
                except Exception as e:
                    print("JSON parse error:", e)
                    return None

    return None


def generate_test_plan(user_input, html=None):

    prompt = f"""
You are an expert UI testing agent.

STRICT RULES:
- Output ONLY ONE JSON ARRAY
- DO NOT generate multiple lists
- NO explanation
- Actions allowed: open_url, type, click, verify

- For verify ONLY use:
    "dashboard" OR "login_page"

- Use XPath for elements
- Do NOT generate multiple plans

HTML:
{html[:6000] if html else ""}

USER REQUEST:
{user_input}

OUTPUT:
[
  {{"action": "open_url", "target": "/web/index.php/auth/login", "value": ""}},
  {{"action": "type", "target": "//input[@name='username']", "value": "Admin"}},
  {{"action": "type", "target": "//input[@name='password']", "value": "admin123"}},
  {{"action": "click", "target": "//button[@type='submit']", "value": ""}},
  {{"action": "verify", "target": "dashboard", "value": ""}}
]
"""

    response = query_llm(prompt)

    # 🔥 FIXED PARSER
    plan = extract_first_json_array(response)

    if not plan:
        print("❌ Failed to extract valid JSON")
        print("RAW:", response)
        return []

    # Clean
    cleaned_plan = []
    for step in plan:
        cleaned_plan.append({
            "action": step.get("action", "").strip(),
            "target": step.get("target", "").strip(),
            "value": step.get("value", "").strip()
        })

    return cleaned_plan