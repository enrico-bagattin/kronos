import requests

'''
This module is used in order to retrive the data from the OpenWeather service
'''
API_KEY = "e8707e5c7eb2b3c36d45fe108cf994f9"  # key needed to call OpenWeather apis

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

    return {
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "temperature": data["main"]["temp"]
    }