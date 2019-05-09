import numpy as np
import matplotlib.pyplot as plt
import guass as g
import jacobi as jb
import seidal as sd
import re

# Number of interior pts
size = 25

x = np.linspace(0, 1., size+2 )

deltax = x[1]
print("Delta x is: " + str(deltax))

def fx(x):
    A = np.pi**2. * np.sin(np.pi * x)
    return A

def ux(x):
    A = np.sin(np.pi * x)
    return A

# Setup Empty Matrices
A = np.zeros((size,size))

# Fill the A array
it_count =0
for xv in range(0, size): # Iterate over the diagonals
    A[xv,xv] = -2.
    if it_count != 0:
        A[xv,xv-1] = 1.
    if it_count != size-1:
        A[xv,xv+1] = 1.

    it_count += 1


print(A)
# Fill the b array
b = - deltax**2. * fx(x[1:size+1])
print("b matrix is: ")
print(b)

ans2 = sd.seidal(A, b, 10.**-50)[0]

real_ans = ux(x)
ans2 = ans2.reshape((len(b)))
#Fix boundary conditions aligns graph
ans2 = np.insert(ans2, 0, 0.)
ans2 = np.append(ans2, 0.)
print("Answer is: ")
print(ans2)

norm = (1. / np.sqrt(size)) * np.linalg.norm(ans2 - real_ans)
print("Scaled L2 norm is: " + str(norm));
plt.plot(x, ans2, "b--") # Approximation is dotted
plt.plot(x, real_ans)

plt.show()
