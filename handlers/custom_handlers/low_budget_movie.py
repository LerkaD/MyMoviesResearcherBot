from loader import bot
from telebot.types import Message
import api
from states.states import BotStates
from .operations import parse_results, check_request_data
from database.settings import add_movie_to_history


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
    bot.set_state(message.from_user.id, BotStates.low_budget_movie, message.chat.id)

@bot.message_handler(state=BotStates.low_budget_movie)
def low_budget_movies_search(message: Message) -> None:
    print('into')
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data: #контекстный менеджер с данными о пользователе в чате
        print(data)
        if 'movie_genre' not in data:
            data['movie_genre'] = message.text
            bot.send_message(
                message.chat.id,
                'Введите лимит поиска.\n'
            )
        elif 'limit' not in data:
            data['limit'] = message.text
            if len(data) == 2:
                result = api.get_low_budget_movie(data)
                if result['total'] == 0:
                    check_request_data(bot, message, data)
                cur_user = message.from_user.id
                movies_list, mov_his_list = parse_results(result)  # , mov_his_list
                add_movie_to_history(mov_his_list, cur_user)
                for movie in movies_list:
                    bot.send_message(message.chat.id, movie)
                data.clear()
                bot.set_state(message.from_user.id, BotStates.base,message.chat.id)
