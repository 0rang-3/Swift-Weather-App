import requests
import datetime as dt

#Establishes connection with txt file to pass parameters to app.py
f = open("templates/passParameters.txt", "r")
cityInfoList = f.read()
cityInfo = str(cityInfoList).split("/")
CITY = cityInfo[0]
lat = cityInfo[1]
lon = cityInfo[2]

#Sets up the API URL
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key.txt', 'r').read()

def kelvin_to_celsius_fahrenheit(kelvin): #Convert from Kelvin to Fahrenheit/Celsius
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
#Getting the data from the api
temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

wind_speed = response['wind']

#Get Wind Speed from wind_speed
speed = str(wind_speed).split("'")
speed = speed[2].split()
speed = speed[1].split(",")
speed = speed[0]

#Get Win Directino from wind_speed
direction = str(wind_speed).split("'")
direction = direction[4].split()
direction = direction[1].split("}")
direction = direction[0]

#Rounds Temperatures
temp_fahrenheit_rounded = round(int(temp_fahrenheit))
temp_celsius_rounded = round(int(temp_celsius))
feels_like_fahrenheit_rounded = round(int(feels_like_fahrenheit))
feels_like_celsius_rounded = round(int(feels_like_celsius))


#If and elif statements for recommendations based on temperature
if(feels_like_fahrenheit_rounded > 45 and feels_like_fahrenheit_rounded < 64 ):
    recommendation = "We recommend that you wear a light jacket when going out in this weather. "
elif(feels_like_fahrenheit_rounded > 25 and feels_like_fahrenheit_rounded < 44 ):
    recommendation = "We recommend that you wear a heavy jacket when going out in this weather."
elif(feels_like_fahrenheit_rounded < 25):
    recommendation = "We recommend wearing a winter jacket when going out in this weather."
elif(feels_like_fahrenheit_rounded > 64):
    recommendation = "A jacket is not recommended when going out in this weather. "

#Air Quality Index API
BASE2_URL = "http://api.openweathermap.org/data/2.5/air_pollution?"
url2 = BASE2_URL + "lat=" + lat + "&lon=" + lon + "&appid=" + API_KEY
response2 = requests.get(url2).json()

aqi = str(response2).split("'")
aqi = aqi[12].split()
aqi = aqi[1].split("}")
aqi = int(aqi[0])

#If and elif statements for recommendations based on air quality
if(aqi >= 0 and aqi <= 50):
    aqi_recommendation = "Air quality is satisfactory, and air pollution poses little or no risk."
elif(aqi >= 51 and aqi <= 100):
    aqi_recommendation = "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
elif(aqi >= 101 and aqi <= 150):
    aqi_recommendation = "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
elif(aqi >= 151 and aqi <= 200):
    aqi_recommendation = "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
elif(aqi >= 201 or aqi <= 300):
    aqi_recommendation = "Health alert: The risk of health effects is increased for everyone."
elif(aqi >= 301):
    aqi_recommendation = "Health warning of emergency conditions: everyone is more likely to be affected."

#Writes the data to the txt file for app.py to acess
f = open("templates/passParameters.txt", "w+")
f.write(str(temp_fahrenheit_rounded)+"/"+str(feels_like_fahrenheit_rounded)+"/"+str(speed)+"/"+str(direction)+"/"+str(humidity)+"/"+description+"/"+recommendation+"/"+str(aqi)+"/"+aqi_recommendation+"/")
f.close()
