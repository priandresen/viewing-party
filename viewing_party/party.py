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
    
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]

    return avg_rating / len(user_data["watched"]






"""Create a function named `get_most_watched_genre`. This function should...

- take one parameter: `user_data`
  - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
    - This represents that the user has a list of watched movies. Each watched movie has a genre.
    - The values of `"genre"` is a string.
- Determine which genre is most frequently occurring in the watched list
- return the genre that is the most frequently watched
- If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.
"""

def get_most_watched_genre(user_data):

    most_watched_genre = None
    

    for movie in user_data["watched"]:




    return most_watched_genre

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

