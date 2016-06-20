import requests
import os
import json

OMDB_BASE_URL = 'http://www.omdbapi.com/'

def search_movies(title, year, content_type='json'):
  query = '?t={0}&y={1}&plot={2}&r={3}'.format(title, year, 'short', content_type)
  try:
    url = OMDB_BASE_URL + query
    response = requests.get(url)
    if response.status_code == 200:
      return response.content
    else:
      return {'error': 'some error occur'}
  except:
    return {'error': 'some error occur'}

def list_directories(path):
  return [name for name in os.listdir(path) if os.path.isdir(path + name)]
