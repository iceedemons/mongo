import mongoengine


class Site(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField
