from loader import bot
from telebot.types import Message
from states.states import BotStates
from . import operations as oper
import api

def parse_results(req_data: dict):
    movies_list = []
    # movie_info = []
    for movie in req_data['docs']:
        movie_info = (
            f"Название: {oper.check_description(movie, 'name')}\n"
            f"Описание: {oper.check_description(movie, 'description')}\n"
            f"Год: {oper.check_description(movie, 'year')}\n"
            f"Рейтинг: {oper.check_description(movie, 'rating')}\n"
            f"Возрастное ограничение: {oper.check_description(movie, 'ageRating')}\n"
            f"Постер: {oper.check_description(movie, 'poster')}\n"
            "-------------------------\n"
        )
        #print(movie_info)
        movies_list.append(movie_info)
    return movies_list

@bot.message_handler(commands=['low_budget_movie'])
def get_low_budget_movies(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'Для поиска фильмов с низким необходимо:\n'
        '-ввести жанр фильма,\n'
        '-ввести лимит поиска.\n'
    )
    bot.send_message(
        message.chat.id,
        'Введите жанр фильма для поиска.\n'
    )
    bot.set_state(message.from_user.id, BotStates.low_budget_movie, message.chat.id)#смена состояния на movie_search state

@bot.message_handler(state=BotStates.low_budget_movie)
def low_budget_movies_search(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data: #контекстный менеджер с данными о пользователе в чате
        if 'movie_genre' not in data:
            data['movie_genre'] = message.text
            bot.send_message(
                message.chat.id,
                'Введите лимит поиска.\n'
            )
        elif 'limit' not in data:
            data['limit'] = message.text
            if len(data) == 2:
                print(data)
                result = api.get_low_budget_movie(data)
                movies_list = parse_results(result)
                for movie in movies_list:
                    bot.send_message(message.chat.id, movie)
                bot.set_state(message.from_user.id, BotStates.base,message.chat.id)  # смена состояния на movie_search state

                  # смена состояния на movie_search state

