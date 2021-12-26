import re


p=re.compile("o(.).*x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)")
inp = list(map(lambda a: (a[0]=="n",int(a[1]),int(a[2]),int(a[3]),int(a[4]),int(a[5]),int(a[6])),[p.match(line.strip()).groups() for line in open("2201.in","r")]))

ons = set()
for a in filter(lambda a:all(map(lambda x:-50<=x<=50,[a[x] for x in range(1,7) ])),inp):
  for x in range(a[1],a[2]+1):
      for y in range(a[3],a[4]+1):
        for z in range(a[5],a[6]+1):
          if a[0]:
            ons.add((x,y,z))
          elif ons.__contains__((x,y,z)):
            ons.remove((x,y,z))

print(len(ons))

def range_intersect(x11,x12,x21,x22):
  if x11>x22 or x12<x21:
    return None
  [_,a,b,_]=sorted([x11,x12,x21,x22])
  return (a,b)

class Cube1:
  def __init__(self,x1,x2,y1,y2,z1,z2):
    self.x1=x1
    self.x2=x2
    self.y1=y1
    self.y2=y2
    self.z1=z1
    self.z2=z2
    self.offs = []
  @property
  def volume(self):
    return (self.x2-self.x1+1)*(self.y2-self.y1+1)*(self.z2-self.z1+1)-sum(off.volume for off in self.offs)
  def intersect(self,other):
    xi=range_intersect(self.x1,self.x2,other.x1,other.x2)
    if xi == None:
      return
    yi=range_intersect(self.y1,self.y2,other.y1,other.y2)
    if yi == None:
      return
    zi=range_intersect(self.z1,self.z2,other.z1,other.z2)
    if zi == None:
      return
    for off in self.offs:
      off.intersect(other)
    self.offs.append(Cube1(xi[0],xi[1],yi[0],yi[1],zi[0],zi[1]))


cubes = list()

for a in inp:
  cube=Cube1(a[1],a[2],a[3],a[4],a[5],a[6])
  for c in cubes:
    c.intersect(cube)
  if a[0]:
    cubes.append(cube)

print(sum(map(lambda c:c.volume,cubes)))
