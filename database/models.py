from peewee import (
    AutoField,
    BooleanField,
    CharField,
    DateField,
    ForeignKeyField,
    IntegerField,
    Model,
    SqliteDatabase, FloatField,
)

from config_data.config import DATE_FORMAT, DB_PATH
import datetime
db = SqliteDatabase(DB_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = IntegerField(primary_key=True)
    username = CharField()
    first_name = CharField()

class MovieHistory(BaseModel):
    history_id = AutoField()
    user = ForeignKeyField(User, backref="user_hist")
    date = DateField(default=datetime.datetime.now().strftime(DATE_FORMAT))
    movie_title = CharField()
    movie_description = CharField()
    movie_rating = CharField() #FloatField()
    movie_year = CharField() #IntegerField()
    movie_genre = CharField()
    movie_age_rating = CharField() #IntegerField()
    movie_poster = CharField()
    is_watched = BooleanField(default=False)

    def __str__(self):
        return ("Дата запроса: {date}\n"
                "Название: {name}\n"
                "Описание: {description}\n"
                "Жанр: {genre}\n"
                "Год: {year}\n"
                "Рейтинг: {rating}\n"
                "Возрастной рейтинг: {age_rating}\n"
                "Постер: {poster}\n"
        .format(
            date=self.date,
            name = self.movie_title,
            description = self.movie_description,
            genre = self.movie_genre,
            year = self.movie_year,
            rating = self.movie_rating,
            age_rating = self.movie_age_rating,
            poster = self.movie_poster
        ))

def create_models():
    db.create_tables(BaseModel.__subclasses__())

# create_models()
#
# User.create(
#             user_id=1916238619,
#             username='ler4ikd',
#             first_name='Valeri♡'
#         )
#
# user_instance = User.get(User.user_id == 1916238619)
#
# MovieHistory.create(
#     user = user_instance,
#     movie_title = 'vovovo'
# )
