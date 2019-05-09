import numpy as np

def jacobi(A, b, N):
    D = np.diag(A)
    n = A.shape[0]
    A_D = A - np.diag(D)
    x = np.zeros(n)
    s = np.zeros([n,1])
    norm = 500000
    iterations = 0

    while norm > N:
        x = (b - A_D.dot(x)) / D
        if iterations > 0:
             norm = np.linalg.norm(x - last, np.inf)
        last = x
        iterations += 1
    s[:, 0] = x
    return (s, iterations)
