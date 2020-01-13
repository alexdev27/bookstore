
from mongoengine import Document, StringField


class Book(Document):
    name = StringField()
    description = StringField()
