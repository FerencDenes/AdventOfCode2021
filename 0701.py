from collections import Counter
from functools import reduce


input = open('0701.in','r')
vals = list(map(lambda x:int(x), input.readline().strip().split(',')))
sum = sum(vals)
avg = round(sum/len(vals))

fuel = 100000000000
fuel2 = 100000000000

for i in range(min(vals),max(vals)+1):
  v= reduce(lambda x,y:x+abs(i-y),vals,0)
  if v<fuel:
    fuel=v
  v= reduce(lambda x,y:x+(abs(i-y)*(abs(i-y)+1)/2),vals,0)
  if v<fuel2:
    fuel2=v

print(fuel)
print(int(fuel2))
