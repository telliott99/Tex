from math import *

def hyp(a,b):
    return sqrt(a**2 + b**2)

A = 200
for a in range(8,25):
    b = (2.0*A)/a
    c = hyp(a,b)
    p = a + b + c
    print "%d %3.2f %3.2f" % (a,b,p)

