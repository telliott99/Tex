from matplotlib import pyplot as plt
import numpy as np

def plot(X,Y):
    plt.scatter(X,Y,s=5)
    plt.axhline()
    plt.axvline()
    #plt.axes().set_aspect('equal')
    plt.savefig('x.png')

def cubic(a,b,c,d):
    def f(x):
        return a*x**3 + b*x**2 + c*x + d
    L = np.linspace(-10,10,2000)
    X = list()
    Y = list()
    for x in L:
        y = f(x)
        if y < -10 or y > 10:
            continue 
        X.append(x)
        Y.append(y)
    plot(X,Y)

cubic(1,1,1,1)