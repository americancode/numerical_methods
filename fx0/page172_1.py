import numpy as np
import matplotlib.pyplot as plt
from solvers import secant_iterations

# Starting Function
f1 = lambda x: (3 * x ** 3) - (5 * x ** 2) - (4 * x) + 4

ans = secant_iterations(f1, 0.7, 0.75, 4, details = True)

print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
