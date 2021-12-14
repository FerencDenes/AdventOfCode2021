from collections import defaultdict
from typing import Counter


input = open("1401.in","r")
pol = input.readline().strip()
lastChar = pol[len(pol)-1]
input.readline()

rules = {(k[0],k[1]):v for (k,v) in [line.strip().split(" -> ") for line in input]}

polList = [(pol[n],pol[n+1]) for n in range(len(pol)-1)]

for i in range(10):
  newPol = pol[0]
  for n in range(len(pol)-1):
    insert = rules.get((pol[n],pol[n+1]),"")
    newPol += insert+pol[n+1]
  pol=newPol
  if i==9:
    vals = list(Counter(pol).values())
    vals.sort()
    print(vals[len(vals)-1]-vals[0])

polDist = dict()
for source in polList:
  polDist[source] = polDist.get(source,0)+1

for i in range(40):
  newPolDict = dict()
  for source in polDist.keys():
    c = rules.get(source,"")
    if c == "":
      newPolDict[source] = polDist[source]
    else:
      newPolDict[(source[0],c)] = newPolDict.get((source[0],c),0) + polDist[source]
      newPolDict[(c,source[1])] = newPolDict.get((c,source[1]),0) + polDist[source]
  polDist = newPolDict
  if i==9 or i == 39:
    cntDict = defaultdict(lambda:0)
    for c in polDist:
      cntDict[c[0]]+=polDist[c]
    cntDict[lastChar]+=1
    vals = list(cntDict.values())
    vals.sort()
    print(vals[len(vals)-1]-vals[0])



