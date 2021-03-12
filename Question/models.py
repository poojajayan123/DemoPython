from mongoengine import Document, EmbeddedDocument, fields
from Category.models import Category

# Create your models here.

class Question(Document): 
    category = fields.ReferenceField(Category) 
    question = fields.StringField(max_length=500) 
    optionA = fields.StringField(max_length=100)
    optionB = fields.StringField(max_length=100)
    optionC = fields.StringField(max_length=100)
    optionD = fields.StringField(max_length=100)
    answer = fields.StringField(max_length=10)
  
    def __str__(self): 
        return self.question