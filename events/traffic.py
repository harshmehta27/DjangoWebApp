# MapQuest Traffic API
import requests
import json
from .keys import traffic_key

# This function takes in the latitude and longitude of the location and gives information about the traffic incidents
# in nearby regions
def get_traffic(latitude, longitude):
    # This API takes in two values of latitude and longitude and gives the traffic information within that area
    # So, I have defined two variables each for latitude and longitude from the given lat and long
    lo1, lo2 = longitude - 0.5, longitude + 0.5
    la1, la2 = latitude - 0.5, latitude + 0.5

    link = "http://www.mapquestapi.com/traffic/v2/incidents?key={}&boundingBox={},{},{},{}&filters=construction,incidents".format(traffic_key, la1, lo1, la2, lo2)

    data = requests.get(link)

    return json.loads(data.content)['incidents']

