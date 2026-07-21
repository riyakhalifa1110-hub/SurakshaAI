import os
import json
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from app.services.sms_prompt import SMS_PROMPT

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_sms(message, language="en"):

    language_map = {
        "en": "English",
        "hi": "Hindi",
        "gu": "Gujarati"
    }

    output_language = language_map.get(language, "English")

    prompt = f"""
{SMS_PROMPT}

IMPORTANT:

The user has selected: {output_language}

Write ALL text inside "reason" and "advice" in {output_language}.

Keep the JSON keys in English.

SMS:

{message}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are SurakshaAI.

The user's preferred language is {output_language}.

IMPORTANT:
- Write every sentence in "reason" in {output_language}.
- Write every sentence in "advice" in {output_language}.
- Keep JSON keys in English.
- Return ONLY valid JSON.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        text = response.choices[0].message.content.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "").replace("```", "").strip()

        elif text.startswith("```"):
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        return {
            "risk": "Error",
            "score": 0,
            "reason": [str(e)],
            "advice": [
                "Please try again."
            ]
        }