input = open('0201.in','r')

fwd = 0
depth =0
aim=0
depth2=0
for line in input:
  [comm,val]=line.split()
  if comm == "forward":
    fwd+=int(val)
    depth2+=aim*int(val)
  if comm == "up":
    depth-=int(val)
    aim-=int(val)
  if comm == "down":
    depth+=int(val)
    aim+=int(val)
print(fwd*depth)
print(fwd*depth2)
