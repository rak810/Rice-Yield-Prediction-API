import requests

# https://rice-yield-prediction-api.herokuapp.com/predict/weather
# http://127.0.0.1:1080/
url = 'https://rice-yield-prediction-api.herokuapp.com/ndvi'  # localhost and the defined port + endpoint
body = {
    "st": "Maulvibazar"
}


response = requests.post(url, data=body)
if response.status_code == 200:
  print(len(response.json()))
  print(response.json())
else:
  print("response status code : ", response.status_code)
  print(response.reason)

    # "type": "Aman",
    # "land" : 34995.0