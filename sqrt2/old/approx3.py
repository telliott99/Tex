# best rational approximation to a global target
t = 2**0.5

def fit(n,d):
    r = abs((1.0*n)/d - t)
    return r

n = 5
d = 4
current = (n,d)

def one_round():
    n,d = current
    n = n*10
    d = d*10
    
    while True:
        good  = fit(n,d)
        north = fit(n+1,d)
        south = fit(n-1,d)
        east  = fit(n,d+1)
        west  = fit(n,d-1)
        arr = [good,north,south,east,west]
        best = min(arr)
        
        if   best == good:      break
        elif best == north:   n += 1
        elif best == south:   n -= 1
        elif best == east:    d += 1
        else:                 d -= 1
    return (n,d)

for k in range(15):
    n,d = one_round()
    print(k,n,d)
    current = (n,d)


