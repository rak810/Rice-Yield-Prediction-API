import os
import pandas as pd
import urllib.request as urllib


def get_df(link):
  fp = urllib.urlopen(link)
  return pd.read_csv(fp)


link = os.environ['weather_link']

  
wd = get_df(link)

def process_weather_data(weather_data):
  arr = []
  for k, v in weather_data.items():
    arr.append(v)
  return arr

def get_weather_data(st_name, yr):
  result = "Not found"
  for i in range(len(wd)):
    if wd.iloc[i, 0] == st_name and wd.iloc[i, 1] == yr: 
      result = wd.iloc[i].to_dict()
      return process_weather_data(result)
  
  return result

def get_weather_json():
  return wd.to_json()
