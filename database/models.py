
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
    user = ForeignKeyField(User, backref="tasks")
    date = DateField()
    movie_title = CharField()
    movie_description = CharField()
    movie_rating = FloatField()
    movie_year = IntegerField()
    movie_genre = CharField()
    movie_age_rating = IntegerField()
    movie_poster = CharField()
    is_watched = BooleanField(default=False)

    def __str__(self):
        return ("{history_id}. {user} {date} - {movie_title}"
        .format(
            history_id=self.history_id,
            user = self.user,
            date=self.date.strftime(DATE_FORMAT),
            movie_title = self.movie_title
        ))

def create_models():
    db.create_tables(BaseModel.__subclasses__())