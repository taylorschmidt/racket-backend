from peewee import *
from datetime import datetime, date
from flask_login import UserMixin

DATABASE = PostgresqlDatabase('rackets', host='localhost', port=5432)

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
    opponent = CharField()
    score = CharField()
    win = BooleanField()
    notes = TextField()
    

class Doubles(BaseModel):
    person = ForeignKeyField(Person, backref='double')
    date = DateField(
        formats="%d/%m/%Y",
        default=date.today
    )
    opponent = CharField()
    partner = CharField()
    hand = CharField()
    score = CharField()
    win = BooleanField()
    change = BooleanField()
    notes = TextField()

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Person, Singles, Doubles])
    print("Database tables created.")
    DATABASE.close()