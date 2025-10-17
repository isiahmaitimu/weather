from flask import Flask, request, jsonify

app = Flask(__name__)

# 📋 Simpele database met voetbalclubs per stad
clubs = [
    {"club": "Feyenoord", "stad": "Rotterdam", "stadion": "De Kuip", "competitie": "Eredivisie"},
    {"club": "Excelsior", "stad": "Rotterdam", "stadion": "Van Donge & De Roo Stadion", "competitie": "Eredivisie"},
    {"club": "Sparta Rotterdam", "stad": "Rotterdam", "stadion": "Het Kasteel", "competitie": "Eredivisie"},
    {"club": "Ajax", "stad": "Amsterdam", "stadion": "Johan Cruijff ArenA", "competitie": "Eredivisie"},
    {"club": "AZ", "stad": "Alkmaar", "stadion": "AFAS Stadion", "competitie": "Eredivisie"},
    {"club": "PSV", "stad": "Eindhoven", "stadion": "Philips Stadion", "competitie": "Eredivisie"},
    {"club": "FC Twente", "stad": "Enschede", "stadion": "De Grolsch Veste", "competitie": "Eredivisie"},
    {"club": "FC Groningen", "stad": "Groningen", "stadion": "Euroborg", "competitie": "Eerste Divisie"},
    {"club": "ADO Den Haag", "stad": "Den Haag", "stadion": "Bingoal Stadion", "competitie": "Eerste Divisie"},
    {"club": "SC Heerenveen", "stad": "Heerenveen", "stadion": "Abe Lenstra Stadion", "competitie": "Eredivisie"},
]

@app.route("/")
def home():
    return "⚽ Welkom bij de Voetbal API! Gebruik /clubs?stad=Rotterdam om clubs op te vragen."

@app.route("/clubs")
# soccer.py

def get_clubs(city):
    """Haalt de voetbalclubs van een stad op"""
    clubs_data = {
        "Amsterdam": ["Ajax"],
        "Rotterdam": ["Feyenoord", "Excelsior", "Sparta Rotterdam"],
        "Eindhoven": ["PSV"],
        "Utrecht": ["FC Utrecht"]
    }
    
    city = city.title()  # hoofdletters goed zetten
    clubs = clubs_data.get(city, [])
    return {
        "stad": city,
        "aantal_clubs": len(clubs),
        "clubs": clubs
    }


if __name__ == "__main__":
    app.run(debug=True)

