import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "f107fd152136175d26fe526aec88875d"


weather_parameter = {
    "lat":20.593683,
    "lng":78.962883,
    "appid":api_key,
    "cnt":4,
}

response = requests.get(OWM_Endpoint, params=weather_parameter)
response.raise_for_status()
weather_data = response.json{}
print(weather_data)