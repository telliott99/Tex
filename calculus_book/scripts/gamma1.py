from math import e, pi, sqrt
import sys
n = float(sys.argv[1])

def get_xvalues(a,b,N):
    dist = 1.0*b - 1.0*a
    dx = dist/N
    half = dx/2.0
    R = [(a + dx * n + half) for n in range(N)]
    return R, dx
    
def integrate(a,b,f,N=100):
    '''integrate function f over [a,b]'''
    L, dx = get_xvalues(a,b,N)
    values = [f(x) for x in L]
    print sum(values) * dx
    
def f(x):
    return (x - x**2)**n
    
integrate(0,1,f)