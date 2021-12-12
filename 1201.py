from collections import defaultdict


input = [line.strip().split("-") for line in open("1201.in","r")]
graph = defaultdict(list)
for edge in input:
  if edge[1]!="start":
    graph[edge[0]].append(edge[1])
  if edge[0]!="start":
    graph[edge[1]].append(edge[0])

route = ["start"]
cnt =0
def traverse():
  global cnt, route, graph
  last = route[len(route)-1]
  if last == "end":
    cnt+=1
  else:
    for cave in graph[last]:
      if cave.lower() == cave:
        if not route.__contains__(cave):
          route.append(cave)
          traverse()
      else:
        route.append(cave)
        traverse()
  route.pop()


traverse()
print(cnt)

route = ["start"]
cnt2=0
twice = False
def traverse2():
  global cnt2, twice, route, graph
  last = route[len(route)-1]
  if last == "end":
    cnt2+=1
  else:
    for cave in graph[last]:
      if cave.lower() == cave:
        if route.count(cave)==0:
          route.append(cave)
          traverse2()
        elif route.count(cave)==1 and not twice:
          twice = True
          route.append(cave)
          traverse2()
      else:
        route.append(cave)
        traverse2()
  cave = route.pop()
  if cave.lower()==cave and route.__contains__(cave):
    twice = False

route = ["start"]
cnt2=0
twice = False
traverse2()
print(cnt2)

route = ["start"]
cnt2=0
twice = True
traverse2()
print(cnt2)
