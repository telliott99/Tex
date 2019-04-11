import sys
from eutils import *

x,y = 5,1
if len(sys.argv) > 1:
  x = int(sys.argv[1])
  y = int(sys.argv[2])

G = makeG((x,y))

L = sorted(G.keys())

for i in L:
  print str(i).rjust(2),
print

for i in L:
  X = G[i][0]
  print str(X).rjust(2),
print

for i in L:
  Y = G[i][1]
  print str(Y).rjust(2),
print
