from flask import Flask , send_from_directory, render_template , request
import requests
from math import floor
from utils import *
import os
import json


DATA_DIR = "/app/data"
os.makedirs(DATA_DIR, exist_ok=True) 

app = Flask(__name__)
API_KEY = 'c44171366d41778194a8018ab5156f06' 

list_city = ['New York','Paris','Londres']

@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static/', path)

@app.route('/weather',methods=['GET'])
def weather():
    city = request.args.get('city')
    list_city.insert(0, city)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric'
    data = requests.get(url).json() 

    temperature = data["main"]["temp"]
    temperature_min = data["main"]["temp_min"]
    temperature_max = data["main"]["temp_max"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    wind = floor(wind * 2.23694)

    file_path = os.path.join(DATA_DIR, f"{city}.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    icon = data['weather'][0]['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon}.png'
    return render_template('/weather.html',temperature= temperature,temperature_max=temperature_max,temperature_min=temperature_min,humidity=humidity,wind=wind,city=city,icon_url=icon_url)


@app.route("/", methods=['GET'])
def index():

    list_of_city= rmdoublons(list_city)
    list_of_city = list_of_city[:3]
    cities_data = []
    for city in list_of_city:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric'

        data = requests.get(url).json()

        city_name = data["name"]
        temperature = data["main"]["temp"]
        icon = data['weather'][0]['icon']
        icon_url = f'https://openweathermap.org/img/wn/{icon}.png'

        city_data = {
            "name": city_name,
            "temperature": temperature,
            "icon_url": icon_url
        }
        cities_data.append(city_data)
    return render_template('/index.html', cities=cities_data)





