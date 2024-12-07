from .models import MovieHistory

def get_history_by_date(date):
    # print('MovieHistory')
    query = MovieHistory.select().where(MovieHistory.date == date)
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