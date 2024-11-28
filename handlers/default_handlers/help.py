#from telebot.types import Message
from loader import bot
from telebot.types import Message

from states.states import BotStates


@bot.message_handler(commands=['help'])
def help(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'Я могу следующее\n\n'
        f'- /movie_search — поиск фильма/сериала по названию;\n'
        f'- /movie_by_rating — поиск фильмов/сериалов по рейтингу;\n'
        f'- /low_budget_movie — поиск фильмов/сериалов с низким бюджетом;\n'
        f'- /high_budget_movie — поиск фильмов/сериалов с высоким бюджетом;\n'
        f'- /history — возможность просмотра истории запросов и поиска фильма/сериала.\n'
    )
    bot.set_state(message.from_user.id, BotStates.base, message.chat.id)