# Meta-Tag-Movies

A modern web application that scans your movies directory, fetches metadata from OMDB API, and displays the information in a searchable, sortable table.

## Features

- **Automatic Movie Detection**: Scans movie directories and extracts titles and release years
- **OMDB API Integration**: Fetches detailed movie information including ratings, directors, genres
- **Responsive UI**: Modern Bootstrap 5 interface with mobile-friendly design
- **Advanced Data Table**: Sort, filter, and search your movie collection
- **Configurable Settings**: Set custom movie directory paths using environment variables

## Requirements

- Python 3.7+
- Flask
- Internet connection (for API requests)
- OMDB API Key (get one at https://www.omdbapi.com/apikey.aspx)

## Setup

1. Clone this repository
2. Create a `.env` file in the root directory with the following variables:
   ```
   OMDB_API_KEY=your_api_key_here
   MOVIES_PATH=/path/to/your/movies
   FLASK_DEBUG=False
   ```
3. Install dependencies:
   ```
   pip install flask requests python-dotenv
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open your browser and navigate to `http://localhost:5000`

## Movie Directory Format

For the application to correctly parse your movies, directories should be named in this format:

```
Movie Title (Year)
```

Example: `The Matrix (1999)`

## Troubleshooting

- If no movies appear, check that your MOVIES_PATH is correct
- Verify that your OMDB API key is valid
- Check console output for any error messages

## Version History

- 2.0.0 (2025) - Upgraded to Bootstrap 5, jQuery 3, and modern Flask patterns
- 1.0.0 - Initial release

## License

Open source software
