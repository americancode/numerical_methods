import numpy as np

def GENP(A, b):
    A = A.copy()
    b = b.copy()
    n =  A.shape[0] # the number of

    for i in range(n-1):
        # p = np.argmax(np.abs(A[i:,i]))
        # p += i
        # A[[i,p], :] = A[[p,i], :]
        # b[[i,p]] = b [[p,i]]
        for j in range(i+1, n):
            m = A[j,i] / A[i,i]
            A[j,i] = 0
            A[j, i+1:] -= m * A[i,i+1:]
            b[j] -= m * b[i]
    x = np.zeros_like(b)
    x[-1] = b[-1] / A[-1,-1]
    print(A)
    print(b)

    for i in range(n-1, -1, -1):
        for j in range(i+1,n):
            b[i] -= A[i,j] * x[j]
        x[i] = b[i] / A[i,i]
    return x


def GEPP(A, b):
    A = A.copy()
    b = b.copy()
    n =  A.shape[0]

    for i in range(n-1):
        p = np.argmax(np.abs(A[i:,i]))
        p += i
        A[[i,p], :] = A[[p,i], :]
        b[[i,p]] = b [[p,i]]
        for j in range(i+1, n):
            m = A[j,i] / A[i,i]
            A[j,i] = 0
            A[j, i+1:] -= m * A[i,i+1:]
            b[j] -= m * b[i]
    x = np.zeros_like(b)
    x[-1] = b[-1] / A[-1,-1]
    print(A)
    print(b)

    for i in range(n-1, -1, -1):
        for j in range(i+1,n):
            b[i] -= A[i,j] * x[j]
        x[i] = b[i] / A[i,i]
    return x

if __name__ == "__main__":
    A = np.array([[1.,-1.,1.,-1.],[1.,0.,0.,0.],[1.,1.,1.,1.],[1.,2.,4.,8.]])
    b =  np.array([[14.],[4.],[2.],[2.]])
    #print(GENP(np.copy(A), np.copy(b)))
    print(GEPP(A,b))
