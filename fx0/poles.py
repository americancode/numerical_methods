import numpy as np
import matplotlib.pyplot as plt
from .solvers import bisection_e, newton, secant
from .poly_fit import pfit

f1 = lambda x: x * np.cosh(100/x) - x - 15.
df1 = lambda x: -( (100 * np.sinh(100/x))/ x) + np.cosh(100/x) -1
h = 100
xValues = np.linspace(330, 350, h)
yValues = f1(xValues)
tolerance = 10**-15


sign = 0
for i, val in enumerate(yValues):
    s = 0
    if val >= 0:
        s = 1
    if sign != s:
        print("Changed signs")
        print("x is: " + str(xValues[i]))
        sign = s



def calcon(history):
    alphas = []
    xs = []
    ys = []

    for i in range(1, len(history) - 1):
        alphas.append( np.log(abs(history[i+1] - history[i])) / np.log(abs(history[i] - history[i-1])) )
        ys.append(np.log(abs(history[i+1] - history[i])))
        xs.append(np.log(abs(history[i] - history[i-1])))

    alphas = np.asarray(alphas)
    xs = np.asarray(xs)
    ys = np.asarray(ys)

    coe = pfit(xs, ys, 1)
    print("Least Squares Linear Regression of Errors")
    print("y = " + str(coe[1]) + "x + " + str(coe[0]))
    return alphas

def print_table(history, errors):
    print("Approximation        Error")
    for i in range(0, len(history)):
        if i == 0:
            print("{0:.15f}  -----------------".format(history[i]))
        elif i == len(history)-1:
            print("{0:.15f}  {1:.15f}".format(history[i], errors[i-1]))
        else:
            print("{0:.15f}  {1:.15f}".format(history[i], errors[i-1]))

def simpson(fnc, a, b, n):
    n = int(n)
    h = (b-a) / n
    s = (fnc(a) + fnc(b))
    for k in range(1, int(n), 2):
        s += 4 * fnc(a + k * h)
    for k in range(2, n-1, 2):
        s += 2 * fnc(a + k * h)
    return s*h/3

## Bisection Method
print("Bisection Method For Unique Solution")
ans = bisection_e(f1, 335, 336, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
print_table(ans[2],ans[3])
print("\n")

## Secant Method
print("Secant Method For Unique Solution")
ans = secant(f1, 333, 333.2 , tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
print_table(ans[2],ans[3])
print("\n")

## Newtons Method
print("Newtons Method For Unique Solution")
ans = newton(f1, df1, 335, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
print_table(ans[2],ans[3])
print("\n")

h0 = 50 - (ans[0] * np.cosh(100/ans[0]))
print("H0 is: " + str(h0))

f2 = lambda x: 2 * np.sqrt(1 + (np.sinh(x / ans[0]) ** 2))
arclength = simpson(f2, 0,100,100000)
print("Using Simpson's rule we get arclength = " + str(arclength))
