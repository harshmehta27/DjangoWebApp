# This is the file from where the plots in HTML are created
# It uses the Plotly library
import plotly.offline as py
import plotly.graph_objs as go
import time

# This function is executed when the GET request is for 'Hourly Forecast'
def hourly_data(data):
    weather = data['hourly']['data']
    hours = list()
    temperature = list()
    for count, values in enumerate(weather):
        t = time.localtime(values['time'])  # This function converts seconds from epoch to local time format
        hr = str(t.tm_hour)   # The 'hour' and 'minute' of the time are extracted to plot on the X axis
        mn = str(t.tm_min)
        hours.append(hr+':'+mn)
        temperature.append(values['temperature'])
        if count==23:   # The hourly forecast for next 24 hours is only required
            break
    return hours, temperature

# This function is executed when the GET request is for 'Daily Forecast'
def daily_data(data):
    weather = data['daily']['data']
    days = list()
    temp_low = list()
    temp_high = list()
    for values in weather:
        t = time.localtime(values['time'])
        dy = str(t.tm_mday)    # The 'date' and 'month' values are extracted to plot on the X axis
        mn = str(t.tm_mon)
        days.append(mn+'/'+dy)
        temp_low.append(values['temperatureLow'])
        temp_high.append(values['temperatureHigh'])
    return days, temp_low, temp_high

# This function returns a 'div' which is used to generate a plot in HTML
def plot_data(request, data):
    # If the request was for Daily forecast than the below condition will be executed
    if request.GET.get('plot_button')=="Daily":
        x, low, high = daily_data(data)    # The days, low and high temperature values are obtained using this function
        t_low = go.Scatter(x=x, y=low, name="Low")    # A graph object is created for low temperature values
        t_high = go.Scatter(x=x, y=high, name="High")    # A graph object is created for high temperature values
        # The layout for the plot is defined below
        layout = go.Layout(title='Daily Forecast', xaxis=dict(title='Date (MM/DD)'), yaxis=dict(title='Temperature (F)'))
        t = [t_low, t_high]
        data = dict(data=t, layout=layout)
        url = py.offline.plot(data, include_plotlyjs=False, output_type='div')    # This returns a 'div' for HTML

    # If the request was for Hourly forecast than the below condition will be executed
    else:
        x, y = hourly_data(data)    # The hour values and temperature values are returned using this function
        pl = go.Scatter(x=x,y=y)     # A graph object is created for the Plot
        layout = go.Layout(title='Hourly Forecast', xaxis=dict(title='Time'), yaxis=dict(title='Temperature (F)'))
        data = dict(data=[pl], layout=layout)
        url = py.offline.plot(data, include_plotlyjs=False, output_type='div')    # This returns a 'div' for HTML

    return url