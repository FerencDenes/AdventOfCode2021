oct = [[int(x) for x in line.strip()] for line in open("1101.in","r")]

cnt = 0

def incr(x,y):
  global cnt,oct
  oct[x][y]+=1
  if oct[x][y]==10:
    cnt+=1
    if x>0:
      if y>0:
        incr(x-1,y-1)
      incr(x-1,y)
      if y<9:
        incr(x-1,y+1)
    if y>0:
      incr(x,y-1)
      if x<9:
        incr(x+1,y-1)
    if x<9:
      incr(x+1,y)
      if y<9:
        incr(x+1,y+1)
    if y<9:
      incr(x,y+1)


for step in range(1000):
  # for x in range(len(oct)):
  #   print(''.join(map(lambda s: str(s),oct[x])))
  # print()
  cntRound=cnt
  for x in range(len(oct)):
    for y in range(len(oct[x])):
      incr(x,y)
  for x in range(len(oct)):
    for y in range(len(oct[x])):
      if oct[x][y]>9:
        oct[x][y]=0
  if step == 99:
    print(cnt)
  if cntRound+100==cnt:
    print(step+1)
    break
