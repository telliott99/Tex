# Cardano's method for solving
# x^3 + mx = n 

import sys
from math import sqrt

def simplify(a,b,c):
    f = 1.0*a/3
    g = a*f   # a^2/3
    m = -g + b
    h = f*g   # a^3/3^2
    j = h/3   # a^3/3^3
    return m, (-j + h - (a*b*1.0)/3 + c)

def cardano(m,n):
    c = (m**3)/27
    h = n/2.0
    r = 0.3333333333

    rad1 = ( h + sqrt(h**2 + c))
    rad2 = (-h + sqrt(h**2 + c))
    return round(rad1**r - rad2**r, 5)
