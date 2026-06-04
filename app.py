import os
import requests
from flask import Flask, render_template, request
import keys

app = Flask(__name__)
app.secret_key = "movie-night-picker-secret-2024"

TMDB_API_KEY = keys.TMDB_API_KEY
TMDB_READ_TOKEN = keys.TMDB_READ_TOKEN
TMDB_BASE = "https://api.themoviedb.org/3"
POSTER_BASE = "https://image.tmdb.org/t/p/w500"
PLACEHOLDER = "/static/img/no-poster.svg"


def _auth():
    if TMDB_READ_TOKEN:
        return {"headers": {"Authorization": f"Bearer {TMDB_READ_TOKEN}", "accept": "application/json"}, "params": {}}
    return {"headers": {}, "params": {"api_key": TMDB_API_KEY}}


def get_genres():
    url = f"{TMDB_BASE}/genre/movie/list"
    auth = _auth()
    params = {**auth["params"], "language": "en-US"}
    try:
        resp = requests.get(url, headers=auth["headers"], params=params, timeout=10)
        resp.raise_for_status()
        genres = resp.json().get("genres", [])
        return {g["id"]: g["name"] for g in genres}
    except requests.RequestException:
        return {}


def get_movies(genre_id=None, min_rating=0, page=1):
    url = f"{TMDB_BASE}/discover/movie"
    auth = _auth()
    params = {
        **auth["params"],
        "language": "en-US",
        "sort_by": "popularity.desc",
        "vote_count.gte": 100,
        "vote_average.gte": min_rating,
        "page": page,
    }
    if genre_id:
        params["with_genres"] = genre_id

    try:
        resp = requests.get(url, headers=auth["headers"], params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        print("API error:", e)
        return [], 0

    movies = []
    for m in data.get("results", []):
        poster_path = m.get("poster_path")
        movies.append({
            "id": m.get("id"),
            "title": m.get("title", "Unknown Title"),
            "year": (m.get("release_date") or "")[:4] or "N/A",
            "rating": round(m.get("vote_average", 0), 1),
            "overview": m.get("overview") or "No description available.",
            "poster": POSTER_BASE + poster_path if poster_path else None,
        })

    total_pages = min(data.get("total_pages", 1), 500)
    return movies, total_pages


@app.route("/")
def index():
    genres = get_genres()

    genre_id_str = request.args.get("genre", "")
    genre_id = int(genre_id_str) if genre_id_str.isdigit() else None
    min_rating = float(request.args.get("min_rating", 0))
    min_rating = max(0.0, min(10.0, min_rating))
    page = int(request.args.get("page", 1))
    page = max(1, page)

    movies, total_pages = get_movies(genre_id=genre_id, min_rating=min_rating, page=page)
    selected_genre_name = genres.get(genre_id, "All Genres") if genre_id else "All Genres"

    return render_template(
        "index.html",
        genres=genres,
        movies=movies,
        selected_genre_id=genre_id,
        selected_genre_name=selected_genre_name,
        min_rating=min_rating,
        page=page,
        total_pages=total_pages,
        placeholder=PLACEHOLDER,
        api_key_missing=not TMDB_API_KEY and not TMDB_READ_TOKEN,
    )


if __name__ == "__main__":
    app.run(debug=True)