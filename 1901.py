from collections import defaultdict

lines  =[line.strip() for line in  open("1901.in","r")]
class Scanner:
  def __init__(self,name):
    self.name=name
    self.beacons=set()
    self.rotation = 0
    self.rotateDict=defaultdict(list)
    self.matched = False
    self.pos = (0,0,0)

  def addBeacon(self,s):
    self.beacons.add(tuple(map(int,s.split(","))))
  def __repr__(self):
    return self.beacons.__repr__()

  def rotate(self):
    tmpBeacons = set()
    for beacon in self.beacons:
      newBeacon = (beacon[0],-beacon[2],beacon[1])
      if self.rotation==4 or self.rotation == 8 or self.rotation == 12:
            newBeacon = (-newBeacon[2],newBeacon[1],newBeacon[0])
      if self.rotation == 16:
            newBeacon = (-newBeacon[1],newBeacon[0],newBeacon[2])
      if self.rotation==20:
            newBeacon = (-newBeacon[0],-newBeacon[1],newBeacon[2])
      tmpBeacons.add(newBeacon)
    self.beacons=tmpBeacons
    self.rotateDict[self.rotation]= tmpBeacons
    self.rotation+=1

  def tryMatch(self,other):
    for r in other.rotateDict:
      for sb in self.rotateDict[self.rotation]:
        for ob in other.rotateDict[r]:
          d0,d1,d2= sb[0]-ob[0],sb[1]-ob[1],sb[2]-ob[2]
          matches = 0
          for sb2 in self.rotateDict[self.rotation]:
            ind=(sb2[0]-d0,sb2[1]-d1,sb2[2]-d2)
            if other.rotateDict[r].__contains__(ind):
              matches+=1
          if matches>=12:
            other.pos=(self.pos[0]+d0,self.pos[1]+d1,self.pos[2]+d2)
            other.matched=True
            other.rotation = r
            return True
    return False

scanners: list[Scanner] = list()

for line in lines:
  if line == "":
    continue
  if line.startswith("---"):
    scanners.append(Scanner(line))
  else:
    scanners[len(scanners)-1].addBeacon(line)

for sc in scanners:
  for r in range(24):
    sc.rotate()
  sc.rotation =0

matched = set([0])
scanners[0].matched=True
while len(matched)<len(scanners):
  newMatched=set()
  for i in matched:
    for j in range(len(scanners)):
      if i!=j and scanners[i].matched==True and scanners[j].matched==False and scanners[i].tryMatch(scanners[j]):
        newMatched.add(j)
  matched= matched.union(newMatched)

beacons = set()
maxDist = 0
for sc in scanners:
  for b in sc.rotateDict[sc.rotation]:
    beacons.add((sc.pos[0]+b[0],sc.pos[1]+b[1],sc.pos[2]+b[2]))
  for sc2 in scanners:
    dist = abs( sc.pos[0]-sc2.pos[0]) + abs( sc.pos[1]-sc2.pos[1])+abs( sc.pos[2]-sc2.pos[2])
    if dist>maxDist:
      maxDist=dist

print(len(beacons))
print(maxDist)



