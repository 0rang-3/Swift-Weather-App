from flask import Flask, redirect, url_for, render_template, request, session, flash, request
import datetime as dt
import requests

app = Flask(__name__)

temp_fahrenheit_rounded = 0
feels_like_fahrenheit_rounded = 0
wind_speed = 0
humidity = 0
description = "None"



@app.route('/')
def home():  # put application's code here
    return render_template("index.html")

@app.route('/choose_city.html')
def choose_city():
    return render_template("choose_city.html")

@app.route("/update", methods=["POST"])
def update_string():
    global CITY
    CITY = request.form["user_input"]
    cityList = CITY.split(',')
    url2 = "http://api.openweathermap.org/geo/1.0/zip?zip=" + cityList[0] + "," + cityList[1] + "&appid=" + open('api_key.txt', 'r').read()
    response2 = requests.get(url2).json()
    cityList = str(response2).split("'")
    CITY = cityList[7]
    lat = str(response2).split("'")
    lat = lat[10].split(":")
    lat = lat[1].split(",")
    lat = lat[0].split()
    lat = lat[0]
    print(lat)
    lon = str(response2).split("'")
    lon = lon[12].split()
    lon = lon[1].split(",")
    lon = lon[0]
    print(lon)

    f = open("templates/passParameters.txt", "w")
    f.write(CITY+"/"+lat+"/"+lon)
    f.close()
    import weather
    f = open("templates/passParameters.txt", "r")
    weatherList = f.read().split('/')
    temp_fahrenheit_rounded = weatherList[0]
    feels_like_fahrenheit_rounded = weatherList[1]
    wind_speed = weatherList[2]
    humidity = weatherList[3]
    description = weatherList[4]
    recommendation = weatherList[5]
    aqi = weatherList[6]
    aqi_recommendation = weatherList[7]
    return render_template("weather.html", temp = temp_fahrenheit_rounded, feelslike = feels_like_fahrenheit_rounded, wind = wind_speed, hum = humidity,  desc = description, rec = recommendation, aqi = aqi, aqi_rec = aqi_recommendation)


"""
@app.route("/weather.html")
def weather():
    print("hi 2")
    return render_template("weather.html", temp = temp_fahrenheit_rounded, feelslike = feels_like_fahrenheit_rounded, wind = wind_speed, hum = humidity,  desc = description)

"""





if __name__ == '__main__':
    app.run(debug=True)
