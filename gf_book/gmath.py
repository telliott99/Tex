modD = { 3:11, 4:25, 5:37, 8:283 }
genD = { 3:3  , 4:2, 5:2, 8:3 }

def multiplier(exp=8,mod=283):
    # multiply is a closure, "knows" mod
    def multiply(a,b):
        def nspaces(n):
            b = len(bin(mod))
            return len(bin(n)) - b   

        def modulus(n,exp,mod):
            #print "modulus", n, exp, nspaces(n)
            while True:
                if n < 2**exp:
                    return n
                n = n ^ (mod << nspaces(n))
                
        # binary string, reversed
        s = bin(b)[2:][::-1]
        n = 0
        for c in s:
            if c == '1':
                n = n ^ a
            a = a << 1
        return modulus(n,exp,mod)
        
    return multiply

def xor_reduce(L):
    r = 0
    for n in L:
        r = r ^ n
    return r

def make_powers(generator,f,exp):
    p = generator
    n = 1
    pL = list()
    for i in range(2**exp):
        pL.append(n)
        n = f(n,p)
    return pL

def fmt_table(L,exp,rep='int'): 
    N = 8
    if exp >= 8:
        N = 16
    L2 = L[:]
    pL = list()
    while L2:
        sL = L2[:N]
        L2 = L2[N:]
        if rep == 'int':
            s = ' '.join([str(i).rjust(3) for i in sL])
        else:
            s = ' '.join([hex(i)[2:].zfill(2) for i in sL])
        pL.append(s)
    return '\n'.join(pL)

def main():
    import sys
    exp = int(sys.argv[1])
    poly = modD[exp]
    gen  = genD[exp]
    f = multiplier(exp=exp,mod=poly)
    L = make_powers(gen,f,exp)
    print(fmt_table(L,exp,rep='int'))

if __name__ == "__main__":
    main()