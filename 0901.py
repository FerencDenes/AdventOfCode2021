input = open("0901.in","r")

arr = [[int(x) for x in line.strip()] for line in input]
cnt =0
sizes = []
for i in range(len(arr)):
  for j in range(len(arr[i])):
    x=arr[i][j]
    if (i==0 or arr[i-1][j]>x) and (j==0 or arr[i][j-1]>x) and (i==len(arr)-1 or arr[i+1][j]>x) and (j==len(arr[i])-1 or arr[i][j+1]>x):
      cnt+=1+x
      visited=set()
      toVisit =[(i,j)]
      while len(toVisit)>0:
        item=toVisit.pop()
        k=item[0]
        l=item[1]
        itemVal=arr[k][l]
        if itemVal<9 and not visited.__contains__(item):
          visited.add(item)
          if k>0 and arr[k-1][l]>itemVal:
            toVisit.append((k-1,l))
          if l>0 and arr[k][l-1]>itemVal:
            toVisit.append((k,l-1))
          if k<len(arr)-1 and arr[k+1][l]>itemVal:
            toVisit.append((k+1,l))
          if l<len(arr[k])-1 and arr[k][l+1]>itemVal:
            toVisit.append((k,l+1))
      sizes.append(len(visited))
sizes.sort(reverse=True)
print(cnt)
print(sizes[0]*sizes[1]*sizes[2])
