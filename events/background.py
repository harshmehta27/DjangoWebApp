
# The following dictionary has the url's (for background) for each of the rain, snow, cloudy, etc weather conditions
# Any of this url is used to set the background animation in HTML
background = {
    'rain': "https://media0.giphy.com/media/5PjafLZFxMWc/giphy.gif?cid=3640f6095c10bb2949707334413fc5e1",
    'snow': "https://media3.giphy.com/media/14uJKhQMZ1wLfO/200w.webp?cid=3640f6095c1139c6665a374a67242a3c",
    'cloudy': "https://media3.giphy.com/media/Cn46Wi1Fvh11S/giphy.gif?cid=3640f6095c113a01417756472efeff4b",
    'default': "https://media1.giphy.com/media/u01ioCe6G8URG/giphy.gif?cid=3640f6095c113a23427335753267ff3c",
    'clear-night': "https://media2.giphy.com/media/FlodpfQUBSp20/giphy.gif?cid=3640f6095c113a4f31664a6667905c5e",
    'partly-cloudy-night': "https://media2.giphy.com/media/FlodpfQUBSp20/giphy.gif?cid=3640f6095c113a4f31664a6667905c5e"
}

# This function checks the weather condition form the data and then selects the most suitable url from above dictionary
def back(data):
    weather = data['currently']['icon']  # This gives the weather condition like snow, rain, cloudy, etc.
    if weather in background.keys():
        return background[weather]
    else:
        return background['default']