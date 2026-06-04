# Movie Night Picker

A Flask web app that helps you pick a movie to watch. Filter by genre and minimum rating.

Powered by the [TMDB API](https://www.themoviedb.org/).

## Setup

1. Clone the repo

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Install dependencies:
   ```
   python -m pip install flask requests
   ```

4. Get a free TMDB API key at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)


5. Run the app:
   ```
   python app.py
   ```
6. Open your browser to `http://127.0.0.1:5000`

## Features

- Filter movies by genre
- Set a minimum rating threshold
- Browse paginated results
- Random Pick button for when you still can't decide
```