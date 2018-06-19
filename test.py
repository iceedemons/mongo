from models.proposal import Proposal
from models.reel import Reel
from models.station import Station

s3 = Station(name="Station 3")
s2 = Station(name="Station 2")
r1 = Reel(name="reel 1")
s1 = Station(name="Station 1")
r2 = Reel(name="reel 2")
r3 = Reel(name="reel 3")
p1 = Proposal(name="test proposal",number=12351)
p2 = Proposal(name="test test number 2",number=55555)

p1.stations.append(s2)
p1.stations.append(s1)
p2.stations.append(s1)
s1.reels.append(r1)
s1.reels.append(r2)
s2.reels.append(r3)

print(p1.station_qty)
print(p1.reel_qty)
print(p2.station_qty)
print(p2.reel_qty)