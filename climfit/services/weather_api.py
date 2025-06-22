import requests, os
from dotenv import load_dotenv

load_dotenv()
_API = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city: str) -> dict:
    url = ("http://api.openweathermap.org/data/2.5/weather"
           f"?q={city}&appid={_API}&units=metric&lang=en")
    res = requests.get(url, timeout=10)
    if res.status_code != 200:
        msg = res.json().get("message", "Unknown error")
        raise RuntimeError(f"OpenWeather: {msg}")
    data = res.json()
    return {
        "temp": round(data["main"]["temp"]),
        "desc": data["weather"][0]["description"].title()
    }
