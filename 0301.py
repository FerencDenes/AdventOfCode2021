input = open('0301.in','r')
cnt = 0
arr = []
for i in range(12):
  arr.append(0)
for line in input:
  cnt+=1
  for i in range(len(line)):
    if line[i]=='1':
      arr[i]+=1
gamma =0
epsilon =0
for i in arr:
  gamma*=2
  epsilon*=2
  if i>cnt/2:
    gamma+=1
  else:
    epsilon+=1

print(gamma*epsilon)
