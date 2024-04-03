"""
This app will collect weather information for a given location, hourly
Using API provided by
https://openweathermap.org/api
There's a limit for 1000 request per day
"""
import requests
import os

# TODO: check weather of cities passing by of my road-trip for forecast
# TOUSE: run this in bash
# export OPENWEATHERMAP_API_KEY='your_api_key'


OPEN_WEATHER_DOMAIN = "https://api.openweathermap.org/data/2.5/weather"

# this is the free version, which they call CURRENT
# https://openweathermap.org/current


# CITY: (latitude, longtitude)
city_coord_dict = {
    "BOSTON": (42.361145, -71.057083),
    "YANTAI": (37.47649, 121.44081),
    "MIAMI": (25.793449, -80.139198)
}

# make the call
def get_weather(api_key: str, city: str):
    """
    inputs:
        api_key: openweather api key
        city   : city name
    """
    city = city.upper()
    url = f"{OPEN_WEATHER_DOMAIN}?lat={city_coord_dict[city][0]}&lon={city_coord_dict[city][1]}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

def convert_temp(temp: int, fromUnit: str = 'K', toUnit: str = 'C'):
    # Round is needed as float calculation breaks the number in python
    if fromUnit == 'K' and toUnit =='C':
        return round(temp - 273.15, 2)
    elif fromUnit == 'C' and toUnit =='K':
        return round(temp + 273.15, 2)
    elif fromUnit == toUnit:
        return temp
    else:
        return "Invalid conversion"


def main():
    api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
    if not api_key:
        print("Error: OpenWeatherMap API Key not found.")
        return

    city = "Boston"
    weather_data = get_weather(api_key, city)
    if weather_data:
        print("Weather data for:", city)
        print("Weather:", weather_data['weather'][0]['main'])
        temp_k = weather_data['main']['temp']
        print("Temperature:", convert_temp(temp_k))
        print("Humidity:", weather_data['main']['humidity'])
        print("Wind Speed:", weather_data['wind']['speed'])
    else:
        print("Failed to retrieve weather data.")

if __name__ == "__main__":
    main()