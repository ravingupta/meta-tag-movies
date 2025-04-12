import requests
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OMDB_BASE_URL = 'https://www.omdbapi.com/'
API_KEY = os.getenv('OMDB_API_KEY', '')
DEFAULT_MOVIES_PATH = os.getenv('MOVIES_PATH', os.path.expanduser('~/Movies'))

def search_movies(title, year, content_type='json'):
  """
  Search for a movie using the OMDB API
  """
  query = f'?t={title}&y={year}&plot=short&r={content_type}&apikey={API_KEY}'
  try:
    url = OMDB_BASE_URL + query
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
      return response.text  # Return as text, will be parsed by caller
    else:
      print(f"Error fetching from OMDB: {response.status_code}")
      return json.dumps({'Error': f'API error: {response.status_code}'})
  except Exception as e:
    print(f"Exception in search_movies: {str(e)}")
    return json.dumps({'Error': str(e)})

def list_directories(path=None):
  """
  List all directories in the specified path
  Falls back to default path if none provided
  """
  search_path = path or DEFAULT_MOVIES_PATH
  
  if not os.path.exists(search_path):
    print(f"Path does not exist: {search_path}")
    return []
    
  try:
    return [name for name in os.listdir(search_path) if os.path.isdir(os.path.join(search_path, name))]
  except Exception as e:
    print(f"Error listing directories: {str(e)}")
    return []
