## Telegram бот для поиска фильмов

MyMoviesResearcherBot — Telegram-бот на Python для поиска фильмов и сериалов по различным критериям. Работает с внешними API и локальной SQLite-базой данных через ORM Peewee. Управление диалогами реализовано с помощью встроенного FSM из библиотеки pyTelegramBotAPI.

### 🚀 Функциональность

* /movie_search — поиск фильма/сериала по названию

* /movie_by_rating — подборка фильмов/сериалов с высоким рейтингом

* /low_budget_movie — поиск бюджетных фильмов/сериалов

* /high_budget_movie — поиск дорогих фильмов/сериалов

* /history — просмотр истории пользовательских запросов

### 🛠️ Используемые технологии

* Python 3.10+

* pyTelegramBotAPI (telebot) — Telegram-бот

* FSM через StatesGroup и StateMemoryStorage — управление состояниями пользователя

* Peewee ORM + SQLite — хранение истории запросов

* requests — взаимодействие с внешним API для получения информации о фильмах

* dotenv — конфигурация через .env

### 📁 Структура проекта

MyMoviesResearcherBot/

├── api/                # Запросы к внешнему API (через requests)

├── config_data/        # Настройки и переменные окружения

├── database/

│   ├── models.py       # Модели для ORM (Peewee)

│   └── db_init.py      # Инициализация БД

├── handlers/           # Обработчики команд Telegram-бота

├── keyboards/          # Reply и Inline клавиатуры

├── states/             # FSM-состояния

├── utils/              # Вспомогательные функции

├── .env.template       # Пример переменных окружения

├── main.py             # Точка входа

└── requirements.txt    # Зависимости



