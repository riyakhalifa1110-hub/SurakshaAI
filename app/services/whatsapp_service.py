import os
import json
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from app.services.whatsapp_prompt import WHATSAPP_PROMPT

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_whatsapp(message, language="en"):

    # Language mapping
    language_map = {
        "en": "English",
        "hi": "Hindi",
        "gu": "Gujarati"
    }

    output_language = language_map.get(language, "English")

    prompt = f"""
{WHATSAPP_PROMPT}

WhatsApp Chat:

{message}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"""
You are a cybersecurity expert.

The user has selected the language: {output_language}.

IMPORTANT RULES:
1. The JSON keys MUST remain in English:
   - risk
   - score
   - reason
   - advice

2. Every sentence inside "reason" MUST be written in {output_language}.

3. Every sentence inside "advice" MUST be written in {output_language}.

4. Do NOT reply in English if the selected language is Hindi or Gujarati.

5. Return ONLY valid JSON.

6. Never return Markdown.
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

    