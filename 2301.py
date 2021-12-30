
#############
#...........#
###C#A#B#D###
  #B#A#D#C#
  #########

pitval = {1:1,10:2,100:3,1000:4}
pitpos = {1:2,10:4,100:6,1000:8}

hwpos = {0:0,1:1,2:3,3:5,4:7,5:9,6:10}
inp = [line for line in open("2301.in","r")]
def toCost(c):
  if c=="A":
    return 1
  if c=="B":
    return 10
  if c=="C":
    return 100
  return 1000

state0=((0,0,0,0,0,0,0),
  (toCost(inp[2][3]),toCost(inp[3][3])),
  (toCost(inp[2][5]),toCost(inp[3][5])),
  (toCost(inp[2][7]),toCost(inp[3][7])),
  (toCost(inp[2][9]),toCost(inp[3][9])),
  )

inf = 10000000000000

#find if the apm can move in
def pitFree(state,a):
  pit = pitval[a]
  pi=-1
  for p in state[pit]:
    if p!=0 and p!=a:
      return -1
    if p==0:
      pi+=1
  return pi

def hwFreeToPop(hw,pos,pit):
  if pos<=pit:
    for i in range(pos,pit+1):
      if hw[i]!=0:
        return False
  else:
    for i in range(pit+1,pos+1):
      if hw[i]!=0:
        return False
  return True

def hwFreeToPush(hw,pos,pit):
  if pos<=pit:
    for i in range(pos+1,pit+1):
      if hw[i]!=0:
        return False
  else:
    for i in range(pit+1,pos):
      if hw[i]!=0:
        return False
  return True

finalState = ((0,0,0,0,0,0,0),(1,1),(10,10),(100,100),(1000,1000))
def solve(state):
  if state == finalState:
    return 0
  # slam dunk
  for ai in range(len(state[0])):
    a=state[0][ai]
    if a!=0:
      pf = pitFree(state,a)
      if pf!=-1:
        if  hwFreeToPush(state[0],ai,pitval[a]):
          newHw = list(state[0])
          newHw[ai]=0
          newHw = tuple(newHw)
          newState = list()
          newState.append(newHw)
          for t in range(1,5):
            if t==pitval[a]:
              newPit = list(state[t])
              for t2 in range(len(newPit)-1,-1,-1):
                if newPit[t2]==0:
                  newPit[t2]=a
                  break
              newState.append(tuple(newPit))
            else:
              newState.append(state[t])
          cost = a*(abs(hwpos[ai]-pitpos[a])+1+pf)
          return cost+solve(tuple(newState))

  # move out all to all positions
  minRet = inf
  for pv in range(1,5):
    toPop=False
    toPopPos =-1
    for pp in range(len(state[pv])-1,-1,-1):
      if state[pv][pp]!=0 and pitval[state[pv][pp]]!=pv:
        toPop = True
      if toPop and state[pv][pp]!=0:
        toPopPos = pp
    if toPop:
      for hw in range(7):
        if hwFreeToPop(state[0],hw,pv):
          #create new state and call solve
          newHw = list(state[0])
          newHw[hw]=state[pv][toPopPos]
          newHw = tuple(newHw)
          newState = list()
          newState.append(newHw)
          for t in range(1,5):
            if t==pv:
              newPit = list(state[t])
              for t2 in range(len(newPit)-1,-1,-1):
                if t2==toPopPos:
                  newPit[t2]=0
                  break
              newState.append(tuple(newPit))
            else:
              newState.append(state[t])
          cost = state[pv][toPopPos]*(abs(hwpos[hw]-pv*2)+1+toPopPos)
          ret = cost+solve(tuple(newState))
          if ret<minRet:
            minRet=ret
  return minRet


print(solve(state0))

  #D#C#B#A#
  #D#B#A#C#
state02 = (state0[0],
  (state0[1][0],1000,1000,state0[1][1]),
  (state0[2][0],100,10,state0[2][1]),
  (state0[3][0],10,1,state0[3][1]),
  (state0[4][0],1,100,state0[4][1]),
)
finalState = ((0,0,0,0,0,0,0),(1,1,1,1),(10,10,10,10),(100,100,100,100),(1000,1000,1000,1000))

print(solve(state02))
