from math import floor
from operator import itemgetter

def f(n,d):
    return 1.0*n**2/d**2

def fit(n,d):
    try:
        return abs(2.0 - f(n,d))
    except:
        return 10
    
def d_for(n):
    s = 2**0.5
    d = floor(n/s)
    g = fit(n,d)
    g_prev = fit(n,d-1)
    
    if g < g_prev:
        return (d,g)
    return d-1,g_prev

pow = 4
L = list()
for n in range(2,int(10**pow)):
    d, g = d_for(n)
    L.append((n, d, g))
    
L.sort(key=itemgetter(2))
for e in L[:5]:
    print(e)


