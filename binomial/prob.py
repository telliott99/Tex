from math import factorial
import matplotlib.pyplot as plt

N = 100
p = 0.5**N
L = [1,1]
for i in range(2,N+1):
    next = L[-1] * i
    L.append(next)

assert L[37] == factorial(37)
f = factorial(100)

def choose(n,k):
    return 1.0*L[n] / (L[k] * L[n-k])

R = range(N + 1)
pL = [choose(N,k)*p for k in R]
for k in R:
    print k, pL[k]

sL = pL[30:71]
plt.scatter(range(len(sL)),sL,s=100,color='b')
plt.savefig('example.png')


