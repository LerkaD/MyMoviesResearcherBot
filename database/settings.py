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

def get_history_by_date(date):
    print(MovieHistory)
    query = MovieHistory.select().where(MovieHistory.date == date).limit(5)
    mov_history = query.dicts().execute()
    # for mov in mov_history:
    #     print(mov)
    #     print(mov['movie_title'])
    return mov_history

def show_history_movie(movie):
    return ("Дата запроса: {date}\n"
            "Название: {name}\n"
            "Описание: {description}\n"
            "Жанр: {genre}\n"
            "Год: {year}\n"
            "Рейтинг: {rating}\n"
            "Возрастной рейтинг: {age_rating}\n"
            "Постер: {poster}\n"
    .format(
        date=movie['date'],
        name=movie['movie_title'],
        description=movie['movie_description'],
        genre=movie['movie_genre'],
        year=movie['movie_year'],
        rating=movie['movie_rating'],
        age_rating=movie['movie_age_rating'],
        poster=movie['movie_poster']
    ))