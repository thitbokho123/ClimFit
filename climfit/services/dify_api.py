import requests, os
from dotenv import load_dotenv

load_dotenv()
_DIFY = os.getenv("DIFY_API_KEY")
_URL  = "https://api.dify.ai/v1/completion-messages"

def get_outfit_advice(weather: dict, gender: str, age: int, style: str) -> str:
    payload = {
        "inputs": {
            "weather_description": weather["desc"],
            "temperature": f"{weather['temp']} °C",
            "gender": gender,
            "age": str(age),
            "style": style,
        },
        "response_mode": "blocking",
        "user": "streamlit-demo"
    }
    headers = {
        "Authorization": f"Bearer {_DIFY}",
        "Content-Type": "application/json"
    }

    try:
        resp = requests.post(_URL, json=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        core = resp.json().get("answer", "").strip()
        if not core:
            raise RuntimeError("Empty answer from Dify")

    except Exception as e:
        print("Dify error:", e)
        core = "A stylish and comfortable outfit"

    prompt = (
        f"{gender} outfit for a {age}-year-old, {style} style. "
        f"{core} "
    )
    return prompt[:1000]
