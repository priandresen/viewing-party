# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # If any of the required fields is missing or falsy, return None
    if not title or not genre or not rating:
        return None
    # Return a movie dictionary with the expected keys
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    # Assumes user_data already has a "watched" key that is a list
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # Assumes user_data already has a "watchlist" key that is a list
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # Look through the watchlist for a movie with the matching title
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    # Initialize the running total of ratings as a float
    avg_rating = 0.0

    if len(user_data["watched"]) == 0:
        return avg_rating
    # Accumulate the rating of each watched movie
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]
    # Total of ratings divided by the number of watched movies
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
            if friend_movie["title"] in unique_title and (friend_movie not in unique_movies):
                #checking for duplicates
                unique_movies.append(friend_movie)
    
    return unique_movies




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    watched = user_data.get("watched", [])
    friends = user_data.get("friends", [])
    subscriptions = user_data.get("subscriptions", [])

    # set of EXACT movies the user has already watched (title, genre, rating, host)
    user_watched_exact = set()
    i = 0
    while i < len(watched):
        m = watched[i]
        user_watched_exact.add((
            m.get("title"),
            m.get("genre"),
            m.get("rating"),
            m.get("host"),
        ))
        i += 1

    # set of available services
    subs_set = set()
    j = 0
    while j < len(subscriptions):
        subs_set.add(subscriptions[j])
        j += 1

    # recommendations without duplicates
    recs = []
    seen_exact = set()  # avoid repeating the SAME movie from a friend

    f = 0
    while f < len(friends):
        fw = friends[f].get("watched", [])
        k = 0
        while k < len(fw):
            movie = fw[k]
            movie_key = (
                movie.get("title"),
                movie.get("genre"),
                movie.get("rating"),
                movie.get("host"),
            )
            host = movie.get("host")

            if (movie_key not in user_watched_exact) and (host in subs_set) and (movie_key not in seen_exact):
                recs.append(movie)
                seen_exact.add(movie_key)

            k += 1
        f += 1

    return recs


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




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

    """- take one parameter: `user_data`
- Consider the user's most frequently watched genre. Then, determine a list of 
recommended movies. A movie should be added to this list if and only if:
  - The user has not watched it
  - At least one of the user's friends has watched
  - The `"genre"` of the movie is the same as the user's most frequent genre
- Return the list of recommended movies
"""
def get_new_rec_by_genre(user_data):
    # 1) find the user's most watched genre
    watched = user_data.get("watched", [])
    if not watched:
        return []

    genre_freq = {}
    i = 0
    while i < len(watched):
        g = watched[i].get("genre")
        if g is not None:
            if g in genre_freq:
                genre_freq[g] += 1
            else:
                genre_freq[g] = 1
        i += 1

    if not genre_freq:
        return []

    # manually find the most frequent genre (without using max)
    top_genre = None
    top_count = -1
    for g in genre_freq:
        if genre_freq[g] > top_count:
            top_count = genre_freq[g]
            top_genre = g

    # 3) recommendations from friends with the favorite genre
    user_titles = set()
    i = 0
    while i < len(watched):
        user_titles.add(watched[i].get("title"))
        i += 1

    # 3) recomendações vindas dos amigos com o gênero favorito
    recs = []
    seen_titles = set()
    friends = user_data.get("friends", [])

    f = 0
    while f < len(friends):
        fw = friends[f].get("watched", [])
        j = 0
        while j < len(fw):
            movie = fw[j]
            title = movie.get("title")
            genre = movie.get("genre")
            if (
                genre == top_genre
                and title not in user_titles
                and title not in seen_titles
            ):
                recs.append(movie)
                seen_titles.add(title)
            j += 1
        f += 1

    return recs

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
def get_rec_from_favorites(user_data):
    favorites = user_data.get("favorites", [])
    friends = user_data.get("friends", [])

    # collect all titles that any friend has watched
    friends_titles = set()
    f = 0
    while f < len(friends):
        fw = friends[f].get("watched", [])
        j = 0
        while j < len(fw):
            friends_titles.add(fw[j].get("title"))
            j += 1
        f += 1

    # recommend only those from favorites that none of the friends have watched
    recs = []
    i = 0
    while i < len(favorites):
        movie = favorites[i]
        title = movie.get("title")
        if title not in friends_titles:
            recs.append(movie)
        i += 1

    return recs

