import re
from collections import defaultdict

input = open("1701.in","r")
(x1,x2,y1,y2) = map(int,re.findall(r'-?\d+',input.readline().strip()))
# (x1,x2,y1,y2) = (20,30,-10,-5)
xDict = defaultdict(list)
yDict = defaultdict(list)

for y in range(y1-1,-y1+2):
  s=0
  j=y
  i=0
  while s>=y1:
    s+=j
    j-=1
    if y1<=s<=y2:
      yDict[i].append(y)
    i+=1


for x in range(x2+1):
  s =0
  j=x
  for i in range(max(yDict.keys())+1):
    s+=j
    j= 0 if j==0 else j-1
    if x1<=s<=x2:
      xDict[i].append(x)


solutionSet = set()
for step in yDict:
  for x in xDict[step]:
    for y in yDict[step]:
      solutionSet.add((x,y))

print(y1*(y1+1)//2)
print(len(solutionSet))


