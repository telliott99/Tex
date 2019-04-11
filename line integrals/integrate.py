import numpy as np
import scipy.integrate

def integrate(f,start=0,stop=1,N=100):
    R,dx = np.linspace(start,stop,N,
                       endpoint=False,
                       retstep=True)
    mid = 0.5*dx
    R = [n + mid for n in R]
    return sum([f(n)*dx for n in R])

f = lambda x: x**2
g = lambda x: np.sqrt(1 + 4*x**2)
print integrate(f)
print integrate(g,0,1,1000)
print scipy.integrate.quad(g,0,1)[0]