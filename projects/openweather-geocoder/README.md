# OpenWeather Geocoder

Looks up coordinates for a configured city with OpenWeather's geocoding API, then requests its current temperature. Requires an internet connection and an OpenWeather API key.

## Setup

Install the third-party packages:

```bash
python -m pip install requests python-dotenv
```

Create an untracked `appkeys.env` file in this directory with:

```dotenv
WEATHER_APP_API_KEY=your_openweather_api_key
```

## Run

```bash
python longlat.py
```

The script currently requests weather for San Francisco and prints the temperature in Kelvin. Never commit the API key; `*.env` files are excluded by the repository `.gitignore`.