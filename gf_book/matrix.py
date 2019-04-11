# we show that 
# fM x fM x fM = rM
# fM x fM x fM x fM = I
# so
# fM x rM = I

from gmath import gmultiply as gm
from gmath import xor_reduce
from fmt import fmt_matrix, fmt_matrix_mul

def dot(L1,L2):
    rL = [gm(x,y) for x,y in zip(L1,L2)]
    return xor_reduce(rL)

fM = [[2,3,1,1],
      [1,2,3,1],
      [1,1,2,3],
      [3,1,1,2]]
      
rM = [[14,11,13, 9],
      [ 9,14,11,13],
      [13, 9,14,11],
      [11,13, 9,14]]
     
      
def matrix_mul(a,b):
    b = zip(*b)
    rL = list()
    for i in range(4):
        sL = list()
        for j in range(4):
            n = dot(a[i],b[j])
            sL.append(n)
        rL.append(sL)
    return rL
    
P = matrix_mul(fM,fM)
print(fmt_matrix_mul(
          fmt_matrix(fM),
          fmt_matrix(fM),
          fmt_matrix(P)))

'''
 2  3  1  1     2  3  1  1     5  0  4  0
 1  2  3  1     1  2  3  1     0  5  0  4
 1  1  2  3     1  1  2  3     4  0  5  0
 3  1  1  2     3  1  1  2     0  4  0  5
'''

P2 = matrix_mul(fM,P)
print(fmt_matrix_mul(
          fmt_matrix(fM),
          fmt_matrix(P),
          fmt_matrix(P2)))

'''
 2  3  1  1     5  0  4  0    14 11 13  9
 1  2  3  1     0  5  0  4     9 14 11 13
 1  1  2  3     4  0  5  0    13  9 14 11
 3  1  1  2     0  4  0  5    11 13  9 14
'''

I = matrix_mul(fM,P2)
print(fmt_matrix_mul(
          fmt_matrix(fM),
          fmt_matrix(P2),
          fmt_matrix(I)))

'''
 2  3  1  1    14 11 13  9     1  0  0  0
 1  2  3  1     9 14 11 13     0  1  0  0
 1  1  2  3    13  9 14 11     0  0  1  0
 3  1  1  2    11 13  9 14     0  0  0  1
'''

M = matrix_mul(fM,rM)
print(fmt_matrix_mul(M))

# fM * rM = I

'''
 1  0  0  0
 0  1  0  0
 0  0  1  0
 0  0  0  1
'''
