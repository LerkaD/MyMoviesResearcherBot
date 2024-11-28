#from telebot.types import Message
from loader import bot
from telebot.types import Message
from states.states import BotStates
from peewee import IntegrityError
from database.models import User


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name
        )
        bot.reply_to(message,
            'Привет! Я бот Kinopoisk. Я умею подбирать фильмы.\n\n'
            f'- /help. Обратиться за помощью\n'
            '- /find. Найти фильм')
    except IntegrityError:
        bot.reply_to(message, f"Рад вас снова видеть, {first_name}!")

    bot.set_state(message.from_user.id, BotStates.base, message.chat.id)