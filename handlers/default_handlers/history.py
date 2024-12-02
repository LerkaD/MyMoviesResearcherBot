from loader import bot
from telebot.types import Message
from states.states import BotStates
from database.models import User, MovieHistory
from typing import List

@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'История запросов'
    )
    user_id = message.from_user.id
    user = User.get_or_none(User.user_id == user_id)
    if user is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    user_hist: List[MovieHistory] = user.user_hist.order_by(-MovieHistory.date, -MovieHistory.history_id).limit(10)

    result = []
    result.extend(map(str, reversed(user_hist)))

    if not result:
        bot.send_message(message.from_user.id, "У вас ещё нет истории поиска")
        return

    bot.send_message(message.from_user.id, "\n".join(result))
    bot.set_state(message.from_user.id, BotStates.base, message.chat.id)