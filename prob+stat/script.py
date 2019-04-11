import random
import numpy as np
import matplotlib.pyplot as plt
random.seed(153)
N = 50

X = [10*random.random() for i in range(N)]
Y = [random.random() for i in range(N)]
X = [x - np.mean(X) for x in X]
Y = [y - np.mean(Y) for y in Y]

M = np.matrix([X,Y])
plt.scatter(M[0],M[1],s=200,
    marker='o', color='0.8')
plt.axes().set_aspect('equal')

s = np.sqrt(3)/2.0
R = [[0.5,-s],[s,0.5]]
M = R * M
plt.scatter(M[0],M[1],s=100,color='salmon')

A = M * M.transpose()
D,E = np.linalg.eig(A)
# evecs in increasing order of evals
# so switch the two columns
E = E[:,(1,0)]

M = E * M
# PCA may flip pos and negative, and did so here
M[0] = -M[0]
plt.scatter(M[0],M[1],s=50,color='black')
plt.savefig('example.png')
