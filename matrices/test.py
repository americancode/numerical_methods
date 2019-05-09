import numpy as np
import guass as g
import jacobi as jb

A = np.array([[6.,3.,2.,],[2.,5.,1.],[1.,1.,4.]])
b =  np.array([26.,17.,9.])

print("Starting Matrices")
print(A)
print(b)



print("With Jacobi")
ans = jb.jacobi(A, b, 10.**-6)
print(ans)
