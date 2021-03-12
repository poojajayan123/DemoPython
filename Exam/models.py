from mongoengine import Document, EmbeddedDocument, fields
from Category.models import Category
from User.models import User
from Question.models import Question

class Exam(Document):
    examName = fields.StringField(max_length=200)
    userId = fields.ReferenceField(User)
    questionIds = fields.ReferenceField(Question)
    categoryId = fields.ReferenceField(Category)

    def __str__(self):
        self.examName

