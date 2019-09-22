import numpy as np
import matplotlib.pyplot as plt
from solvers import newton, bisection_e, fixedPoint
from poly_fit import pfit

tolerance = 10 ** - 4

f1 = lambda x: np.exp(x) - 100 * x ** 2 # Original Functions
df1 = lambda x: np.exp(x) - 200 * x # Original Function Derivative

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

def print_table(history, errors, alphas):
    print("Approximation       Error              Alphas/Convergence")
    for i in range(0, len(history)):
        if i == 0:
            print("{0:.15f}  -----------------  -----------------".format(history[i]))
        elif i == len(history)-1:
            print("{0:.15f}  {1:.15f}  -----------------".format(history[i], errors[i-1]))
        else:
            print("{0:.15f}  {1:.15f}  {2:.15f}".format(history[i], errors[i-1], alphas[i-1]))


## Bisection Method
print("Bisection Method For 3 Unique Solutions")
ans = bisection_e(f1, -0.3, 0, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n")

ans = bisection_e(f1, 0, 0.3, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n")

ans = bisection_e(f1, 8, 10, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n\n")




## Fixed Point Method
print("Fixed Point Method For 3 Unique Solutions")
fix1 = lambda x: np.exp(x / 2) / 10
fix2 = lambda x: 2 * (np.log(x) + np.log(10))
fix3 = lambda x: - np.exp(x / 2) / 10

ans = fixedPoint(fix3, -2, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n")

ans = fixedPoint(fix1, 0, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n")

ans = fixedPoint(fix2, 10, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n\n")




## Newtons Method
print("Newtons Method For 3 Unique Solutions")
ans = newton(f1, df1, -0.3, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n")

ans = newton(f1, df1, 0.3, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n")

ans = newton(f1, df1, 10, tolerance, details = False)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
ap = calcon(ans[2])
print_table(ans[2],ans[3], ap)
print("\n\n")
