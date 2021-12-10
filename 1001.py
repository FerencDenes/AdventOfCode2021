input = open("1001.in","r")

cnt = 0
cnt2=[]
for line in input:
  st = []
  wrong = False
  for c in line.strip():
    if c=='(':
      st.append(')')
    elif c=='{':
      st.append('}')
    elif c=='[':
      st.append(']')
    elif c=='<':
      st.append('>')
    else:
      p=st.pop()
      if c!=p:
        wrong = True
        if c==')':
          cnt+=3
        elif c==']':
          cnt+=57
        elif c=='}':
          cnt+=1197
        elif c=='>':
          cnt+=25137
  if not wrong:
    subcnt =0
    st.reverse()
    for c in st:
      subcnt*=5
      if c == ')':
        subcnt+=1
      elif c== ']':
        subcnt+=2
      elif c=='}':
        subcnt+=3
      elif c=='>':
        subcnt+=4
    cnt2.append(subcnt)
print(cnt)
cnt2.sort()
print(cnt2[int((len(cnt2)-1)/2)])
