import mongoengine


class Client(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField
