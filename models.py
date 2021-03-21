from peewee import *
from datetime import datetime, date
from flask_login import UserMixin
import os

from playhouse.db_url import connect

DATABASE = connect(os.environ.get('DATABASE_URL'))

# DATABASE = PostgresqlDatabase('rackets', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = DATABASE

class Person(UserMixin, BaseModel):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    
class Singles(BaseModel):
    person = ForeignKeyField(Person, backref='single')
    date = DateField(
        formats="%d/%m/%Y",
        default=date.today
    )
    opponent = CharField(null = True)
    score = CharField(null = True)
    win = BooleanField()
    notes = TextField(null = True)
    

class Doubles(BaseModel):
    person = ForeignKeyField(Person, backref='double')
    date = DateField(
        formats="%d/%m/%Y",
        default=date.today
    )
    opponent = CharField(null = True)
    partner = CharField(null = True)
    hand = CharField()
    score = CharField(null = True)
    win = BooleanField()
    change = BooleanField(null = True)
    notes = TextField(null = True)

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Person, Singles, Doubles])
    print("Database tables created.")
    DATABASE.close()