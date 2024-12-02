from loader import bot
from telebot.types import Message
from states.states import BotStates
import api
from .operations import parse_results, check_request_data
from database.settings import add_movie_to_history

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
                result = api.get_movie_by_rating(data)
                if result['total'] == 0:
                    check_request_data(bot, message, data)
                cur_user = message.from_user.id
                movies_list, mov_his_list = parse_results(result)  # , mov_his_list
                add_movie_to_history(mov_his_list, cur_user)
                for movie in movies_list:
                    bot.send_message(message.chat.id, movie)
                data.clear()
                bot.set_state(message.from_user.id, BotStates.base,message.chat.id)  # смена состояния на movie_search state