import numpy as np
import matplotlib.pyplot as plt
import guass as g
import jacobi as jb
import seidal as sd
import re

def fx(x):
    A = np.pi**2. * np.sin(np.pi * x)
    return A

def ux(x):
    A = np.sin(np.pi * x)
    return A

# Number of interior pts
sizes = [25, 50, 75, 100, 150, 200]
last_norm = 0.
m_iter = 0

for s in sizes:
    size = s
    x = np.linspace(0, 1., size+2 )
    deltax = x[1]
    # Setup Empty Matrices
    A = np.zeros((size,size))
    # Fill the A array
    it_count = 0
    for xv in range(0, size): # iterate over the diagonals
        A[xv,xv] = -2.
        if it_count != 0:
            A[xv,xv-1] = 1.
        if it_count != size-1:
            A[xv,xv+1] = 1.

        it_count += 1

    # Fill the b array
    b = - deltax**2. * fx(x[1:size+1])

    ans2 = sd.seidal(A, b, 10.**-50)[0]
    ans2 = ans2.reshape((len(b)))
    real_ans = ux(x)
    #Fix boundary conditions aligns graph
    ans2 = np.insert(ans2, 0, 0.)
    ans2 = np.append(ans2, 0.)


    norm = (1. / np.sqrt(size)) * np.linalg.norm(ans2 - real_ans)

    if m_iter > 0:
        print("Ratio of L2 Norms: " + str(abs(last_norm / norm)))
    last_norm = norm
    m_iter += 1
