# api key e7e7b64e92164cde582d416840ef15f6
import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY = "Sunnyvale"

def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

temp_fahrenheit_rounded = round(int(temp_fahrenheit))
temp_celsius_rounded = round(int(temp_celsius))
feels_like_fahrenheit_rounded = round(int(feels_like_fahrenheit))
feels_like_celsius_rounded = round(int(feels_like_celsius))




print(f"Temperature in {CITY}: {temp_celsius_rounded:.2f}ºC or {temp_fahrenheit_rounded}ºF")
print(f"Temperature in {CITY}: feels like {feels_like_celsius_rounded:.2f}ºC or {feels_like_fahrenheit_rounded}ºF")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sun rises in {CITY} at {sunrise_time} local time.")
print(f"Sun sets in {CITY} at {sunset_time} local time.")