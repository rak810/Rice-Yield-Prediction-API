import ignore
import os
import joblib
import urllib.request as urllib
import numpy as np
import ndvi



link = os.environ['predict_link']

fp = urllib.urlopen(link)
rf_pred_model = joblib.load(fp)

def get_num_type(type):
  if type == 'Aus':
    return 1
  elif type == 'Aman':
    return 2
  elif type == 'Boro':
    return 3
  
  return -1

def process_weather_data(type, land, weather_data, ndvi_val):
  arr = []
  num_type = get_num_type(type)

  if num_type == -1:
    return -1

  arr.append(num_type)

  for i in weather_data:
    arr.append(i)
  arr.append(ndvi_val)
  arr.append(land)
  return np.array([arr])

def get_prod(type, land, weather_data):
  ndvi_val = ndvi.get_ndvi_data(weather_data)
  data = process_weather_data(type, land, weather_data, ndvi_val)
  y_pred = rf_pred_model.predict(data)
  return ndvi_val, y_pred[0]
  

# y_pred = rf_model.predict(np.array([[1, 159.083333, 82.583333, 3.541667, 6.133333, 27.662500, 0.463067, 34995.0]]))
#mtype rain rel_hum cloud avg_sun temp ndvi hectare
# print(y_pred)