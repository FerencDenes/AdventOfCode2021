from os import path
from typing import Counter


input = open("0801.in","r")
cnt=0
cnt2=0
lenSet=set([2,4,3,7])
for line in input:
  [test, val] = line.strip().split(' | ')
  cnt+= len(list(filter(lambda x:lenSet.__contains__( len(x)), val.split())))

  tests = test.split()

  byOcc = Counter(test)
  del(byOcc[' '])
  for (k,v) in byOcc.items():
    if v==9:
      f=k
    if v==6:
      b=k
    if v==4:
      e=k

  for t in tests:
    if len(t) == 2:
      if t[0]==f:
        c=t[1]
      else:
        c=t[0]
  for t in tests:
    if len(t)==4:
      for ch in t:
        if ch!=b and ch!=c and ch!=f:
          d=ch
    if len(t) ==3:
      for ch in t:
        if ch!=c and ch!=f:
          a=ch
  for (k,v) in byOcc.items():
    if v==7 and k!=d:
      g=k

  subres =0
  for v in val.split():
    subres*=10
    if len(v)==2:
      subres+=1
    elif len(v)==5 and v.__contains__(e):
      subres+=2
    elif len(v)==5 and v.__contains__(c):
      subres+=3
    elif len(v) == 4:
      subres+=4
    elif len(v)==5:
      subres+=5
    elif len(v)==6 and v.__contains__(d) and v.__contains__(e):
      subres+=6
    elif len(v)==3:
      subres+=7
    elif len(v) ==7:
      subres+=8
    elif len(v)==6 and v.__contains__(d):
      subres+=9
  cnt2+=subres

print(cnt)
print(cnt2)
