#from telebot.types import Message
from datetime import datetime
from keyboards import show_first_history_page
from config_data import DATE_FORMAT
from loader import bot
from telebot.types import Message
from states import BotStates
import api
from .operations import add_movie_to_history
from keyboards.inline.reseaches_pages import show_first_pag_page

@bot.message_handler(commands=['movie_search'])
def start_movie_search(message):
    try:
        data_from_user = {}
        bot.send_message( message.chat.id, 'Введите название фильма для поиска.\n')
        bot.register_next_step_handler(message, process_movie_name,data_from_user)
    except Exception as e:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id )

def process_movie_name(message,data_from_user):
    try:
        data_from_user['movie_name'] = message.text
        # print(data_from_user, message.text)
        bot.send_message( message.chat.id, 'Введите жанр фильма для поиска.\n' )
        bot.register_next_step_handler(message, process_movie_genre, data_from_user)
    except Exception:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

def process_movie_genre(message,data_from_user):
    try:
        data_from_user['movie_genre'] = message.text
        bot.send_message( message.chat.id, 'Введите лимит фильма для поиска.\n')
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
        print(data_from_user)
        researching_movie(message, data_from_user)
    except Exception as e:
        bot.reply_to(message, 'Что- то не так. Выберите операцию')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

def researching_movie(message,data_from_user):
    try:
        print(data_from_user)
        result = api.movie_search(data_from_user)
        if result:
            add_movie_to_history(result, message.from_user.id)
            show_first_pag_page(message.chat.id, datetime.now().strftime(DATE_FORMAT), int(data_from_user['limit']))
            # bot.set_state(message.from_user.id, BotStates.base,message.chat.id)
        else:
            raise bot.send_message(message.chat.id, 'По вашему запросу ничего не найдено')  #
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, 'Произошла ошибка. Попробуйте заново.')
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)