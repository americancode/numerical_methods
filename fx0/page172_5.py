import numpy as np
import matplotlib.pyplot as plt
from solvers import secant

# Starting Function
f1 = lambda x: np.exp(x) - 100 * x ** 2

tolerance = 10 ** -10

# Target first solution
ans = secant(f1, -0.3, -0.31, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
# Target second solution
ans = secant(f1, 0.3, 0.31, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
# Target third solution
ans = secant(f1, 9.9, 10, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
