from loader import bot
from telebot.types import Message
from states import BotStates
from database import User, MovieHistory
from config_data import DATE_FORMAT
from database import get_history_by_date, show_history_movie
from keyboards import show_first_history_page
from datetime import datetime


@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    bot.send_message( message.chat.id, 'История запросов')
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return
    bot.send_message(message.chat.id, 'Введите дату в формате : дд.мм.гг')
    bot.register_next_step_handler(message,get_history_process)

def get_history_process(message):
    try:
        date = message.text
        datetime.strptime(date, DATE_FORMAT)
        history = get_history_by_date(date)
    except ValueError:
        bot.send_message(message.chat.id, 'Дата не верна. Введите дату в формате : дд.мм.гг')
        bot.register_next_step_handler(message,get_history_process)
        return
    if history:
        show_first_history_page(message.chat.id, history, date)
    else:
        bot.send_message(message.chat.id, 'В день: {date} история пуста.'.format(date = message.text)) #reply_markup = show_pagination_buttons())
        bot.set_state(message.from_user.id, BotStates.base, message.chat.id)

