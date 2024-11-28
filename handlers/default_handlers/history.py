from loader import bot
from telebot.types import Message
from states.states import BotStates


@bot.message_handler(commands=['history'])
def history(message: Message) -> None:
    bot.send_message(
        message.chat.id,
        'История запросов : еще не реализована'
    )
    bot.set_state(message.from_user.id, BotStates.base, message.chat.id)