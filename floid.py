from math import inf
from itertools import product
import math
n=4

def floyd(C,T,H):
    for i in range (n):
        for j in range (n):
            T[i][j] = C[i][j]
            if C[i][j] == 99:
                H[i][j]=0        
            elif C[i][j] != 99  and C[i][j] != 0: 
               H[i][j]=j 
    print (H)
    for i in range (n):
        for j in range (n):
            for k in range(n):
                if (i!=j and T[i][j]!=99 and i != k and T[i][k] != 99 and (T[j][k] == 99 or T[j][k] > T[j][i] + T[i][k])):
                    H[j][k] = H[j][i]
                    T[j][k] = T[j][i]+T[i][k]
    for i in range (n):
        if T[j][j] < 0:
            break
    print ("\n")
    print (T)

if __name__ == '__main__':
    import numpy as np
    M = np.random.randint(0,2,(n,n))
    np.fill_diagonal(M, 0)
    C = np.tril(M) + np.tril(M,-1).T
    print (C)
    print ("\n")
    for i in range(len(C)):
        for j in range (len(C[i])):
            if (C[i][j] == 1):
                C[i][j] = np.random.randint(1,9)
    for i in range(len(C)):
        for j in range (len(C[i])):
            if (C[i][j] == 0 and i!=j):
                C[i][j] = 99
    T = np.tril(C) + np.tril(C,-1).T
    print (T)
    print ("\n")
    H=[[]]
    H=np.diag(np.arange(1,n+1))
    floyd(C,T,H)
