import requests

url = 'http://127.0.0.1:1080/predict/yield'  # localhost and the defined port + endpoint
body = {
    "st": "Barisal",
    "yr": 2022,
    "type": "Aman",
    "land" : 34995.0
}


response = requests.post(url, data=body)
if response.status_code == 200:
  print(response.json())
else:
  print("response status code : ", response.status_code)
  print(response.reason)

    # "type": "Aman",
    # "land" : 34995.0