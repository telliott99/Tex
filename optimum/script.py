from math import *

c = 0.93969 # cos 20 degrees
s = 0.34202 # sin 20 degrees

def f(x):
    hoz = 9 + x*c
    a_sq = hoz**2 + (35 - 4 - x*s)**2
    b_sq = hoz**2 + (4 + x*s - 10)**2
    
    a = sqrt(a_sq)
    b = sqrt(b_sq)
    num = a_sq + b_sq - 25**2
    den = 2 * a * b
    return num*1.0/den

for x in range(1,90):
    print str(x).rjust(2),
    cosine = f(x)
    print acos(cosine) * 360 /(2 * pi)
    
