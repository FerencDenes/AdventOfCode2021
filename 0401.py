def mark(b,n):
  for i in range(len(b)):
    for j in range(len(b[i])):
      if n==b[i][j]:
        b[i][j]='X'

def check(b):
  chk = 0
  for i in range(len(b)):
    x =1
    y=1
    for j in range(len(b[i])):
      if b[i][j] !='X':
        x=0
      if b[j][i]!='X':
        y=0
    if x==1 or y==1:
      return 1
  return 0

def play(draws, boards):
  for d in draws:
    for k in range(len(boards)):
      b=boards[k]
      mark(b,d)
      if check(b) == 1:
        sum=0
        for i in b:
          for j in i:
            sum+=0 if j=='X' else int(j)
        del(boards[k])
        return sum*int(d)
  return -1



input = open('0401.in','r')

draws = input.readline().split(',')
input.readline()
borards = []
current = []
for line in input:
  if line == '\n':
    borards.append(current)
    current = []
  else:
    current.append(line.split())
borards.append(current)



print(play(draws,borards))
last =0
for i in draws:
  val = play(draws,borards)
  if val!=-1:
    last=val
print(last)
