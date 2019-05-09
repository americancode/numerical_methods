import numpy as np
import matplotlib.pyplot as plt
from solvers import fixedPoint

tolerance = 10. ** - 6
a = -10
b = 10

f1 = lambda x: np.exp(x / 2) / 10
f2 = lambda x: 2 * (np.log(x) + np.log(10))
f3 = lambda x: - np.exp(x / 2) / 10

# Target first solution
print("Function i")
ans = fixedPoint(f1, 0, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

print("Function ii")
ans = fixedPoint(f2, 10, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

print("Function iii")
ans = fixedPoint(f3, -2, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
