from flask import Flask, request, jsonify
from weather import getWeather
from statistics import getStatistics

app = Flask(__name__)

@app.route("/cityinfo", methods=["GET"])
def get_city_data():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "Geen stad opgegeven"}), 400

    try:
        stats = getStatistics(city)
        weather = getWeather(city)

        # Combineer alles in één object
        combined = {**stats, **weather}

        return jsonify(combined)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)