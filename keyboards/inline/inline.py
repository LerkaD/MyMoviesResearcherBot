from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot
import json
from database import show_history_movie
from loader import bot
from database import get_history_by_date

def show_first_history_page(chat_id, history, date):
    print(history[0])
    buttons = types.InlineKeyboardMarkup()

    curr_page_b = InlineKeyboardButton(text=f'1 / {len(history)}', callback_data=f' ')
    next_page_b = InlineKeyboardButton(text= f'->>', callback_data= '1' + ' ' + str(len(history)) + ' '+ str(date))
    close_button = InlineKeyboardButton(text=f'Закончить просмотр', callback_data=f'close')

    buttons.add(curr_page_b, next_page_b)
    buttons.add(close_button)

    bot.send_message(chat_id,show_history_movie(history[0]), reply_markup = buttons)

@bot.callback_query_handler(func=lambda call: call.data.split(' ') == 3)
def first_button(call):
    call_text = call.data.split(' ')

    curr_page = int(call_text[0])
    all_pages = int(call_text[1])
    date = call_text[2]

    history = get_history_by_date(date)
    buttons = types.InlineKeyboardMarkup()

    prev_page_b = InlineKeyboardButton(text=f'<<-', callback_data = str(curr_page - 1) + ' ' + str(len(history)) + ' ' + str(date))
    curr_page_b = InlineKeyboardButton(text=f'{curr_page + 1}/ {len(history)}', callback_data=f' ')
    next_page_b = InlineKeyboardButton(text=f'->>', callback_data = str(curr_page + 1) + ' ' + str(len(history)) + ' ' + str(date))
    close_button = InlineKeyboardButton(text=f'Закончить просмотр', callback_data=f'close')

    if curr_page == 0:
        buttons.add(curr_page_b, next_page_b)
    elif curr_page == all_pages - 1:
        buttons.add(prev_page_b,curr_page_b)
    else:
        buttons.add(prev_page_b,curr_page_b,next_page_b)
    buttons.add(close_button)

    bot.edit_message_text(show_history_movie(history[curr_page]),
                          reply_markup=buttons, chat_id=call.message.chat.id,
                          message_id=call.message.message_id)
