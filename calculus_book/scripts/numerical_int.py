from math import e, pi, sqrt

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
    return x**2

integrate(0,1,f)
integrate(1,2,f)

def g(x):
    exp = -0.5*x**2
    norm = sqrt(2*pi)
    return e**(exp) / norm

for b in [2,4,6,8,10]:
    print str(b).rjust(2),
    integrate(-b,b,g)
