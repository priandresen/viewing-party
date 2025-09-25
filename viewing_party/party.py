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
            # here we are checking the movie that the friend has watched
            if friend_movie["title"] in unique_title and (friend_movie not in unique_movies):
                #checking for duplicates
                unique_movies.append(friend_movie)
    
    return unique_movies




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # Create a set with the services the user is subscribed to
    subscriptions = set()
    for service in user_data["subscriptions"]:
        subscriptions.add(service)

    # Create a set with the EXACT movies the user has already watched
    user_watched_exact = set()
    for movie in user_data["watched"]:
        # Here we take the four values directly with []
        title = movie["title"]
        genre = movie["genre"]
        rating = movie["rating"]
        host = movie["host"]

        user_watched_exact.add((title, genre, rating, host))

    # Final list of recommendations and set to avoid duplicates
    recommendations = []
    seen_movies = set()

    # 4. Check the movies that the friends have watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            genre = movie["genre"]
            rating = movie["rating"]
            host = movie["host"]

            movie_key = (title, genre, rating, host)

            # Add only if:
            # - the user has NOT watched it
            # - the host is in the user's subscriptions
            # - it has NOT been added before
            if movie_key not in user_watched_exact and host in subscriptions and movie_key not in seen_movies:
                recommendations.append(movie)
                seen_movies.add(movie_key)

    return recommendations



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
    # Get the list of movies the user has watched
    watched = user_data["watched"]
    if len(watched) == 0:
        return []

    # Count how many times each genre appears
    genre_count = {}
    for movie in watched:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

    # Find the most watched genre
    top_genre = None
    top_count = 0
    for genre in genre_count:
        if genre_count[genre] > top_count:
            top_genre = genre
            top_count = genre_count[genre]

    # Get all titles the user has already watched
    user_titles = set()
    for movie in watched:
        user_titles.add(movie["title"])

    # Find friends' movies that match the top genre
    recs = []
    seen_titles = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if (
                movie["genre"] == top_genre and
                title not in user_titles and
                title not in seen_titles
            ):
                recs.append(movie)
                seen_titles.add(title)

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
    # Get user's favorite movies and friends list
    favorites = user_data["favorites"]
    friends = user_data["friends"]

    # Collect all movie titles that friends have watched
    friends_titles = set()
    for friend in friends:
        for movie in friend["watched"]:
            friends_titles.add(movie["title"])

    # Recommend favorite movies that none of the friends have watched
    recs = []
    for movie in favorites:
        if movie["title"] not in friends_titles:
            recs.append(movie)

    return recs

