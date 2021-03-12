from mongoengine import Document, EmbeddedDocument, fields
import datetime
        
class Category(Document):
    name = fields.StringField(max_length=50,required=True)
    
    
    def __str__(self):
        return self.name