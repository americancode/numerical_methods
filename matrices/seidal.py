import numpy as np
import guass as g
import jacobi as jb
import re

def seidal(A, b, N):
    x = np.zeros_like(b)
    norm = 500000
    iterations = 0

    while norm > N:
        x_new = np.zeros_like(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, rtol=1e-8):
            break
        if iterations > 0:
             norm = np.linalg.norm(x - x_new, np.inf)
        iterations += 1
        x = x_new

    return (x.reshape((len(b),1)), iterations)
