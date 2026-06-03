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
   python -m pip install flask requests python-dotenv
   ```

4. Get a free TMDB API key at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

5. Create a `.env` file in the project root with:
   ```
   TMDB_API_KEY=your_key_here
   TMDB_READ_ACCESS_TOKEN=your_token_here
   FLASK_SECRET_KEY=any_random_string
   ```

6. Run the app:
   ```
   python app.py
   ```
7. Open your browser to `http://127.0.0.1:5000`

## Features

- Filter movies by genre
- Set a minimum rating threshold
- Browse paginated results
- Random Pick button for when you still can't decide
```