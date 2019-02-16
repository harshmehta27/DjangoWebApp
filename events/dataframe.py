# Pandas is used to create a dataframe which is displayed in the HTML as a table
import pandas as pd
import time

# This function converts seconds from epoch to mm/dd format
def to_date(x):
    t = time.localtime(x)
    dy = str(t.tm_mday)
    mn = str(t.tm_mon)
    days = mn + '/' + dy
    return days

# This function converts from seconds from epoch to HH:MM (hour, minute) format
def to_time(x):
    t = time.localtime(x)
    hr = str(t.tm_hour)
    mn = str(t.tm_min)
    hours = hr + ':' + mn
    return hours

# This function converts the precipitation probability to a string indicating percentage from 0 to 100
def to_str(x):
    x = round(x*100)
    x = str(x)+'%'
    return x


# This function returns the 'div' for the table and the absolute top position of the table
def dataframe(data, idx):
    df = pd.DataFrame()    # An empty dataframe is initiated
    c1, c2, c3 = [], [], []    # The values of selected parameters are stored in lists
    for i,rows in enumerate(data):
        c1.append(rows['time'])
        c2.append(rows['precipProbability'])
        c3.append(rows['summary'])
        if i == 23:
            break
    df[idx] = c1    # These list values are stored in the dataframe.
    df['Precipitation'] = c2
    df['Summary'] = c3
    df['Precipitation'] = df['Precipitation'].apply(lambda x: to_str(x))
    if idx == 'Date':
        df[idx] = df[idx].apply(lambda x: to_date(x))
    else:
        df[idx] = df[idx].apply(lambda x: to_time(x))
    df.set_index(idx, inplace=True)
    return df.to_html()


# This is the function which returns the final dataframe into a div format
def make_table(request, data):
    if request.GET.get('plot_button') == 'Daily':
        json_data = data['daily']['data']
        df = dataframe(json_data, 'Date')
        top = '220px'
    else:
        json_data = data['hourly']['data']
        df = dataframe(json_data, 'Hours')
        top = '90px'

    return df, top

