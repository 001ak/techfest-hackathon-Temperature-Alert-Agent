# weather_api.py

import requests
from decouple import config  # Import the 'config' function from 'python-decouple'

# Retrieve the Weather API key from the environment variable
WEATHER_API_KEY = config("WEATHER_API_KEY")

def fetch_temperature(location):
    # weather API URL
    api_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}"

    # Include the API key in the request headers
    headers = {
        "Authorization": f"Bearer {WEATHER_API_KEY}"
    }

    try:
        response = requests.get(api_url, headers=headers)
        data = response.json()
        current_temperature = data["current"]["temp_c"]

        # Print the temperature data
        print(f"Current Temperature in {location}: {current_temperature}°C")

        return current_temperature
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
        return None
