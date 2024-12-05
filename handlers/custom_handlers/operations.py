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

def parse_results(req_data):
    movies_list = []
    movies_history_list= []
    for movie in req_data['docs']:
        name = get_movie_name(movie)
        description = get_description(movie)
        year = get_year(movie)
        rating = get_rating(movie)
        age_rating = get_description(movie)
        poster = get_poster(movie)
        genre = get_genres(movie)
        movie_info = (
            f"Название: {name}\n"
            f"Описание: {description}\n"
            f"Жанр: {genre}\n"
            f"Год: {year}\n"
            f"Рейтинг: {rating}\n"
            f"Возрастной рейтинг: {age_rating}\n"
            f"Постер: {poster}\n"
            # "-------------------------\n"
        )
        movie_history_info = [name, description, year, rating, age_rating, poster, genre]
        print(type(movie_info), movie_info)
        movies_list.append(movie_info)
        movies_history_list.append(movie_history_info)
    return movies_list, movies_history_list
