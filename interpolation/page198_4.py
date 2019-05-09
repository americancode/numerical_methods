import numpy as np
import matplotlib.pyplot as plt
from inter import cspline, lagrange, lagrangec

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

def plot_poly(coe, a, b, n):
    # predicted response vector
    xv = np.linspace(a,b,n)
    y_pred = np.zeros(len(xv))
    for i in range(0, len(coe)):
        if i == 0:
            y_pred = coe[i] + y_pred
        else:
            y_pred = coe[i] * (xv ** i) + y_pred

    # plotting the regression line
    plt.plot(xv, y_pred, color = "g", )
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    # function to show plot
    plt.show()



f1 = lambda x: np.sin(x)

xValues = np.linspace(0, 0.3, 4)
yValues = f1(xValues)
coes = lagrangec(xValues, yValues)
approximation = eval_poly(0.26, coes)
print("X Data")
print(xValues)
print("Y Data")
print(yValues)
print("Coefficients")
print(coes)
print("sin(0.26) = " + str(np.sin(0.26)))
print("Approximation using coefficients: " + str(approximation))
print("Absolute error: " + str(abs(approximation - np.sin(0.26))))
