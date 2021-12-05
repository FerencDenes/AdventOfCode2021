input = open('0501.in','r')
s=dict()
res=0
for line in input:
  v1,v2=line.split(' -> ')
  x1,y1 = v1.split(',')
  x1=int(x1)
  y1=int(y1)
  x2,y2=v2.split(',')
  x2=int(x2)
  y2=int(y2)
  if x1 == x2:
    if y1>y2:
      y2,y1=y1,y2
    for i in range(y1,y2+1):
      s[(x1,i)]=s.get((x1,i),0)+1
  elif y1==y2:
    if x1>x2:
      x2,x1=x1,x2
    for i in range(x1,x2+1):
      s[(i,y1)]=s.get((i,y1),0)+1
  else:
    incy = 1 if y1<y2 else -1
    incx = 1 if x1<x2 else -1
    y=y1
    for x in range(x1,x2+incx,incx):
      s[(x,y)]=s.get((x,y),0)+1
      y+=incy

print(len(list(filter(lambda i:i>1,s.values()))))
