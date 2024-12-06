from telebot import types

def bud_keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('low', 'height')
    return markup