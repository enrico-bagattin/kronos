import requests
import json

api_key = "e8707e5c7eb2b3c36d45fe108cf994f9"
lat = "45.467175"
lon = "9.189664"

url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=metric" % (lat, lon, api_key)

response = requests.get(url)
data = json.loads(response.text)
print(data)