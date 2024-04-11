import requests

def get_weather(city):
    response = requests.get(f"https://example.com/weather/{city}")
    return response.json()['weather']
