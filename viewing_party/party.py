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
    # Create two sets to store movie titles: all movies friends have watched and all movies the user has watched
    friends_set = set()
    user_set = set()

    # Loop through each friend and add their watched movie titles to friends_set
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_set.add(friend_movie["title"])

    # Loop through the user's watched movies and add their titles to user_set
    for user_movie in user_data["watched"]:
        user_set.add(user_movie["title"])

    # Find movies that the user has watched but friends haven't
    unique_title = user_set - friends_set
    
    # Create a list of movie dictionaries for those unique titles
    unique_movies = []

    for movie in user_data["watched"]:
        if movie["title"] in unique_title:
            unique_movies.append(movie)
    # Return the list of unique movies
    return unique_movies

def get_friends_unique_watched(user_data):
    # Create two sets: all movies friends have watched and all movies the user has watched
    friends_set = set()
    user_set = set()
    # Add all movie titles that friends have watched to friends_set
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            friends_set.add(friend_movie["title"])
    
    # Add all movie titles that the user has watched to user_set
    for user_movie in user_data["watched"]:
        user_set.add(user_movie["title"])
    # Find movies that friends have watched but the user has NOT watched
    unique_title = friends_set - user_set

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
    
    friends_unique_movies = get_friends_unique_watched(user_data)

    recommended_movies = []

    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    user_favorite_genre = get_most_watched_genre(user_data)
    friends_recommendations = get_friends_unique_watched(user_data)
    
    recommendations = []

    for movie in friends_recommendations:
        if movie["genre"] == user_favorite_genre:
            recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):

    favorite_movies_recommendation = []
    user_unique_movies = get_unique_watched(user_data)

    for movie in user_unique_movies:
        if movie in user_data["favorites"]:
            favorite_movies_recommendation.append(movie)

    return favorite_movies_recommendation

