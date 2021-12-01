#!/usr/bin/python

input = open('0101.in','r')
prev = 1000000000
p1, p2, p3 = 1000000000, 1000000000, 1000000000
count =0
count2=0
for line in input:
  num = int(line)
  if prev < num:
    count +=1
  if p1+p2+p3 < p2+p3+num:
    count2 +=1
  p1,p2,p3= p2,p3,num

  prev = num


print count
print count2
