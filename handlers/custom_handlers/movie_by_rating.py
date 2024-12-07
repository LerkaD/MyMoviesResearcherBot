from loader import bot
from telebot.types import Message
from states.states import BotStates
from api import get_movie_by_rating
from .operations import add_movie_to_history
from datetime import datetime
from config_data import DATE_FORMAT
from keyboards import show_first_pag_page

@bot.message_handler(commands=['movie_by_rating'])
def start_movie_by_rating(message: Message) -> None:
    try:
        bot.send_message(message.chat.id,'Введите рейтинг фильма для поиска.\n')
        data_from_user = {}
        bot.register_next_step_handler(message, process_movie_rating, data_from_user)
    except Exception:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

def process_movie_rating(message,data_from_user):
    try:
        if float(message.text) < 0 or float(message.text) > 10:
            bot.send_message(message.chat.id, 'Рейтинг: число в пределах от 0 до 10. Введите рейтинг фильма.\n')
            bot.register_next_step_handler(message, process_movie_rating, data_from_user)
            return
        data_from_user['movie_rating'] = message.text
        bot.send_message(message.chat.id, 'Введите жанр фильма для поиска.\n')
        bot.register_next_step_handler(message, process_movie_genre, data_from_user)
    except ValueError:
        bot.send_message(message.chat.id, 'Рейтинг: число. Введите рейтинг фильма.\n')
        bot.register_next_step_handler(message, process_movie_rating, data_from_user)
    except Exception as e:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

def process_movie_genre(message,data_from_user):
    try:
        data_from_user['movie_genre'] = message.text
        bot.send_message(message.chat.id, 'Введите лимит фильма для поиска.\n')
        bot.register_next_step_handler(message, process_movie_limit, data_from_user)
    except Exception as e:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

def process_movie_limit(message: Message,data_from_user) -> None:
    try:
        limit = message.text
        if not limit.isdigit():
            msg = bot.reply_to(message, 'Лимит - целое число. Введите лимит')
            bot.register_next_step_handler(msg, process_movie_limit, data_from_user)
            return
        data_from_user['limit'] = limit
        researching_movie_by_rating(message, data_from_user)
    except Exception as e:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

def researching_movie_by_rating(message,data_from_user):
    try:
        result = get_movie_by_rating(data_from_user)
        if result:
            add_movie_to_history(result, message.from_user.id)
            show_first_pag_page(message.chat.id, datetime.now().strftime(DATE_FORMAT), int(data_from_user['limit']))
            bot.set_state(message.from_user.id, BotStates.base,message.chat.id)
        else:
            raise bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')#
    except Exception as e:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)


