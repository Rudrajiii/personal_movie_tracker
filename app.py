import database
import datetime
menu = """
1) Add a new movie.
2) view upcoming movies.
3) view all movies.
4) watch a movie.
5) view watched movies.
6) Search for a movie.
7) Exit.
Your Selection:"""
welcome = "welcome to the watchlist app!"

print(welcome)
database.create_tables()

def prompt_add_movie():
    title = input("Movie Title: ")
    release_date = input("Release Date (DD-MM-YYYY): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movie(title,timestamp)
def print_movie_list(heading , movies):
    print(f"-- {heading} movies --")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{movie[0]} (on {human_date})")
    print("----- \n")

def prompt_watch_movie():
    watcher_name = input("Username: ")
    movie_title = input("Enter Movie Title You Have Watched: ")
    added_movies = database.added_movies()
    print(added_movies)
    if movie_title in added_movies:
        database.watch_movie(watcher_name,movie_title)
    else:
        release_date = input("Release Date (DD-MM-YYYY): ")
        parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
        timestamp = parsed_date.timestamp()
        database.add_movie(movie_title, timestamp)
        database.watch_movie(watcher_name,movie_title)
        
def print_movie_list_movie(watcher_name , movies):
    print(f"{watcher_name} watche's the movies: ")
    for movie in movies:
        print(f"{movie[1]}")
    print("----\n")

def prompt_search_movies():
    search_item = input("Search a movie: ")
    movies = database.search_movies(search_item)
    if movies:
        print("--- Movies Found ---")
        for movie in movies:
            print(movie[0])
    else:
        print("--- No movies found ---")

while (user_input := input(menu)) != "7":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movie(True)
        print_movie_list("Upcoming",movies)
    elif user_input == "3":
        movies = database.get_movie()
        print_movie_list("All",movies)
    elif user_input == "4":
        prompt_watch_movie()
    elif user_input == "5":
        watcher_name = input("Username: ")
        all_user = database.user_hashMap()
        if watcher_name in all_user:
            movies = database.get_watched_movies(watcher_name)
            print_movie_list_movie(watcher_name, movies)
        else:
            print("User Not Found: " + watcher_name)
    elif user_input == "6":
        prompt_search_movies() 
    else:
        print("Invalid input , Please try again!")

# save = database.added_movies()
# print(save)