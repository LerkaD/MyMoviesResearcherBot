from loader import bot
from telebot.types import Message
from states.states import BotStates
from database.models import User, MovieHistory
from typing import List
from database import get_history_by_date, show_history_movie
from keyboards import show_pagination_buttons

@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    bot.send_message( message.chat.id, 'История запросов')
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    history = get_history_by_date('05.12.2024')
    bot.send_message(message.chat.id, show_history_movie(history)) #reply_markup = show_pagination_buttons())
    bot.set_state(message.from_user.id, BotStates.base, message.chat.id)
