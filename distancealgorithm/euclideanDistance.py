import math
import numpy as np

def eculid(A,B):
    return math.sqrt(sum([(a - b) **2 for (a,b) in zip(A,B)]))

def npeculid(A,B):
    return np.sqrt(sum(np.power((A-B),2)))

A = [1,2,3,4]
B = [0,1,2,3]
print(eculid(A,B))
X = np.array(A)
Y = np.array(B)
print(npeculid(X,Y))