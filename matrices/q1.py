import numpy as np
import guass as g
import jacobi as jb

A = np.array([[1.,2.,3.,4.],[2.,2.,3.,4.],[3.,3.,3.,4.],[4.,4.,4.,4.]])
b =  np.array([[20.],[22.],[22.],[24.]])

print("Starting Matrices")
print(A)
print(b)

print("With No Pivoting")
ans = g.GENP(A, b)
print("Answer with no Pivoting")
print(ans)

print("With Partial Pivoting")
ans = g.GEPP(A,b)
print("Answer with Pivoting")
print(ans)


print("With Jacobi")
ans = jb.jacobi(A, b, 20)
print("Answer with Pivoting")
print(ans)
