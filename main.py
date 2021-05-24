from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import data
import predict

APP = Flask(__name__)
API = Api(APP)

def gen_json(weather_data, ndvi_val, prod, tp, land):
  fin_dict = {}

  fin_dict['dist'] = weather_data[0]
  fin_dict['year'] = int(weather_data[1])
  fin_dict['geo'] = {'lat' : float(weather_data[2]),
                     'long' : float(weather_data[3])
                    }
  fin_dict['weather'] = {'rain' : float(weather_data[4]),
                         'rel_hum' : float(weather_data[5]),
                         'cloud' : float(weather_data[6]),
                         'avg_sun': float(weather_data[7]),
                         'temp' : float(weather_data[8])
                        }
  fin_dict['land'] = land
  fin_dict['type'] = tp
  fin_dict['ndvi'] = float(ndvi_val)
  fin_dict['prod'] = float(prod)
  
  return json.dumps(fin_dict)

class GetWeather(Resource):

  @staticmethod
  def post():
    parser = reqparse.RequestParser()
    parser.add_argument('st')
    parser.add_argument('yr')

    args = parser.parse_args()  # creates dict
    arr = data.get_weather_data(args['st'], int(args['yr']))
    print(arr)
    out = {"success" : "nigger"}
    
    return out, 200

class GetYield(Resource):
  @staticmethod
  def post():
    parser = reqparse.RequestParser()
    parser.add_argument('st')
    parser.add_argument('yr')
    parser.add_argument('type')
    parser.add_argument('land')

    args = parser.parse_args()  # creates dict
    weather_data = data.get_weather_data(args['st'], int(args['yr']))
    ndvi_val, prod = predict.get_prod(args['type'], args['land'], weather_data[4:])
    out = gen_json(weather_data, ndvi_val, prod, args['type'], args['land'])
    return out, 200

API.add_resource(GetWeather, '/predict/weather')
API.add_resource(GetYield, '/predict/yield')

if __name__ == '__main__':
    APP.run(debug=True, port='1080')