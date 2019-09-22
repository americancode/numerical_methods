import numpy as np
import matplotlib.pyplot as plt
from solvers import newton

# Starting Function
# 2 solutions between -.3 and .3
# one at approximately 9

f1 = lambda x: np.exp(x) - 100 * x ** 2
df1 = lambda x: np.exp(x) - 200 * x
tolerance = 10 ** -10

# Target first solution
ans = newton(f1, df1, -0.3, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
# Target second solution
ans = newton(f1, df1, 0.3, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
# Target third solution
ans = newton(f1, df1, 10, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
