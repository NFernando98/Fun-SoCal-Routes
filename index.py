import googlemaps
import datetime as dt
import requests
import math
import json
from flask import Blueprint, render_template, request
import folium
from datetime import datetime
import html

views = Blueprint(__name__, "views")


data = {
    "api_key": "key: AIzaSyBFmKmoW-sa6HfOXD6GPQWwl9H-sv_q3oY"
}
with open('google_maps_credentials.json', 'w') as file:
    json.dump(data, file)

API_KEY = "AIzaSyBFmKmoW-sa6HfOXD6GPQWwl9H-sv_q3oY"

gmaps = googlemaps.Client(key=API_KEY)

Starting_address = 'Dana Point, California, USA'
geocode_result = gmaps.geocode(Starting_address)

Ending_address = 'Laguna Beach, California, USA'



# if geocode_result:
#     lat = geocode_result[0]['geometry']['location']['lat']
#     lng = geocode_result[0]['geometry']['location']['lng']
#     print('Latitude:', lat)
#     print('Longitude:', lng)
# else:
#     print('Geocoding failed')
    
# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="driving",
                                     departure_time=now)


@views.route('/directions')
def directions():
    # Get the origin and destination addresses
    origin = 'Dana Point, California, USA'
    destination = 'Laguna Beach, California, USA'

    # Request directions from the Google Maps API
    directions_result = gmaps.directions(origin, destination)

    # Extract the steps from the response
    steps = directions_result[0]["legs"][0]["steps"]
    


    return render_template('directions.html', steps=steps)
    
    
    

@views.route('/directions2')
def display_route():
    address = 'Dana Point, California, USA'
    geocode_result = gmaps.geocode(address)
    start_lat = geocode_result[0]['geometry']['location']['lat']
    start_lng = geocode_result[0]['geometry']['location']['lng']
    
    address = 'Laguna Beach, California, USA'
    geocode_result = gmaps.geocode(address)
    end_lat = geocode_result[0]['geometry']['location']['lat']
    end_lng = geocode_result[0]['geometry']['location']['lng']
    
    return render_template('directions.html', start_lat=start_lat, start_lng=start_lng, end_lat=end_lat, end_lng=end_lng)
    
    


def getLatitude(address:str):
    return null    

