import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase

# id (Integer, primary_key, autoincrement)
# surname (String) (фамилия)
# name (String) (имя)
# age (Integer) (возраст)
# position (String) (должность)
# speciality (String) (профессия)
# address (String) (адрес)
# email (String, unique) (электронная почта)
# hashed_password (String) (хэшированный пароль)
# modified_date (DateTime) (дата изменения)

class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    position = sqlalchemy.Column(sqlalchemy.Integer)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)


    jobs = orm.relationship("Jobs", back_populates='user')