import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_KEY = os.getenv("API_KEY")
API_BASE_URL = ' https://api.kinopoisk.dev/'

DEFAULT_COMMANDS = (
    ("start", "запустить бота"),
    ("help", "вывести справку"),
    ("movie_search", "поиск фильма по названию"),
    ("movie_by_rating",  "Поиск фильмов/сериалов по рейтингу"),
    ("low_budget_movie", "поиск фильмов/сериалов с низким бюджетом"),
    ("high_budget_movie", "поиск фильмов/сериалов с высоким бюджетом"),
    ("history",  "просмотр истории запросов и поиска фильма/сериала")
)

DB_PATH = "kino_data_base.db"

DATE_FORMAT = "%d.%m.%Y"
