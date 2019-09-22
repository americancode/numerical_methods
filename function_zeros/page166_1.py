import numpy as np
import matplotlib.pyplot as plt
import newton_iterations

# Starting Function
f1 = lambda x: (3 * x ** 3) - (5 * x ** 2) - (4 * x) + 4
df1 = lambda x: (9 * x ** 2) - (10 * x) - 4

ans = newton_iterations(f1, df1, 0.7, 4, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
