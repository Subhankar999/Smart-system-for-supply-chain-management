import requests

api_key = "AIzaSyCVxoSGiTtDDdCESnG6Aq0GQtZNt4b3Nl0"
# Our fleet of trucks across India
fleet = [
    {"truck_id": "TRK-001", "location": "Kolkata", "cargo": "Electronics"},
    {"truck_id": "TRK-002", "location": "Delhi", "cargo": "Textiles"},
    {"truck_id": "TRK-003", "location": "Mumbai", "cargo": "Medicines"},
    {"truck_id": "TRK-004", "location": "Bangalore", "cargo": "Coffee"}
]

print(f"{'TRUCK ID':<10} | {'CITY':<12} | {'TEMP':<8} | {'CONDITION':<15} | {'STATUS'}")
print("-" * 70)

for truck in fleet:
    city = truck['location']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    data = requests.get(url).json()

    if data.get("cod") == 200:
        temp = data['main']['temp']
        weather = data['weather'][0]['main']

        # LOGISTICS LOGIC: Define what counts as a "Delay"
        # If it's Rain, Thunderstorm, or extreme heat/cold, flag it!
        if weather in ["Rain", "Thunderstorm", "Snow", "Smoke", "Dust"]:
            status = "⚠️ DELAY RISK"
        elif temp > 40:
            status = "🔥 HEAT ALERT"
        else:
            status = "✅ ON TIME"

        print(f"{truck['truck_id']:<10} | {city:<12} | {temp:<6}°C | {weather:<15} | {status}")
    else:
        print(f"Error fetching data for {city}")
