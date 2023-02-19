from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home(): #Home Page
    return render_template("index.html")

@app.route('/choose_city.html')
def choose_city(): #Choose City Page
    return render_template("choose_city.html")

@app.route("/update", methods=["POST"])
def update_string(): #HTML Form to Choose City
    global CITY
    CITY = request.form["user_input"]
    cityList = CITY.split(',')

    #Geocoding API
    url2 = "http://api.openweathermap.org/geo/1.0/zip?zip=" + cityList[0] + "," + cityList[1] + "&appid=" + open('api_key.txt', 'r').read()
    response2 = requests.get(url2).json()

    #Get City Name
    cityList = str(response2).split("'")
    CITY = cityList[7]

    #Get Latitude
    lat = str(response2).split("'")
    lat = lat[10].split(":")
    lat = lat[1].split(",")
    lat = lat[0].split()
    lat = lat[0]

    #Get Longitude
    lon = str(response2).split("'")
    lon = lon[12].split()
    lon = lon[1].split(",")
    lon = lon[0]

    #Transfer Information to weather.py
    f = open("templates/passParameters.txt", "w")
    f.write(CITY+"/"+lat+"/"+lon)
    f.close()
    import weather #Start weather.py

    #Get Information from weather.py
    f = open("templates/passParameters.txt", "r")
    weatherList = f.read().split('/')
    temp_fahrenheit_rounded = weatherList[0]
    feels_like_fahrenheit_rounded = weatherList[1]
    speed = weatherList[2]
    speed_mph = round(float(speed)*2.23694) #Convert from m/s to mph
    direction = weatherList[3]
    humidity = weatherList[4]
    description = weatherList[5]
    recommendation = weatherList[6]
    aqi = weatherList[7]
    aqi_recommendation = weatherList[8]

    #Render weather.html
    return render_template("weather.html", temp = temp_fahrenheit_rounded, feelslike = feels_like_fahrenheit_rounded, speed = speed_mph, dir = direction, hum = humidity,  desc = description, rec = recommendation, aqi = aqi, aqi_rec = aqi_recommendation, city = CITY)

if __name__ == '__main__':
    app.run(debug=True)
