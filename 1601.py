import math

input = open("1601.in","r")
line = input.readline().strip()

bin = ''
for c in line:
  bin+=f'{int(c,16):0>4b}'

verSum = 0
def parseHeader(i):
  global verSum
  verSum += int(bin[i],2)*4 + int(bin[i+1],2)*2 + int(bin[i+2],2)
  i+=3
  type = int(bin[i]+bin[i+1]+bin[i+2],2)
  i+=3
  return i,type

def parsePacket(i,packetNo,length, ind):
  till = i+length
  ret = list()
  while (ind==0 and i<till) or (ind ==1 and packetNo>0):
    packetNo-=1
    i,type = parseHeader(i)
    if type ==4:
      val = 0
      while bin[i]=="1":
        val *=16
        val +=int(bin[i+1]+bin[i+2]+bin[i+3]+bin[i+4],2)
        i+=5
      val *=16
      val +=int(bin[i+1]+bin[i+2]+bin[i+3]+bin[i+4],2)
      i+=5
      ret.append(val)
    else:
      subPackets = 0
      if bin[i]=="0":
        i+=1
        for j in range(15):
          subPackets*=2
          if bin[i]=="1":
            subPackets+=1
          i+=1
        i,subVal=parsePacket(i,0,subPackets,0)
      else:
        i+=1
        for j in range(11):
          subPackets*=2
          if bin[i]=="1":
            subPackets+=1
          i+=1
        i,subVal=parsePacket(i,subPackets,0, 1)

      if type == 0:
        ret.append(sum(subVal))
      elif type == 1:
        ret.append(math.prod(subVal))
      elif type ==2:
        ret.append(min(subVal))
      elif type==3:
        ret.append(max(subVal))
      elif type == 5:
        ret.append(1 if subVal[0]>subVal[1] else 0)
      elif type == 6:
        ret.append(1 if subVal[0]<subVal[1] else 0)
      elif type == 7:
        ret.append(1 if subVal[0]==subVal[1] else 0)

  return i, ret

_,val = parsePacket(0,1,0,1)
print(verSum)
print(val[0])
