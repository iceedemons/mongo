import mongoengine

from models.client import Client
from models.site import Site
from models.station import Station
from models.user import User


class Proposal(mongoengine.Document):
    number = mongoengine.IntField(required=True)
    name = mongoengine.StringField(required=True)
    client = mongoengine.EmbeddedDocumentField(Client)
    createdBy = mongoengine.EmbeddedDocumentField(User)
    checkedBy = mongoengine.EmbeddedDocumentField(User)
    approvedBy = mongoengine.EmbeddedDocumentField(User)
    site = mongoengine.EmbeddedDocumentField(Site)
    stations = mongoengine.EmbeddedDocumentListField(Station)

    @property
    def station_qty(self):
        return len(self.stations)

    @property
    def reel_qty(self):
        x = 0
        for station in self.stations:
            for reels in station.reels:
                x += len(reels)
        return x

