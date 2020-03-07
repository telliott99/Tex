def f(n,d):
    return 1.0*n**2/d**2

def fit(n,d):
    return abs(2.0 - f(n,d))

def pp(best):
    n,d,g = best
    print(n, d)
    print(f(n,d))
    print(g)
    print('count', count)
    print()

best = (1,1,1000)

for i in range(1,5):
    top = 10**i + 1
    count = 0

    for n in range(2,top):
       for d in range(2,n):
           count += 1
           r = fit(n,d)
           if r < best[2]:
               best = (n,d,r)
    pp(best)