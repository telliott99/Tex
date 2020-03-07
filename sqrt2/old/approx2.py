# best rational approximation to a target
def fit(n,d):
    return abs(n/d - t)

t = 2**0.5
n = 5
d = 4
best = [n,d,fit(n,d)]

def one_round(best):
    n,d,g = best
    count = 0
    N = n*10
    D = d*10
    
    for i in range(N-15,N+15):
        for j in range(D-15,D+15):
            count += 1
            f = fit(i,j)
            if f <= g:
                n,d,g = i,j,f
    best = [n,d,g]
    return best

for k in range(8):
    L = one_round(best)
    print(k, L)
    best = L

                
    
    
    