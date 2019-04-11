import numpy as np

a,b,c = 1, 1, 1

def f(x):
    return x**3 + a*x**2 + b*x + c

def getX(x1,x2):
    N = 1000
    return np.linspace(x1,x2,N)

# assumes we go from f(x) < 0 to f(x) > 0
def guess(x1, x2):
    std_order = f(x1) < f(x2)
    
    print 'guess'
    print 'x1 = ', str(x1)
    print 'x2 = ', str(x2)
    print 'y1 = ', str(f(x1))
    print 'y2 = ', str(f(x2))
    print
    
    X = getX(x1,x2)
    if not std_order:
        X.reverse()
    assert f(X[0]) < 0 and f(X[-1]) > 0
    
    for i,x1 in enumerate(X):
        x2 = X[i+1]
        # must happen
        if f(x2) > 0:
            if not std_order:
                return x2, x1
            return x1, x2
     
def close(r):
    e = 1e-12
    return not (r > e or r < -e)
    
x1 = -2
x2 =  0
i = 0

while i < 100:
    print i+1
    x1, x2 = guess(x1, x2)
    if close(x2 - x1):
        break
    i += 1
