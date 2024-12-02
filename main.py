from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from telebot import custom_filters
from database.models import create_models

if __name__ == "__main__":
    create_models()
    bot.add_custom_filter(custom_filters.StateFilter(bot))# обработка сообщений в зависимости от текещго состояния
    set_default_commands(bot)
    bot.infinity_polling()
