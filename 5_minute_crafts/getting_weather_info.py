import requests
from pprint import pprint

API_KEY = '421e918a8e57b10162e406952160aa7b'

city = input("Enter a city: ")

base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

weather_data = requests.get(base_url).json()

pprint(weather_data)