#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 20:38:22 2020

@author: tylerpruitt
"""


import requests
import time
import datetime
import matplotlib.pyplot as plt

def iss():
    URL = 'https://api.wheretheiss.at/v1/satellites/25544'
    iss_data = requests.get(URL).json()

    url = 'http://api.open-notify.org/astros'
    crew_data = requests.get(url).json()

    iss_lat = iss_data['latitude']
    iss_long = iss_data['longitude']
    iss_alt = iss_data['altitude']
    iss_velocity = iss_data['velocity']
    iss_visib = iss_data['visibility']
    iss_foot = iss_data['footprint']
    iss_time = iss_data['timestamp']
    iss_day = iss_data['daynum']
    iss_solar_lat = iss_data['solar_lat']
    iss_solar_long = iss_data['solar_lon']
    iss_crew = crew_data['number']
    print('Spacecraft: ISS (catalog number: 25544)')
    print('Time:', iss_time, "s")
    print('Latitude:', iss_lat, 'deg')
    print('Longitude:', iss_long, 'deg')
    print('Altitude:', iss_alt, "km")
    print('Orbital Velocity:', iss_velocity / 3600, 'km/s')
    print('Visibility:', iss_visib)
    print('Day Number:', iss_day)
    print('Footprint:', iss_foot)
    print('Solar Latitude:', iss_solar_lat, 'deg')
    print('Solar Longitude:', iss_solar_long, 'deg')
    print('Crew Members:', iss_crew)
    print('')
    
    def translate_geo_to_pixels(iss_lat, iss_long, max_pixelX, max_pixelY):
        scale_x = (((iss_long + 180) / 360) * max_pixelX)
        scale_y = (((-iss_lat + 90) / 180) * max_pixelY)
        return scale_x, scale_y
    
    im = plt.imread('map.png')
    implot = plt.imshow(im)
    plt.scatter([translate_geo_to_pixels(iss_lat, iss_long, 876, 402)[0]], [translate_geo_to_pixels(iss_lat, iss_long, 876, 402)[1]], c='r', s=20)
    plt.show()
    
seconds = 0
minutes = 0
hours = 0
interval = 30

while True:
    print('----------------------------------------')
    local_time = time.ctime()
    print('Local Time: ', local_time)
    print('T: +' + str(datetime.time(hours, minutes, seconds)))
    print('----------------------------------------')
    print()
    iss()
    print('----------------------------------------')
    time.sleep(interval)
    seconds += interval
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1


