a = 2
b = 2
n = 17

# multiplicative inverses mod n = 17
D = {1:1, 2:9, 3:6, 4:13, 5:7, 
     8:15, 10:12, 11:14, 16:16}   
for k,v in D.items():  D[v] = k

# square roots
sqrtD = {1:(1,16), 2:(6,11), 4:(2,15), 
     8:(5,12), 9:(3,14), 
     13:(8,9), 15:(7,10), 16:(4,13)}   

def check(x,y):
  def f(x):
    return (x**3 + a*x + b) % n
  y_sq = f(x)
  ysqrts = sqrtD[y_sq]
  assert y in ysqrts
  #print x, y, ysqrts

def getx(s, x1, x2):
  return (s**2 - (x1 + x2)) % n

def gety(s,(x,y),X):
  ret = (s*(x-X) - y) 
  return ret % n

def add((x,y),(x2,y2)):
  num = (y2 - y)
  den = (x2 - x) % n
  s = (num * D[den]) % n
  X = getx(s,x,x2)
  return X, gety(s,(x,y),X)

def double((x,y), a=a):
  num = (3 * x**2 + a)
  den = (2 * y) % n
  s = (num * D[den]) % n
  X = getx(s,x,x)
  return X, gety(s,(x,y),X)

def makeG((x,y)):
  # 1G
  G = { 1:(x,y) }
  check(x,y)
  
  # 2G, 4G, 8G, 16G
  for i in range(4):
    X,Y = double((x,y))
    k = 2**(i+1)
    G[k] = (X,Y)
    x,y = X,Y
    check(x,y)
    
  # 3G..18G
  x,y = G[2]
  for i in range(3,19):
    X,Y = add(G[1],(x,y))
    if not i in G:
      G[i] = (X,Y)
    else:
      assert G[i] == (X,Y)
    x,y = X,Y
    check(x,y)
  return G
