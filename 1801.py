lines = [line.strip() for line in open("1801.in","r")]

pos = 0
class Node:
  def __init__(self):
    self.rightVal=None
    self.leftVal=None

  @classmethod
  def createFromString(cls,line):
    cls.pos=1
    return cls.fromString(line)

  @classmethod
  def fromString(cls,line):
    self = Node()
    if line[cls.pos]=="[":
      cls.pos+=1
      self.left = Node.fromString(line)
      self.leftVal = None
    else:
      self.leftVal = int(line[cls.pos])
      cls.pos+=1
    cls.pos+=1
    if line[cls.pos]=="[":
      cls.pos+=1
      self.right = Node.fromString(line)
      self.rightVal=None
    else:
      self.rightVal = int(line[cls.pos])
      cls.pos+=1
    cls.pos+=1
    return self

  def __repr__(self):
    return f'[{self.leftVal if self.leftVal!=None else self.left},{self.rightVal if self.rightVal!=None else self.right}]'

  def addLeft(self,val):
    return

  def addRight(self,val):
    return

  def explode(self,depth):
    l=0
    r=0
    if depth == 3 and self.leftVal==None:
      if self.rightVal == None:
        self.right.leftVal += self.left.rightVal
      else:
        self.rightVal+=self.left.rightVal
      ret = self.left.leftVal
      self.left = None
      self.leftVal = 0
      return (ret,0,True)
    if depth == 3 and self.rightVal == None:
      if self.leftVal==None:
        self.left.rightval += self.right.leftVal
      else:
        self.leftVal+=self.right.leftVal
      ret = self.right.rightVal
      self.right=None
      self.rightVal=0
      return (0,ret,True)
    if self.leftVal ==None:
      (l,r,fl)=self.left.explode(depth+1)
      if r!=0:
        if self.rightVal!=None:
          self.rightVal+=r
          r=0
        elif self.right.leftVal!=None:
          self.right.leftVal+=r
          r=0
        elif self.right.left.leftVal!=None:
          self.right.left.leftVal+=r
          r=0
        elif self.right.left.left.leftVal!=None:
          self.right.left.left.leftVal+=r
          r=0
        elif self.right.left.left.left.leftVal!=None:
          self.right.left.left.left.leftVal+=r
          r=0
      if fl:
        return (l,r,fl)
    if self.rightVal == None:
      (l,r,fl)=self.right.explode(depth+1)
      if l!=0:
        if self.leftVal!=None:
          self.leftVal+=l
          l=0
        elif self.left.rightVal!=None:
          self.left.rightVal+=l
          l=0
        elif self.left.right.rightVal!=None:
          self.left.right.rightVal+=l
          l=0
        elif self.left.right.right.rightVal!=None:
          self.left.right.right.rightVal+=l
          l=0
        elif self.left.right.right.right.rightVal!=None:
          self.left.right.right.right.rightVal+=l
          l=0
      if fl:
        return (l,r,fl)
    return (0,0,False)

  def split(self):
    if self.leftVal != None and self.leftVal>=10:
      self.left = Node()
      self.left.leftVal=self.leftVal//2
      self.left.rightVal=self.leftVal//2 + self.leftVal%2
      self.leftVal=None
      return True
    if self.leftVal==None:
      if self.left.split():
        return True
    if self.rightVal != None and self.rightVal>=10:
      self.right = Node()
      self.right.leftVal=self.rightVal//2
      self.right.rightVal=self.rightVal//2 + self.rightVal%2
      self.rightVal=None
      return True

    if self.rightVal==None:
      if self.right.split():
        return True
    return False

  def relax(self):
    fl=True
    while fl:
      while fl:
        (_,_,fl)=self.explode(0)
      fl=self.split()

  def add(self,node):
    ret = Node()
    ret.left=self
    ret.right=node
    ret.relax()
    return ret

  def eval(self):
    ret=0
    if self.leftVal!=None:
      ret+=3*self.leftVal
    else:
      ret+=3*self.left.eval()
    if self.rightVal!=None:
      ret+=2*self.rightVal
    else:
      ret+=2*self.right.eval()
    return ret


first = True
for line in lines:
  if first:
    node = Node.createFromString(lines[0])
    first=False
    continue
  newNode = Node.createFromString(line.strip())
  node=node.add(newNode)
print(node.eval())

max = 0
for i in range(len(lines)):
  for j in range(len(lines)):
    if i!=j:
      n1 = Node.createFromString(lines[i])
      n2 = Node.createFromString(lines[j])
      val = n1.add(n2).eval()
      if val>max:
        max=val
print(max)

nodes= {
  "[[6,[5,[4,[3,2]]]],1]":"[[6,[5,[7,0]]],3]",
"[[[[[9,8],1],2],3],4]":"[[[[0,9],2],3],4]",
"[7,[6,[5,[4,[3,2]]]]]":"[7,[6,[5,[7,0]]]]",
"[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]":"[[3,[2,[8,0]]],[9,[5,[7,0]]]]",
"[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]":"[[3,[2,[8,0]]],[9,[5,[7,0]]]]",
"[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]":"[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"}
for n in nodes:
  node = Node.createFromString(n)
  node.relax()
  if (node.__repr__()!=nodes[n]):
    print(n, nodes[n], node)

nodes={
  "[[1,2],[[3,4],5]]":143,
  "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]":1384
}
for n in nodes:
  node = Node.createFromString(n)
  if (node.eval()!=nodes[n]):
    print(n, nodes[n], node.eval())
