from database.models import MovieHistory
from states.states import BotStates

def get_movie_name(movie):
    if movie['name']:
        movie_name = movie['name']
    else:
        movie_name = movie['alternativeName']
    return movie_name

def get_description(movie):
    if movie['description']:
        return movie['description']
    elif movie['shortDescription']:
        return movie['shortDescription']
    else:
        return 'Нет описания'

def get_poster(movie):
    if movie['poster']['url']:
        return movie['poster']['url']
    else:
        return 'Нет описания'

def get_budget(movie):
    ...

def get_rating(movie):
    if movie['rating']['kp']:
        return movie['rating']['kp']
    else:
        return 'Нет описания'

def get_year(movie):
    if movie['year']:
        return movie['year']
    else:
        return 'Нет описания'

def get_age_rating(movie):
    if movie['ageRating']:
        return movie['ageRating']
    else:
        return 'Нет описания'

def get_genres(movie):
    if movie['genres']:
        genres = []
        for genre in movie['genres']:
            print(genre['name'])
            genres.append(genre['name'])
        return ', '.join(genres)
    else:
        return 'Нет описания'

def add_movie_to_history(req_data, cur_user):
    for movie in req_data['docs']:
        new_movie = MovieHistory(
            user=cur_user,
            movie_title=get_movie_name(movie),
            movie_description=get_description(movie),
            movie_rating=get_rating(movie),
            movie_year=get_year(movie),
            movie_genre=get_genres(movie),
            movie_age_rating=get_description(movie),
            movie_poster=get_poster(movie)
        )
        new_movie.save()
