# This function uses the Geocoder API to get longitude and latitude of the requested location
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='My App')

def latLong(location):
    loc = geolocator.geocode(location)
    # If the user enters an invalid location then the flag is set as 1 which will throw an error
    if loc == None:
        loc = geolocator.geocode('Raleigh')
        lat, long = loc.latitude, loc.longitude
        flag = 1
        address = None
    else:
        lat, long = loc.latitude, loc.longitude
        address = loc.address.split(sep=',')[0]
        flag = 0
    return address, lat, long, flag
