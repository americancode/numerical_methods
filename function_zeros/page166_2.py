import numpy as np
import matplotlib.pyplot as plt
from solvers import newton

tolerance = 10. ** - 12

f1 = lambda x: np.exp(x) - (3. * x) - 1.
df1 = lambda x: np.exp(x) - 3.

# Target first solution
ans = newton(f1, df1, 2, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

xValues = np.linspace(1, 3, 1000)
yValues = f1(xValues)

# Graphing
plt.ylabel('Y')
plt.xlabel("X")
plt.plot(xValues, yValues)
plt.plot(xValues, np.zeros(1000))
plt.show()
