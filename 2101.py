pos=[4,9]
score = [0,0]
rolled = 0
nextVal=1
nextPlayer=0
while score[0]<1000 and score[1]<1000:
  rolled+=3
  for _ in range(3):
    pos[nextPlayer]+=nextVal%10
    if pos[nextPlayer]>10:
      pos[nextPlayer]-=10
    nextVal+=1
    if nextVal>100:
      nextVal=1
  score[nextPlayer]+=pos[nextPlayer]

  nextPlayer = 1 if nextPlayer ==0 else 0

print(score[nextPlayer]*rolled)

states = dict()

memo = dict()
def win(p1,sc1,p2,sc2):
  ret = memo.get((p1,sc1,p2,sc2),None)
  if ret !=None:
    return ret

  w1=0
  w2=0
  for r1 in range(1,4):
    for r2 in range(1,4):
      for r3 in range(1,4):
        newPos=p1+r1+r2+r3
        if newPos>10:
          newPos-=10
        newScore = sc1+newPos
        if newScore>=21:
          w1+=1
        else:
          r=win(p2,sc2,newPos,newScore)
          w1+=r[1]
          w2+=r[0]
  memo[(p1,sc1,p2,sc2)]=(w1,w2)
  return (w1,w2)

ret = win(4,0,9,0)
print(max(ret))
