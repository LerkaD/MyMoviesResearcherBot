from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage


state_storage = StateMemoryStorage()
class BotStates(StatesGroup):
    base = State()
    movie_search = State()
    movie_by_rating = State()
    low_budget_movie = State()
    high_budget_movie = State()


