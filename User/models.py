from mongoengine import Document, EmbeddedDocument, fields
from Category.models import Category
import datetime

class User(Document):
    name = fields.StringField(max_length=100,required=True)
    email = fields.StringField(max_length=250, required=True)
    password = fields.StringField(max_length=50,required=True)
    createdAt = fields.StringField(default=datetime.datetime.now)
    Category = fields.ReferenceField(Category)

    def __str__(self):
        return self.name