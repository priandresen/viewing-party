# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):


    avg_rating = 0.0

    if len(user_data["watched"]) == 0:
        return avg_rating
    
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]

    return avg_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):

    most_watched_genre = None

    if len(user_data["watched"]) == 0:
        return most_watched_genre 
    
    genre_frequency = {}

    for movie in user_data["watched"]:
        genre_frequency[movie["genre"]] = genre_frequency.get(movie["genre"], 1) + 1

    most_watched_genre_frequency = 0

    for genre, frequency in genre_frequency.items():
        if frequency > most_watched_genre_frequency:
            most_watched_genre_frequency = frequency
            most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_movies = []
    friends_set = set()
    user_set = set()
    
    for friend_movies in user_data["friends"]:
        for movie in friend_movies:
            friends_set.add(movie)

    for user_movie in user_data["watched"]:
        for movie in user_movie:
            user_set.add(movie)

    return user_set - friends_set

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

