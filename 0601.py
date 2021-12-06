
from functools import reduce
from typing import Counter

def simulate(c):
  c2=dict()
  c2[8]=c.get(0,0)
  c2[6]=c.get(0,0)
  for j in range(9):
    c2[j]=c.get(j+1,0)+c2.get(j,0)
  return c2

input = open('0601.in','r')
vals = map(lambda x:int(x), input.readline().strip().split(','))

c=Counter(vals)
for i in range(80):
  c=simulate(c)
print(sum(c.values()))

for i in range(256-80):
  c=simulate(c)
print(sum(c.values()))
