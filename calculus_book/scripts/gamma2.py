from matplotlib import pyplot as plt
import numpy as np

p = 81
q = 219

def f(x):
    return x**(p-1)*(1-x)**(q-1)
    
X = np.linspace(0,1,1000)
Y = [f(x)*1e90 for x in X]
m = max(Y)
Y = [y*1.0/m for y in Y]

plt.scatter(X,Y,s=5,c='red')
plt.savefig('example.png')