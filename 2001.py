input = open("2001.in","r")
code = [c=='#' for c in input.readline().strip()]

input.readline()
map = [[c=="#" for c in "".rjust(51,".")+line.strip()+"".rjust(51,".")] for line in input ]
for _ in range(51):
  map.insert(0,[False for _ in range(len(map[0]))])
  map.append([False for _ in range(len(map[0]))])

infVal = False
for round in range(50):
  m2= list()
  for i in range(len(map)):
    row=list()
    for j in range(len(map[i])):
      ind=0
      for (x,y) in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
        ind*=2
        xi=i+x
        yj=j+y
        if xi<0 or yj<0 or xi>=len(map) or yj>=len(map[0]):
          if infVal:
            ind+=1
        elif map[xi][yj]:
          ind+=1
      row.append(code[ind])
    m2.append(row)
  infVal= code[0] and not infVal
  map=m2
  if round == 1 or round == 49:
    cnt=0
    for i in range(len(map)):
      for j in range(len(map[i])):
        if map[i][j]:
          cnt+=1
    print(cnt)
