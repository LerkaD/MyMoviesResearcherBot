from loader import bot
from telebot.types import Message
from states.states import BotStates
from .operations import parse_results, check_request_data
import api
from database.settings import add_movie_to_history



@bot.message_handler(commands=['high_budget_movie'])
def get_high_budget_movies(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'Для поиска фильмов с высоким бюджетом необходимо:\n'
        '-ввести жанр фильма,\n'
        '-ввести лимит поиска.\n'
    )
    bot.send_message(
        message.chat.id,
        'Введите жанр фильма для поиска.\n'
    )
    bot.set_state(message.from_user.id, BotStates.high_budget_movie, message.chat.id)#смена состояния на movie_search state

@bot.message_handler(state=BotStates.high_budget_movie)
def high_budget_movies_search(message: Message) -> None:
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
                result = api.get_high_budget_movie()
                if result['total'] == 0:
                    check_request_data(bot, message, data)
                cur_user = message.from_user.id
                movies_list, mov_his_list = parse_results(result)  # , mov_his_list
                add_movie_to_history(mov_his_list, cur_user)
                for movie in movies_list:
                    bot.send_message(message.chat.id, movie)
                data.clear()
                bot.set_state(message.from_user.id, BotStates.base,message.chat.id)  # смена состояния на movie_search state
