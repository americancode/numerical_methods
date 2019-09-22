import numpy as np
import matplotlib.pyplot as plt
from solvers import fixedPoint

f1 = lambda x: (np.exp(x) - 1.) / 3. # Not convergent
f2 = lambda x: np.log(3. * x + 1.)

tolerance = 10. ** - 6

xValues = np.linspace(1, 3, 1000)
yValues = f2(xValues)

# Target first solution
ans = fixedPoint(f2, 1, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

# Graphing
plt.ylabel('Y')
plt.xlabel("X")
plt.plot(xValues, yValues)
plt.plot(xValues, xValues)
plt.show()
