import json
import pandas as pd
import urllib.request as urllib
import os

def get_df(link):
  fp = urllib.urlopen(link)
  return pd.read_csv(fp)

def get_previous_data(dst, tp):
  link = os.environ['final_key']
  print(link)
  df = get_df(link)
  df = df[(df['st'] == dst) & (df['rtype'] == tp)]
  df = df[df['yr'] < 2017]
  df = df[['st', 'yr', 'rtype', 'hectares', 'prod']]
  return df.to_json(orient='index')

def get_validation_data(dst, tp):

  link = os.environ['validation_key']
  print(link)
  df = get_df(link)
  df = df[(df['st'] == dst) & (df['rtype'] == tp)]
  df = df[['st', 'yr', 'rtype', 'hectares', 'prod', 'pred']]
  return df.to_json(orient='index')


def get_data(dst, tp):
  prev_json = get_previous_data(dst, tp)
  val_json = get_validation_data(dst, tp)
  fn_dict = {}
  fn_dict['prev'] = prev_json
  fn_dict['val'] = val_json

  fn_json = json.dumps(fn_dict)
  return fn_json






