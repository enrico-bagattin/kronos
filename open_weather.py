"""
This module is used in order to retrieve the data from the OpenWeather service
"""

import requests

API_KEY = "e8707e5c7eb2b3c36d45fe108cf994f9"  # key needed to call OpenWeather apis
WEATHER_ICONS = {
    "01d": "☀️",
    "02d": "⛅️",
    "03d": "☁️",
    "04d": "☁️",
    "09d": u"\U0001F327",
    "10d": u"\U0001F326",
    "11d": "⛈",
    "13d": "❄️",
    "50d": u"\U0001F32B",
    "01n": "🌑",
    "02n": u"\U0001F311",
    "03n": "☁️",
    "04n": "☁️",
    "09n": u"\U0001F327",
    "10n": "☔️",
    "11n": "⛈",
    "13n": "❄️",
    "50n": u"\U0001F32B"
}


def get_weather(lat, lon):
    """
    Get weather information by position
    :param lat: position latitude
    :param lon: position longitude
    :return: json with weather info
    """
    URL = "https://api.openweathermap.org/data/2.5/weather"  # api-endpoint

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }

    # sending get request and saving the response as response object
    response = requests.get(url=URL, params=PARAMS)

    # extracting data in json format
    data = response.json()

    if data['cod'] != 200:
        raise InvalidDataError(data['message'])
    return {
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"].title(),
        "temperature": str(data["main"]["temp"]) + '°C',
        "icon": WEATHER_ICONS[data["weather"][0]["icon"]]
    }


class InvalidDataError(BaseException):
    """
    Handle errors provided by OpenWeather
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
