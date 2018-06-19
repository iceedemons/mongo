import mongoengine

class User(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField