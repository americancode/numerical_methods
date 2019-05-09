import numpy as np
import matplotlib.pyplot as plt
from solvers import bisection

# Starting Function
# 2 solutions between -.3 and .3
# one at approximately 9

f1 = lambda x: np.exp(x) - 100 * x ** 2
h = 1000
xValues = np.linspace(-10, 10, h)
yValues = f1(xValues)
tolerance = 0.1


sign = 0
for i, val in enumerate(yValues):
    s = 0
    if val >= 0:
        s = 1
    if sign != s:
        print("Changed signs")
        print("x is: " + str(xValues[i]))
        sign = s


# Target first solution
ans = bisection(f1, -0.3, 0, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
# Target second solution
ans = bisection(f1, 0, 0.3, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
# Target third solution
ans = bisection(f1, 8, 10, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

# Graphing
plt.ylabel('Y')
plt.xlabel("X")
plt.plot(xValues, yValues)
plt.plot(xValues, np.zeros(h))
plt.show()
