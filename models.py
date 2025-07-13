import os
import uuid

from dotenv import load_dotenv
from peewee import PostgresqlDatabase, Model, UUIDField, CharField, ForeignKeyField, FloatField

load_dotenv()

db = PostgresqlDatabase(
    os.getenv('PSQL_DB'),
    user=os.getenv('PSQL_USER'),
    password=os.getenv('PSQL_PASS'),
    host=os.getenv('PSQL_HOST'),
    port=int(os.getenv('PSQL_PORT'))
)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = CharField()
    lastname = CharField()
    username = CharField()
    password_hash = CharField()

    class Meta:
        table_name = 'users'
        db = db


class Article(BaseModel):
    class Meta:
        table_name = 'articles'

    owner_id = ForeignKeyField(User, on_delete='CASCADE', field=User.id, backref='articles')
    timestamp = FloatField()
    text = CharField()
    tag = CharField(null=True, default=None)
    id = UUIDField(primary_key=True, default=uuid.uuid4)

