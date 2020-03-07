# best rational approximation to a target
def fit(n,d):
    return abs(n/d - t)

t = 2**0.5
n = 5
d = 7

def test(n,d,where='N'):
    curr = fit(n,d)
    if where == 'N':
        m = n+1
    elif where == 'S':
        m = n-1
        if fit(m,d) < curr:
            return m

    if where == 'E':
        e = d+1
    elif where == 'W':
        e = d-1
        if fit(n,e) < curr:
            return e

def oneRound(n,d):
    n *= 10
    d *= 10
    best = fit(n,d)
    while True:    
        improved = False
        for w in 'NSEW':
            r = test(n,d,where=w)
            if r:
                improved = True
                if w in 'NS':
                    n = r
                else:
                    d = r
                best = fit(n,d)
                print(w,n,d)
        if not improved:
            break
    return n,d

for i in range(1,15):
    n,d = oneRound(n,d)
    print (i, (n*1.0/d)**2, fit(n,d))


