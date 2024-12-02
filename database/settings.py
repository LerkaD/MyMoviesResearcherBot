from .models import MovieHistory

def add_movie_to_history(movies, cur_user):
    for movie in movies:
        new_movie = MovieHistory(
            user = cur_user,
            movie_title = movie[0],
            movie_description = movie[1],
            movie_rating =  str(movie[3]),
            movie_year = str(movie[2]),
            movie_genre = movie[6],
            movie_age_rating =  str(movie[4]),
            movie_poster = movie[5]
        )
        new_movie.save()
