#Parameters title , release_date , watched
import sqlite3
import datetime
CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL
);"""
CREATE_WATCHLIST_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT
);"""
INSERT_MOVIES = "INSERT INTO movies (title, release_timestamp) VALUES (? , ?);"
DELETE_MOVIE = "SELECT * FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_UPCOMING_MOVIES = "SELECT * FROM movies WHERE release_timestamp > ?;"
SELECT_WATCHED_MOVIES = "SELECT * FROM watched WHERE watcher_name = ?;"
INSERT_WATCHED_MOVIES = "INSERT INTO watched (watcher_name,title) VALUES (? ,?);"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"
UNIQUE_USERS = "SELECT watcher_name FROM watched;"
ALL_MOVIES_ADDED = "SELECT title FROM movies;"
SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE ?;"

connection = sqlite3.connect("database.db")

def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_WATCHLIST_TABLE)

def add_movie(title , release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES , (title, release_timestamp))

def get_movie(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if(upcoming):
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES , (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()

def watch_movie(watcher_name,title):
    with connection:
        cursor = connection.execute(DELETE_MOVIE , (title,))
        movie_details = cursor.fetchone()
        connection.execute(INSERT_WATCHED_MOVIES, (watcher_name, title))
        return movie_details
def get_watched_movies(watcher_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES ,(watcher_name,))
        return cursor.fetchall()

def search_movies(search_item):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SEARCH_MOVIES , (f"%{search_item}%",))
        return cursor.fetchall()
def user_hashMap():
    user_set = {}
    with connection:
        cursor = connection.execute(UNIQUE_USERS)
        for row in cursor:
            watcher_name = row[0]
            user_set[watcher_name] = "Unique User"
    return user_set

def added_movies():
    all_added_movies = {}
    with connection:
        cursor = connection.execute(ALL_MOVIES_ADDED)
        for movie in cursor:
            movie = movie[0]
            all_added_movies[movie] = "Uniquely Added"
    return all_added_movies
