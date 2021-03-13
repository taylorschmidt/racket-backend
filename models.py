from peewee import *
import datetime
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

class Doubles(BaseModel):

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Person, Singles, Doubles])
    print("Database tables created.")
    DATABASE.close()