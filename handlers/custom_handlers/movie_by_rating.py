from loader import bot
from telebot.types import Message
from states.states import BotStates
import api

@bot.message_handler(commands=['movie_by_rating'])
def get_movie_by_rating(message: Message) -> None:
    print("'commands=['movie_by_rating']'")
    bot.send_message(
        message.chat.id,
        'Для поиска фильмов по рейтингу необходимо:\n'
        '-ввести рейтинг фильма,\n'
        '-ввести жанр фильма,\n'
        '-ввести лимит поиска.\n'
    )
    bot.send_message(
        message.chat.id,
        'Введите рейтинг фильма для поиска.\n'
    )
    bot.set_state(message.from_user.id, BotStates.movie_by_rating, message.chat.id)#смена состояния на movie_search state

@bot.message_handler(state=BotStates.movie_by_rating)
def search_movie_by_rating(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data: #контекстный менеджер с данными о пользователе в чате
        if 'movie_rating' not in data:
            data['movie_rating'] = message.text
            bot.send_message(
                message.chat.id,
                'Введите название жанра фильма для поиска.\n'
            )
        elif 'movie_genre' not in data:
            data['movie_genre'] = message.text
            bot.send_message(
                message.chat.id,
                'Введите лимит поиска.\n'
            )
        elif 'limit' not in data:
            data['limit'] = message.text
            if len(data) == 3:
                print(data)
                result = api.get_movie_by_rating(data)
                movies_list = []
                for movie in result['docs']:
                    movie_info = (
                        f"Название: {movie['name']}\n"
                        f"Описание: {movie['description']}\n"
                        f"Год: {movie['year']}\n"
                        f"Рейтинг: {movie['rating']['kp']}\n"
                        f"Возрастное ограничение: {movie['ageRating']}\n"
                        f"Постер: {movie['poster']['url']}\n"
                        "-------------------------\n"
                    )
                    movies_list.append(movie_info)
                for movie in movies_list:
                    bot.send_message(message.chat.id, movie)
                bot.set_state(message.from_user.id, BotStates.base,message.chat.id)  # смена состояния на movie_search state