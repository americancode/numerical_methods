import numpy as np
from functools import reduce
import operator

def eval_poly(coe, xv):
    y_pred = np.zeros(len(xv))
    for i in range(0, len(coe)):
        if i == 0:
            y_pred = coe[i] + y_pred
        else:
            y_pred = coe[i] * (xv ** i) + y_pred
    return y_pred


def cspline(knots, data, x):

    N = np.size(knots) -1
    P = np.size(x)
    h = np.diff(knots)
    D = np.diff(data) / h
    dD3 = 3 * np.diff(D)
    a = data[:N]

    H = (np.diag(2 * (h[:-1] + h[1:])) + np.diag(h[1:-1],1) + np.diag(h[1:-1],-1))
    c = np.zeros(N+1)
    c[1:N] = np.linalg.solve(H, dD3)
    b = D - h * (c[1:] + 2 * c[:-1]) / 3
    d = (c[1:] - c[:-1]) / (3*h)

    s = np.empty(P)
    for i in range(P):
        indices = np.argwhere(x[i] > knots)
        if indices.size > 0:
            k = indices.flat[-1]
        elif x[i] == knots[0]:
            k = 0
        else:
            raise ValueError('cspline does not support extrapolation')

        z = x[i] - knots[k]
        s[i] = a[k] + z * (b[k] + z * (c[k] + z * d[k]))
    return s


def divdiff(xdat , ydat , x) :
    N = x.size
    M = xdat.size
    D = np.zeros((M, M))
    y = np.zeros(N)
    for k in range(N):
        # Sort contents of input data arrays
        xtst = x[k]
        ind = np.argsort(np.abs(xtst - xdat))
        xsort = xdat[ind]
        D[:,0] = ydat[ind]
        # Begin divided differences
        for j in range(M):
            for i in range(M-j-1):
                D[i, j+1] = ((D[i+1, j] - D[i,j]) / (xsort[i+j+1] - xsort[i]))
        # End divided differences # Compute interpolation
        xdiff = xtst - xsort
        prod = 1 # Holds the product of xdiff
        for i in range(M):
            y[k] = y[k] + prod * D[0,i]
            prod = prod * xdiff[i]

    return y , np.flip(D, axis = 0)

def lagrange(x, x_values, y_values):
    #Number of data points
    n = len(x_values)
    #Number of x points
    nx = 1

    #Raname x, y data points
    dx = x_values
    dy = y_values

    a=0

    def b(j,xi):
        """Calculate b_j(x_xi)"""
        v = 1.0
        for k in range(n):
            if k != j:
                v *= (xi-dx[k]) / (dx[j]-dx[k])
        return v

    #Construct each element of L(x)
    for j in range(n):
        a += dy[j]*b(j,x)

    return a


def lagrangec(xdata, ydata):
    coes = np.zeros(len(xdata))
    n = len(xdata)

    def bottom(j):
        b = 1.0
        for k in range(n):
            if k != j:
                #print("x: " + str(xdata[j]) + " -x :" + str(xdata[k]))
                b *= (xdata[j]-xdata[k])
        return b

    def top(j):
        temp_coes = np.zeros_like(coes)
        first = True
        for k in range(n):
            if k != j:
                if first == True:
                    first = False
                    temp_coes[len(temp_coes) - 2] = 1.
                    temp_coes[len(temp_coes) - 1] = - xdata[k]
                    # print("Foil")
                    # print(temp_coes)
                else:
                    # Shift mult by x
                    p_coes = y = np.roll(temp_coes,-1)
                    # Multipy for right term
                    m_coes = temp_coes * - xdata[k]
                    # add
                    temp_coes = p_coes + m_coes
        # print("Temp Coes")
        # print(temp_coes)
        return np.flip(temp_coes)

    #Construct each element of L(x)
    for j in range(len(xdata)):
        topp = top(j)
        b = bottom(j)
        # print("Y is: " + str(ydata[j]))
        # print("Bottom is: " + str(b))
        multiplier = ydata[j] / b
        topp = topp * multiplier

        if j == 0:
            coes = topp
        else:
            coes = coes + topp

    return coes
