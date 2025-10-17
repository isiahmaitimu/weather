import requests

def get_statistics(city):
    """
    Haalt statistieken op van een stad via de GeoDB Cities API.
    Retourneert een dict met bevolking en coördinaten.
    """
    url = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities"
    querystring = {"namePrefix": city}
    headers = {
        "x-rapidapi-key": "9cfe675b2amsh12cf2d2e12087b6p1aeb0djsnca9311d8e302",
        "x-rapidapi-host": "wft-geo-db.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Controleer of de API goed reageert
    if response.status_code != 200:
        raise Exception(f"Fout bij API-aanroep: {response.status_code}")

    data = response.json()["data"]

    if not data:
        raise Exception(f"Geen gegevens gevonden voor stad: {city}")

    stad_data = data[0]

    # Bouw een net dictionary met relevante info
    return {
        "stad": stad_data.get("city", city),
        "land": stad_data.get("country", "Onbekend"),
        "populatie": stad_data.get("population", "Onbekend"),
        "coordinaten": {
            "latitude": stad_data.get("latitude"),
            "longitude": stad_data.get("longitude")
        }
    }
