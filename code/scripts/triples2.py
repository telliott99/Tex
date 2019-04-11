import sys
from operator import itemgetter

# greatest common divisor
from fractions import gcd

# pre-computed triples
fh = open('triples.txt')
data = fh.read().strip().split('\n')
fh.close()
L = list()
for line in data:
    sL = line.strip().split()
    a,b,c = [int(s) for s in sL]
    L.append((a,b,c))

# Euclid's formula for triples
tL = list()
for m in range(1,15):
    for n in range(1,m):
        a = m**2-n**2
        b = 2*m*n
        c = m**2 + n**2
        if b < a:
             a,b = b,a
        tL.append(((n,m),(a,b,c)))

if len(sys.argv) > 1:
    tL.sort(key=itemgetter(1))
else:
    tL.sort()

# display     
for u,t in tL:
    s = '%3d ' * 5
    if gcd(t[0],t[1]) != 1:
        pass
    elif t in L:
        print s % (u + t)
    else:
        print s % (u + t) + ' not in list'

'''
> python triples2.py x
  1   2   3   4   5 
  2   3   5  12  13 
  3   4   7  24  25 
  1   4   8  15  17 
  4   5   9  40  41 
  5   6  11  60  61 
  1   6  12  35  37 
  6   7  13  84  85 
  7   8  15 112 113 
  1   8  16  63  65 
  8   9  17 144 145 
  9  10  19 180 181 
  2   5  20  21  29 
  1  10  20  99 101 
 10  11  21 220 221 
 11  12  23 264 265 
  1  12  24 143 145 
 12  13  25 312 313 
 13  14  27 364 365 
  2   7  28  45  53 
  1  14  28 195 197 
  4   7  33  56  65 
  2   9  36  77  85 
  5   8  39  80  89 
  2  11  44 117 125 
  3   8  48  55  73 
  7  10  51 140 149 
  2  13  52 165 173 
  8  11  57 176 185 
  3  10  60  91 109 
  4   9  65  72  97 
 10  13  69 260 269 
 11  14  75 308 317 
  3  14  84 187 205 
  6  11  85 132 157 
  4  11  88 105 137 
  7  12  95 168 193 
  4  13 104 153 185  not in list
  8  13 105 208 233  not in list
  9  14 115 252 277  not in list
  5  12 119 120 169  not in list
  6  13 133 156 205  not in list
  5  14 140 171 221  not in list
> 

> python triples2.py
  1   2   3   4   5 
  1   4   8  15  17 
  1   6  12  35  37 
  1   8  16  63  65 
  1  10  20  99 101 
  1  12  24 143 145 
  1  14  28 195 197 
  2   3   5  12  13 
  2   5  20  21  29 
  2   7  28  45  53 
  2   9  36  77  85 
  2  11  44 117 125 
  2  13  52 165 173 
  3   4   7  24  25 
  3   8  48  55  73 
  3  10  60  91 109 
  3  14  84 187 205 
  4   5   9  40  41 
  4   7  33  56  65 
  4   9  65  72  97 
  4  11  88 105 137 
  4  13 104 153 185  not in list
  5   6  11  60  61 
  5   8  39  80  89 
  5  12 119 120 169  not in list
  5  14 140 171 221  not in list
  6   7  13  84  85 
  6  11  85 132 157 
  6  13 133 156 205  not in list
  7   8  15 112 113 
  7  10  51 140 149 
  7  12  95 168 193 
  8   9  17 144 145 
  8  11  57 176 185 
  8  13 105 208 233  not in list
  9  10  19 180 181 
  9  14 115 252 277  not in list
 10  11  21 220 221 
 10  13  69 260 269 
 11  12  23 264 265 
 11  14  75 308 317 
 12  13  25 312 313 
 13  14  27 364 365 
> 

'''