import mongoengine

class User(mongoengine.Document):
    name = mongoengine.StringField(required=True,max_length=50)
    position = mongoengine.StringField(required=True)
    extension = mongoengine.IntField()
    telephone = mongoengine.ListField()
    email = mongoengine.EmailField()
    department = mongoengine.StringField(max_length=20)
    company = mongoengine.StringField(max_length=20)