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

    friends_set = set()
    user_set = set()
    
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_set.add(friend_movie["title"])

    for user_movie in user_data["watched"]:
        user_set.add(user_movie["title"])

    unique_title = user_set - friends_set

    unique_movies = []

    for movie in user_data["watched"]:
        if movie["title"] in unique_title:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):

    friends_set = set()
    user_set = set()
    
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_set.add(friend_movie["title"])
    

    for user_movie in user_data["watched"]:
        user_set.add(user_movie["title"])
    print(user_set)

    unique_title = friends_set - user_set
    print(unique_title)

    unique_movies = []

    for movie in user_data["friends"]:
        for friend_movie in movie["watched"]:
            ## here we are checking the movie that the friend has watched
            if friend_movie["title"] in unique_title and (friend_movie 
                                                          not in unique_movies):
                #checking for duplicates
                unique_movies.append(friend_movie)
    
    return unique_movies




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    """- take one parameter: `user_data`
  - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"`
    is a list of strings
    - This represents the names of streaming services that the user has access to
    - Each friend in `"friends"` has a watched list. Each movie in the watched 
    list has a `"host"`, which is a string that says what streaming service it's 
    hosted on
- Determine a list of recommended movies. A movie should be added to this list if 
and only if:
  - The user has not watched it
  - At least one of the user's friends has watched
  - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
- Return the list of recommended movies"""

    pass




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre():

    """- take one parameter: `user_data`
- Consider the user's most frequently watched genre. Then, determine a list of 
recommended movies. A movie should be added to this list if and only if:
  - The user has not watched it
  - At least one of the user's friends has watched
  - The `"genre"` of the movie is the same as the user's most frequent genre
- Return the list of recommended movies
"""
    pass


def get_rec_from_favorites():

    """
    - take one parameter: `user_data`
  - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a 
  list of movie dictionaries
    - This represents the user's favorite movies
- Determine a list of recommended movies. A movie should be added to this list
if and only if:
  - The movie is in the user's `"favorites"`
  - None of the user's friends have watched it
- Return the list of recommended movies
    """
    pass

