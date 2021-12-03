
def count(a):
  arr=[]
  for i in range(12):
    arr.append(0)
  for line in a:
    for i in range(len(line)):
      if line[i]=='1':
        arr[i]+=1
  return arr

input = open('0301.in','r')
o2 = []
co2 = []
for line in input:
  o2.append(line)
  co2.append(line)
for i in range(12):
  if len(o2)>1:
    o2count = count(o2)
    o2 = list(filter(lambda val:val[i]==('1' if o2count[i]>=len(o2)/2 else '0'),o2))
  if len(co2)>1:
    co2count = count(co2)
    co2 = list(filter(lambda val:val[i]==('1' if co2count[i]<len(co2)/2 else '0'),co2))
  print(len(o2),len(co2))


print(int(o2[0],2)*int( co2[0],2))





# gamma =0
# epsilon =0
# for i in arr:
#   gamma*=2
#   epsilon*=2
#   if i>cnt/2:
#     gamma+=1
#   else:
#     epsilon+=1

# print(gamma*epsilon)
