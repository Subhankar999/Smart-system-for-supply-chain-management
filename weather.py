import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Logistics Monitor", layout="wide")
st.title("🚛 Real-Time Logistics Control Tower")

# 1. Weather Logic (Point B)
api_key = "AIzaSyCVxoSGiTtDDdCESnG6Aq0GQtZNt4b3Nl0"
cities = ["Kolkata", "Delhi", "Mumbai"]

# 2. Real-Time Simulation (Point C)
st.subheader("Live Fleet & Traffic Status")
cols = st.columns(3)

for i, city in enumerate(cities):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    data = requests.get(url).json()

    if data.get("cod") == 200:
        weather = data['weather'][0]['main']

        # POINT C LOGIC: Simulate traffic based on weather
        if weather in ["Rain", "Haze", "Smoke"]:
            traffic_level = "High Congestion 🔴"
            delay = "45 mins"
        else:
            traffic_level = "Clear Flow 🟢"
            delay = "5 mins"

        with cols[i]:
            st.info(f"**City: {city}**")
            st.write(f"Weather: {weather}")
            st.write(f"Traffic: {traffic_level}")
            st.write(f"Est. Delay: {delay}")

# 3. Mapping (Point C)
map_data = pd.DataFrame({
    'lat': [22.57, 28.61, 19.07],
    'lon': [88.36, 77.20, 72.87]
})
st.map(map_data)
