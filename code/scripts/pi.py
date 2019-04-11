p = 4.0/(2**0.5)
P = 4

def one_round(t):
    p,P = t
    P2 = 2*p*P/(p+P)
    p2 = (p*P2)**0.5
    return p2,P2

s = '%3.10f  %3.10f'
print '%2d' % 1, s % (p,P)
for i in range(18):
    p,P = one_round((p,P))
    if not i%3:
        print '%2d' % (i+2), s % (p,P)
    