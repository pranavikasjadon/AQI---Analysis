import requests
import matplotlib.pyplot as plt
import time

from geopy.geocoders import Nominatim

# Get city coordinates


def get_coordinates(city):
    geolocator = Nominatim(user_agent="aqi_analysis_project")

    location = geolocator.geocode(city)

    if location:
        return location.latitude, location.longitude

    print("City not found.")
    return None, None


# Fetch AQI data


def fetch_aqi(latitude, longitude, api_key):

    url = (
        "https://api.openweathermap.org/data/2.5/air_pollution"
        f"?lat={latitude}&lon={longitude}&appid={api_key}"
    )

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    print("Unable to fetch air-quality data.")
    print("Status Code:", response.status_code)

    return None

# AQI category


def get_category(aqi):

    categories = {
        1: "Good",
        2: "Fair",
        3: "Moderate",
        4: "Poor",
        5: "Very Poor"
    }

    return categories.get(aqi, "Unknown")



# Main program


api_key = input("Enter your OpenWeatherMap API key: ")
city = input("Enter city name: ")

latitude, longitude = get_coordinates(city)

if latitude is not None:

    print("\nCity:", city)
    print("Latitude:", latitude)
    print("Longitude:", longitude)

    aqi_values = []

    print("\nCollecting AQI data...\n")

    for i in range(5):

        data = fetch_aqi(latitude, longitude, api_key)

        if data:

            aqi = data["list"][0]["main"]["aqi"]

            category = get_category(aqi)

            aqi_values.append(aqi)

            print(f"Reading {i + 1}: AQI = {aqi} ({category})")

        time.sleep(5)



    # Plot AQI trend

    if aqi_values:

        plt.plot(
            range(1, len(aqi_values) + 1),
            aqi_values,
            marker="o"
        )

        plt.title(f"AQI Trend for {city}")
        plt.xlabel("Reading")
        plt.ylabel("AQI Index (1–5)")
        plt.grid(True)

        plt.show()
