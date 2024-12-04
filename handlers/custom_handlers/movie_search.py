#from telebot.types import Message
from loader import bot
from telebot.types import Message
from states.states import BotStates
import api
from .operations import parse_results,check_request_data
from database.settings import add_movie_to_history
#from pagination.pagination import show_buttons, first_button


# @bot.message_handler(commands=['movie_search'])
# def get_movie_name(message: Message) -> None:
#     bot.send_message(
#         message.chat.id,
#         'Для поиска фильма по названию необходимо:\n'
#         '-ввести название фильма,\n'
#         '-ввести жанр фильма,\n'
#         '-ввести лимит поиска.\n'
#     )
#     bot.send_message(
#         message.chat.id,
#         'Введите название фильма для поиска.\n'
#     )
#     bot.set_state(message.from_user.id, BotStates.movie_search, message.chat.id)#смена состояния на movie_search state

# @bot.message_handler(commands=['movie_search'])
# def get_movie_name(message: Message) -> None:
#     user_id = message.from_user.id
#     bot.send_message(
#         message.chat.id,
#         'Для поиска фильма по названию необходимо:\n'
#         '-ввести название фильма,\n'
#         '-ввести жанр фильма,\n'
#         '-ввести лимит поиска.\n'
#     )
#     data_from_user = {}
#     print('1')
#     bot.register_next_step_handler(message.chat.id, get_title_from_user)

    #bot.set_state(message.from_user.id, BotStates.movie_search, message.chat.id)#смена состояния на movie_search state


# @bot.message_handler(state=BotStates.movie_search)
def movie_search(message: Message,data_from_user) -> None:
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data: #контекстный менеджер с данными о пользователе в чате
    #     if 'movie_name' not in data:
    #         data['movie_name'] = message.text
    #         bot.send_message(
    #             message.chat.id,
    #             'Введите название жанра фильма для поиска.\n'
    #         )
    #     elif 'movie_genre' not in data:
    #         data['movie_genre'] = message.text
    #         bot.send_message(
    #             message.chat.id,
    #             'Введите лимит поиска.\n'
    #         )
    #     elif 'limit' not in data:
    #         data['limit'] = message.text
    #         if len(data) == 3:
    #             result = api.movie_search(data)
    #             if result['total'] == 0:
    #                 check_request_data(bot, message, data)
    #             cur_user = message.from_user.id
    #             movies_list, mov_his_list = parse_results(result)#, mov_his_list
    #             add_movie_to_history(mov_his_list, cur_user)
    #             for movie in movies_list:
    #                 bot.send_message(message.chat.id, movie)# reply_markup=show_buttons())
    #             data.clear()
    #             bot.set_state(message.from_user.id, BotStates.base,message.chat.id)
    try:
        limit = message.text
        if not limit.isdigit():
            msg = bot.reply_to(message, 'Лимит - целое число. Введите лимит')
            bot.register_next_step_handler(msg, movie_search, data_from_user)
            return
        data_from_user['limit'] = limit
        print(data_from_user)
        result = api.movie_search(data_from_user)
        if result['total'] == 0:
            check_request_data(bot, message, data_from_user)
        cur_user = message.from_user.id
        movies_list, mov_his_list = parse_results(result)#, mov_his_list
        add_movie_to_history(mov_his_list, cur_user)
        for movie in movies_list:
            bot.send_message(message.chat.id, movie)# reply_markup=show_buttons())
        data_from_user.clear()
        bot.set_state(message.from_user.id, BotStates.base,message.chat.id)
    except Exception as e:
        bot.reply_to(message, 'ой-ой-ой')

@bot.message_handler(commands=['movie_search'])
def get_title_from_user(message):
    try:
        data_from_user = {}
        print('get_title_from_user')
        user_id = message.from_user.id
        print(data_from_user, message.text)
        bot.send_message(
            message.chat.id,
            'Введите название фильма для поиска.\n'
        )
        print(data_from_user, message.text)
        bot.register_next_step_handler(message, get_genre_from_user,data_from_user)
    except Exception as e:
        bot.reply_to(message, 'ой-ой-ой')

def get_genre_from_user(message,data_from_user):
    user_id = message.from_user.id
    data_from_user['movie_name'] = message.text
    print(data_from_user, message.text)
    bot.send_message(
        message.chat.id,
        'Введите жанр фильма для поиска.\n'
    )
    bot.register_next_step_handler(message, get_limit_from_user, data_from_user)


def get_limit_from_user(message,data_from_user):
    try:
        user_id = message.from_user.id
        data_from_user['movie_genre'] = message.text
        print(data_from_user, message.text)
        bot.send_message(
            message.chat.id,
            'Введите лимит фильма для поиска.\n'
        )
        bot.register_next_step_handler(message, movie_search, data_from_user)
        # bot.set_state(message.from_user.id, BotStates.movie_search, message.chat.id,data_from_user )#смена состояния на movie_search state
    except Exception as e:
        bot.reply_to(message, 'ой-ой-ой')
    # bot.set_state(message.from_user.id, BotStates.movie_search, message.chat.id)#смена состояния на movie_search state
