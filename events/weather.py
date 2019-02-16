# The Dark Sky Weather API is used to get the weather data
import requests
import json
from .keys import weather_key

# This function returns the Weather data in JSON format
def city_weather(lat, long):
    data = requests.get('https://api.darksky.net/forecast/{}/{},{}'.format(weather_key, lat, long))
    json_data = json.loads(data.content)
    return json_data