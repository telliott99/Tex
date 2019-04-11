def divide(a,b):
    # binary string, reversed
    s = bin(b)[2:][::-1]
    n = 0
    for c in s:
        if c == '1':
            n = n ^ a
        a = a << 1
    return n

def test(exp,m):
    N = 2**exp
    for i in range(2,N):
        if divide(i,m) == 0:
            return False
    return True

def get(exp):
    N = 2**exp
    print exp, N
    for m in range(N,2*N):
        if test(exp,m):
            print m
            
get(8)

        
            
        
