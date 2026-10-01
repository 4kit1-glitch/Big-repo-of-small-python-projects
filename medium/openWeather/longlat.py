# code gets the longitude and latitude of of a san francisco

import sys
import requests
import os
from dotenv import load_dotenv


city_name = "San Francisco"
state_code = "CA"
contry_code = "US"



load_dotenv("/home/kit/Kitstdios/BROSPP/medium/openWeather/appkeys.env")

def get_env(key : str, required: bool = True) -> (str | None):
    """fetch a required api key"""
    value = os.environ.get(key)

    if required and not value:
        raise SystemExit(f"missing some requred environment values {key}")
    return value

API_key = get_env("WEATHER_APP_API_KEY")
GEO_ENPOINT = f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{contry_code}&appid={API_key}"

try:
    response = requests.get(GEO_ENPOINT, timeout=10)
    response.raise_for_status()

    response_data = response.json() # might raise a json.DecodeError

    lat = response_data[0]["lat"]
    lon = response_data[0]["lon"]
    DATA_ENPOINT = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(DATA_ENPOINT, timeout=10)

    print(response.headers["content-type"])
    response.raise_for_status()

    temp = response.json()["main"]["temp"]

    print(f"temp in kelvin = {temp}")

except requests.RequestException as err:
    print(f"error occured: {err}")
    sys.exit(1)
except ValueError as err:
    print(f"unexpected error: {err}")