import mongoengine

<<<<<<< HEAD
class User(mongoengine.Document):
    name = mongoengine.StringField(required=True,max_length=50)
    position = mongoengine.StringField(required=True)
    extension = mongoengine.IntField()
    telephone = mongoengine.ListField()
    email = mongoengine.EmailField()
    department = mongoengine.StringField(max_length=20)
    company = mongoengine.StringField(max_length=20)
=======
class User(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField
>>>>>>> gradual start of models... no data added yet.
