import numpy as np
import matplotlib.pyplot as plt
from solvers import newton2d

# Starting arrays
gx = np.linspace(0, 5280, 25)
gy = np.array([0,20,49,83,115,140,150,135,112,88,63,39,16,-3,-18,-27,-30,-28,-25,-21,-15,-6,-7,26,50])
tolerance = 10**-3

# x  is lambda 
# f1 = lambda x, c, a, b: (x * np.cosh((b + c) / x)) - (x * np.cosh(c / x)) - gy[np.where(gx == b)] + gy[np.where(gx == a)]
# f2 = lambda x, c, a, b: (((x * np.cosh((b + c) / x)) + (x * np.cosh(c / x))) / 2) - x - 10
# df1x = lambda x, c, a, b: - (((b + c) * np.sinh((b+c)/x)) / x ) + np.cosh((b+c)/x) + ((c * np.sinh(c/x)) / x ) - np.cosh(c/x)
# df1c = lambda x, c, a, b: np.sinh((b + c) /x) - np.sinh(c / x)
# df2x = lambda x, c, a, b: 0.5 * (-((((b + c) * np.sinh((b+c)/x)) / x)) + np.cosh((b+c)/x) + ((c * np.sinh(c/x)) / x ) - np.cosh(c/x)) -1
# df2c = lambda x, c, a, b: (0.5 * ( np.sinh((b + c) /x)) + np.sinh(c / x))

f1 = lambda x, c, a, b: (x * np.cosh((b + c) / x)) - (x * np.cosh((a + c) / x)) - gy[np.where(gx == b)] + gy[np.where(gx == a)] # Good to go
f2 = lambda x, c, a, b: (((x * np.cosh((b + c) / x)) + (x * np.cosh((a + c) / x))) / 2) - x - 25

df1x = lambda x, c, a, b: - (((b + c) * np.sinh((b + c)/x)) / x ) + np.cosh((b + c)/x) + (( (a+c) * np.sinh((a+c)/x)) / x ) + np.cosh((a+c)/x)
df1c = lambda x, c, a, b: np.sinh((b + c) /x) - np.sinh((a + c) / x)

df2x = lambda x, c, a, b: 0.5 * ( -(( (b+c) * np.sinh((b+c)/x)) / x ) + np.cosh((b+c)/x) - (( (a+c) * np.sinh((a+c)/x)) / x ) + np.cosh((a+c)/x) - 2)
df2c = lambda x, c, a, b: 0.5 * (np.sinh((b + c) / x) + np.sinh((a + c) / x))


def eqs(v):
    x, c = v
    f = np.empty(2)
    f[0] = f1(x, c , A,  B)
    f[1] = f2(x, c , A,  B)
    return f

def dfs(v):
    x, c = v
    J = np.empty((2,2))
    J[0,0] = df1x(x, c , A,  B)
    J[0,1] = df1c(x, c , A,  B)
    J[1,0] = df2x(x, c , A,  B)
    J[1,1] = df2c(x, c , A,  B)
    return J


xs = np.empty(0)
ys = np.empty(0)

oldh =0 
for i in range(gx.size -1):
    A = gx[i]
    B = gx[i+1]
    ## Newtons Method
    print("Newtons Method For Unique Solution")
    xg = 600
    cg = 2 * (gy[np.where(gx == B)] - gy[np.where(gx == A)]) - 110
    ans = newton2d(eqs, dfs, np.array([xg, cg[0]]), tolerance)
    print(ans)
    # Find the H
    h = 25 + ((gy[np.where(gx == B)] + gy[np.where(gx == A)]) / 2) - (ans[0] * np.cosh((((A+B)/2) + ans[1]) / ans[0]))
    oldh = h
    # Graph on interval
    xVals = np.linspace(A, B, 100)
    yVals = h + (ans[0] * np.cosh((xVals + ans[1])/ans[0]))
    xs = np.concatenate((xs, xVals), axis=None)
    ys = np.concatenate((ys, yVals), axis=None)


# Graph the poles and ground
plt.plot(gx, gy, "k", xs, ys, "b")
plt.show()