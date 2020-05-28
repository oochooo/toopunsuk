import requests
import json
from django.conf import settings
from django.contrib.gis.geos import Point

from math import radians, cos, sin, asin, sqrt

def get_current_loc():

    url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=' + settings.GOOGLE_MAPS_API_KEY
    myobj = {'considerIp': 'true'}

    req = requests.post(url, data = myobj)
    data = json.loads(req.text)
    print(data)

    return {'lat': data['location']['lat'], 'lng': data['location']['lng'], 'accuracy': data['accuracy']}


def dictify_a_point(point):
    coord = [coord for coord in point]
    return {'lng': coord[0], 'lat': coord[1]}

def haversine_func_for_calculating_distance_between_two_points_on_our_very_precious_planet_earth(loc1, loc2):
    
    #takes 2 dicts with following keys 'lat' and 'lng'

    lon1 = radians(loc1['lng'])
    lon2 = radians(loc2['lng'])
    lat1 = radians(loc1['lat'])
    lat2 = radians(loc2['lat'])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

    c = 2 * asin(sqrt(a))

    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371

    # calculate the result
    return(c * r)


'''
pnt = Point(11.726265, 101.592056)
print(dictify_a_point(pnt))



print('testtettstst', haversine_func_for_calculating_distance_between_two_points_on_our_very_precious_planet_earth(get_current_loc(), dictify_a_point(pnt)))'''
