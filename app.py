from flask import Flask, request, render_template, jsonify
import re
import json
import os
from dotenv import load_dotenv

from helpers import list_directories, search_movies, DEFAULT_MOVIES_PATH

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root_url():
    try:
        movies_path = os.getenv('MOVIES_PATH', DEFAULT_MOVIES_PATH)
        dir_names = list_directories(movies_path)
        movie_details = []
        
        for movie_dir in dir_names:
            try:
                # Extract movie name and year from directory name
                name_match = re.findall(r"(.*?) \(", movie_dir)
                year_match = re.findall(r"\((.*?)\)", movie_dir)
                
                if name_match and year_match:
                    movie_title = name_match[0]
                    movie_year = year_match[0]
                    
                    # Search for movie details
                    movie_json_str = search_movies(movie_title, movie_year)
                    movie_data = json.loads(movie_json_str)
                    
                    # Only add movies with valid responses
                    if movie_data and 'Error' not in movie_data:
                        movie_details.append(movie_data)
                else:
                    print(f"Couldn't parse movie name/year from: {movie_dir}")
            except Exception as e:
                print(f"Error processing movie directory {movie_dir}: {str(e)}")
                continue
                
        # Save the results to file
        with open('content.txt', 'w') as outfile:
            json.dump(movie_details, outfile)
            
        return render_template('index.html')
    except Exception as e:
        print(f"Error in root_url: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/table_data', methods=['GET'])
def table_data():
    try:
        with open('content.txt', 'r') as content_file:
            content = content_file.read()
        return content
    except Exception as e:
        print(f"Error fetching table data: {str(e)}")
        return jsonify({"error": "Failed to load movie data"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 6000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)