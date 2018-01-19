import pyowm

# -*- coding: utf-8 -*-


def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def getWeatherData():
    owm = pyowm.OWM('d46d862d143dee6b00df063df2b61cb1')  # You MUST provide a valid API key

    # Search for current weather in London (Great Britain)
    observation = owm.weather_at_zip_code('07030','US')
    w = observation.get_weather()
    print(w)                      # <Weather - reference time=2013-12-18 09:20,

    # Weather details
    print(observation)
    w.get_wind()                  # {'speed': 4.6, 'deg': 330}
    w.get_humidity()              # 87
    print(w.get_temperature('fahrenheit'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

    # Search current weather observations in the surroundings of
    # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
    observation_list = owm.weather_around_coords(-22.57, -43.12)