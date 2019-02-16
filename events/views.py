# Importing libraries and modules from other python files
from django.shortcuts import render
from .geocoder import latLong
from .weather import city_weather
from .mongodb import upload_data, download_data
from .plots import plot_data
from .traffic import get_traffic
from .dataframe import make_table
from .background import back, background
from .keys import map_key

# This is the main function which is executed upon a request from the web page
def get_name(request):

    # A POST request indicates that the used entered a location and requests for weather data
    if request.method == 'POST':
        location = request.POST['location']    # The location entered by user is saved in location variable
        loc, lat, long, flag = latLong(location)  # The latLong function returns the city, latitude, longitude, flag
        data = city_weather(lat, long)    # It calls the weather API and returns weather data in JSON format
        data['location'] = loc    # The city name is inserted into the JSON data
        upload_data(data)     # This function uploads the JSON file to MongoDB
        traffic = get_traffic(lat, long)    # This function returns the Traffic Data in JSON format
        bg = back(data)      # This function returns an url which is used for the background image in HTML
        url = "<div></div>"    # Initiating url, df and top variables
        df = "<div></div>"
        top = "0px"

    # A GET request is sent when the user wants to check the Daily/Hourly forecast
    elif request.GET.get('plot_button'):
        data = download_data()    # This function is used to download the latest entry from MongoDB
        lat, long = data['latitude'], data['longitude']     # The latitude and longitude values are set using above data
        traffic = get_traffic(lat, long)    # This function returns the Traffic Data in JSON format
        flag = 0     # flag = 0 is used to display the weather information in HTML
        url = plot_data(request, data)    # This function returns a 'div' which is used for plotting graph in HTML
        df, top = make_table(request, data)    # This function converts a dataframe into a 'div' format to
                                               # display a table in html
        bg = back(data)     # This function returns an url which is used for the background image in HTML

    # On loading the local host for the first time, the HTML will be rendered using the following context
    else:
        location = 'Raleigh'    # Default location is set to Raleigh
        loc, lat, long, f = latLong(location)
        # The default value is set for the following variables
        flag = 2
        url = "<div></div>"
        data = dict()
        traffic = list()
        df = "<div></div>"
        top = '0px'
        bg = background['default']

    context = {'lat': lat, 'long': long, 'flag': flag, 'temp': data, 'traffic': traffic, 'url': url, 'df': df, 'bg': bg,
               'top': top, 'map_key': map_key}

    return render(request, 'maps.html', context=context)
