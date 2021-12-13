
input = open("1301.in","r")
dots = set()
for line in input:
  ls = line.strip()
  if ls == "":
    break
  [x,y]=ls.split(",")
  dots.add((int(x),int(y)))

first = True
for line in input:
  [s,n]=line.strip().split("=")
  n=int(n)
  newDots = set()
  for dot in dots:
    if s == "fold along x":
      if dot[0]<n:
        newDots.add(dot)
      elif dot[0]>n:
        newDots.add((2*n-dot[0], dot[1]))
    elif s == "fold along y":
      if dot[1]<n:
        newDots.add(dot)
      elif dot[1]>n:
        newDots.add((dot[0],2*n-dot[1]))
  dots=newDots
  if first:
    print(len(dots))
    first=False

for y in range(8):
  for x in range(40):
    if (x,y) in dots:
      print("#",end="")
    else:
      print(" ",end="")
  print()
