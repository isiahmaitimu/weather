import requests
import datetime

API_KEY = "cfd0faf8ecb81ce3ca65df4c89b40a7e"

def get_Weather(city):
    """
    Haalt weerinformatie op van OpenWeatherMap voor een opgegeven stad.
    Retourneert een dictionary met temperatuur, gevoelstemperatuur, vochtigheid, enz.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=nl"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Fout bij ophalen van weer: {response.text}")

    data = response.json()

    return {
        "temperatuur": data["main"]["temp"],
        "gevoelstemperatuur": data["main"]["feels_like"],
        "vochtigheid": data["main"]["humidity"],
        "druk": data["main"]["pressure"],
        "wind": {
            "snelheid": data["wind"]["speed"],
            "richting": data["wind"]["deg"]
        },
        "beschrijving": data["weather"][0]["description"],
        "zonsopkomst": datetime.datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M:%S"),
        "zonsondergang": datetime.datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M:%S")
    }
