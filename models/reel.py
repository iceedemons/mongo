import mongoengine


class Reel(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField()

