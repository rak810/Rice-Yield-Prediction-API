import os

def get_link():
  my_secret = os.environ['validation_key']
  print(my_secret)

get_link()