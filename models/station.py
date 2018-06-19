import mongoengine

from models.reel import Reel


class Station(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField()
    reels = mongoengine.EmbeddedDocumentListField(Reel)

    @property
    def reel_qty(self):
        return len(self.reels)