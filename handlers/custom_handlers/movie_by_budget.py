from loader import bot
from telebot.types import Message
from api import get_low_budget_movie, get_high_budget_movie
from states import BotStates
from telebot import types
from .operations import parse_results
from database import add_movie_to_history
from keyboards import bud_keyboard

@bot.message_handler(commands=['movie_by_budget'])
def movie_by_budget(message: Message) -> None:
    bot.send_message(message.chat.id,'Введите жанр фильма для поиска.\n')
    data_from_user = {}
    bot.register_next_step_handler(message, process_get_genre, data_from_user)

def process_get_genre(message,data_from_user):
    try:
        #user_id = message.from_user.id
        data_from_user['movie_genre'] = message.text
        #print(data_from_user, message.text)
        bot.send_message(message.chat.id, 'Введите лимит фильма для поиска.\n')
        bot.register_next_step_handler(message, process_get_limit, data_from_user)
    except Exception as e:
        bot.reply_to(message, 'ой-ой-ой')

def process_get_limit(message,data_from_user):
    #user_id = message.from_user.id
    try:
        limit = message.text
        if not limit.isdigit():
            msg = bot.reply_to(message, 'Лимит - целое число. Введите лимит')
            bot.register_next_step_handler(msg, process_get_limit, data_from_user)
            return
        data_from_user['limit'] = message.text
        # markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        # markup.add('low', 'height')
        budget_message = bot.send_message(message.chat.id, 'Выберите бюджет', reply_markup=bud_keyboard())
        bot.register_next_step_handler(budget_message, show_result, data_from_user)
    except Exception as e:
        bot.reply_to(message, 'ой-ой-ой')


def show_result(message, data):
    result = get_movies_by_budget(message, data)
    if result:
        movies_list, mov_his_list = parse_results(result)  # , mov_his_list
        add_movie_to_history(mov_his_list, message.from_user.id)
        for movie in movies_list:
            bot.send_message(message.chat.id, movie)  # reply_markup=show_buttons())
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')
    bot.set_state(message.from_user.id, BotStates.base, message.chat.id)


def get_movies_by_budget(message: Message, data) -> None:
    try:
        print(message.text, data)
        if message.text == 'low':
            result = get_low_budget_movie(data)
        elif  message.text == 'height':
            result = get_high_budget_movie(data)
        else:
            budget_message = bot.send_message(message.chat.id, 'Выберите бюджет', reply_markup=bud_keyboard())
            bot.register_next_step_handler(budget_message, get_movies_by_budget, data)
            return
        return result
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Произошла ошибка..Попробуйте заново.')


