import numpy as np
import matplotlib.pyplot as plt
from solvers import bisection

# Starting Function
f1 = lambda x: (3 * x ** 3) - (5 * x ** 2) - (4 * x) + 4

xValues = np.linspace(0, 1, 1000)
yValues = f1(xValues)

tolerance =  10. ** -6.

ans = bisection(f1, 0, 1, tolerance, details = True)

print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

# Graphing
plt.ylabel('Y')
plt.xlabel("X")
plt.plot(xValues, yValues)
plt.plot(xValues, np.zeros(1000))
plt.show()
