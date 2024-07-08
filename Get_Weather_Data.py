import requests as req
import json
import pandas as pd
import csv

# open-meteo.com
url = "https://archive-api.open-meteo.com/v1/archive?latitude=41.6005&longitude=-93.6091&start_date=2000-01-01&end_date=" \
      "2024-07-06&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean&timezone=" \
      "America%2FChicago&temperature_unit=fahrenheit&windspeed_unit=mph&precipitation_unit=inch"
response = req.get(url).json()

# Extracting data from response
dates = response['daily']['time']
max_temps = response['daily']['temperature_2m_max']
max_temp_units = response['daily_units']['temperature_2m_max']
min_temps = response['daily']['temperature_2m_min']
min_temp_units = response['daily_units']['temperature_2m_min']
avg_temps = response['daily']['temperature_2m_mean']
avg_temp_units = response['daily_units']['temperature_2m_mean']

# Creating a DataFrame from the extracted data
data = {
    "DATE": dates,
    "MAX_TEMP": max_temps,
    "MAX_TEMP_UNITS": [max_temp_units] * len(dates),
    "MIN_TEMP": min_temps,
    "MIN_TEMP_UNITS": [min_temp_units] * len(dates),
    "AVG_TEMP": avg_temps,
    "AVG_TEMP_UNITS": [avg_temp_units] * len(dates)
}

df = pd.DataFrame(data)
print(df)