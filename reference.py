import requests
import datetime as dt

CITY = "Sunnyvale"


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "e7e7b64e92164cde582d416840ef15f6"
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

#Less than 25 degrees. Light to medium coat: 25 to 44 degrees. Fleece: 45 to 64 degrees

Deg45_64 = "We recommend that you wear a light jacket when going out in this weather. "
Deg25_44 = "We recommend that you wear a heavy jacket when going out in this weather. "
Deg25bel = "We recommend wearing a winter jacket when going out in this weather."
dont_wear_jacket = "A jacket is not recommended when going out in this weather. "



print(temp_fahrenheit_rounded)
print(feels_like_fahrenheit)
print(wind_speed)
print(humidity)
print(description)




BASE2_URL = "http://api.openweathermap.org/data/2.5/air_pollution?"
#url2 = BASE2_URL + "appid=" + API_KEY + "&q=" +
url2 = "http://api.openweathermap.org/data/2.5/air_pollution?lat=50&lon=50&appid=e7e7b64e92164cde582d416840ef15f6"
response2 = requests.get(url2).json()
print("---------------")
print(response2)





url3 = "http://api.openweathermap.org/geo/1.0/zip?zip=94087,US&appid=e7e7b64e92164cde582d416840ef15f6"
response3 = requests.get(url3).json()
print("--------------")
print(response3)

response4 = str(response3).split("'")
print(response4[12])
response4 = response4[12].split()
print(response4[1])
response4 = response4[1].split(",")
print(response4[0])