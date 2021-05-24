import ignore
import os
import joblib
import urllib.request as urllib
import numpy as np

link = os.environ['ndvi_link']

fp = urllib.urlopen(link)
rf_ndvi_model = joblib.load(fp)

def get_ndvi_data(weather_data):
  wd = np.array([weather_data])
  y_pred = rf_ndvi_model.predict(wd)
  return y_pred[0]

