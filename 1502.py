graph = [[[int(x),1000000000] for x in line.strip()] for line in open("1501.in","r")]

def visit(a,b,mincost):
  n = graph[a][b]
  if not visited.__contains__((a,b)) and (mincost + n[0] < n[1]):
    n[1] = mincost + n[0]
    unvisited.add((a,b))

x= len(graph)-1
y= len(graph[0])-1
unvisited = set([(0,0)])
visited = set()

def solve():
  graph[0][0][1]=0
  while not visited.__contains__((x,y)):
    min =  (x,y)
    for node in unvisited:
      if graph[min[0]][min[1]][1] > graph[node[0]][node[1]][1]:
        min = node
    mincost = graph[min[0]][min[1]][1]
    if min[0]>0:
      visit(min[0]-1,min[1],mincost)
    if min[0]<x:
      visit(min[0]+1,min[1],mincost)
    if min[1]>0 :
      visit(min[0],min[1]-1,mincost)
    if min[1]<y:
      visit(min[0],min[1]+1,mincost)
    visited.add(min)
    unvisited.remove(min)

  print(graph[x][y][1])

solve()
graph0 = [[[int(x),1000000000] for x in line.strip()] for line in open("1501.in","r")]
graph = list()
for j in range(5):
  for row in graph0:
    row0 = list()
    for i in range(5):
      for item in row:
        newVal = item[0]+i+j
        while newVal > 9 :
          newVal -= 9
        row0.append([newVal,1000000000])
    graph.append(row0)
x= len(graph)-1
y= len(graph[0])-1
unvisited = set([(0,0)])
visited = set()
solve()
