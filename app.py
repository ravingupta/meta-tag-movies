from flask import Flask, Request, render_template
import re
import json
import ast

from helpers import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_url():
  dir_names = list_directories('/home/ravin/Videos/')
  movie_details = []
  for names in dir_names:
    name = re.findall("(.*?) \(", names)
    year = re.findall("\((.*?)\)", names)
    movie_json = search_movies(name[0], year[0])
    movie_json = ast.literal_eval(movie_json)
    movie_details.append(movie_json)
  with open('content.txt', 'w') as outfile:
    json.dump(movie_details, outfile)
  return render_template('index.html')

@app.route('/table_data', methods=['GET'])
def table_data():
  content = {}
  with open('content.txt', 'r') as content_file:
    content = content_file.read()
  return content

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)