code = [line.strip() for line in open("2401.in","r")]

w=[0]*14
w2=[0]*14
z=list()
for i in range(0,len(code),18):
  instr= code[i+4]
  if instr.endswith("1"):
    z.append((int(code[i+15].split()[2]),i//18))
  else:
    x=int(code[i+5].split()[2])
    (lastval,ind) = z.pop()
    if lastval+x<0:
      w[ind]=9
      w[i//18]=9+(lastval+x)
      w2[ind]=1-(lastval+x)
      w2[i//18]=1
    else:
      w[ind]=9-(lastval+x)
      w[i//18]=9

      w2[ind]=1
      w2[i//18]=1+(lastval+x)
print("".join(map(str,w)))
print("".join(map(str,w2)))

