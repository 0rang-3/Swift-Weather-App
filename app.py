from flask import Flask, redirect, url_for, render_template, request, session, flash
import datetime as dt
import requests

app = Flask(__name__)

#variables

CityVar = "London"

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()
CITY = CityVar

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

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route("/weather.html")
def weather():
    return render_template("weather.html", temp = temp_fahrenheit_rounded, feelslike = feels_like_fahrenheit, wind = wind_speed, hum = humidity,  desc = description)





if __name__ == '__main__':
    app.run(debug=True)
