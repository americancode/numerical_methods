import numpy as np
import matplotlib.pyplot as plt
from inter import cspline, divdiff, lagrangec

# Write down the Lagrange interpolation polynomial using the nodes 0.0, 0.1, and 0.2, and then using 0.3 as well.
# Estimate the value of sin 0.26 using each of these polynomials.
def eval_poly(x, coe):
    y_pred =0
    for i in range(0, len(coe)):
        if i == 0:
            y_pred = coe[i] + y_pred
        else:
            y_pred = coe[i] * (x ** i) + y_pred
    return y_pred


f1 = lambda x: np.sin(x)

xValues = np.array([-1,0,1,2,3])
yValues = np.array([3,-4,5,-6,7])
# coes = lagrangec(xValues, yValues)
# approximation = eval_poly(0.26, coes)
# print("X Data")
# print(xValues)
# print("Y Data")
# print(yValues)
# print("Coefficients")
# print(coes)
# print("sin(0.26) = " + str(np.sin(0.26)))
# print("Approximation using coefficients: " + str(approximation))
# print("Absolute error: " + str(abs(approximation - np.sin(0.26))))

ans = divdiff(xValues, yValues, np.array([2,3]))[1]
print(ans)
