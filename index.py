import googlemaps
import datetime as dt
import requests
import math
import json
from flask import Blueprint, render_template, request


API_KEY = "AIzaSyBFmKmoW-sa6HfOXD6GPQWwl9H-sv_q3oY"

gmaps = googlemaps.Client(key=API_KEY)

address = '1600 Amphitheatre Parkway, Mountain View, CA'
geocode_result = gmaps.geocode(address)

if geocode_result:
    lat = geocode_result[0]['geometry']['location']['lat']
    lng = geocode_result[0]['geometry']['location']['lng']
    print('Latitude:', lat)
    print('Longitude:', lng)
else:
    print('Geocoding failed')

