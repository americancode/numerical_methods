import numpy as np
import matplotlib.pyplot as plt
from solvers import fixedPoint_iterations, fixedPoint

f1 = lambda x: 5./3. + (4./3. * x) - (4/3. * x**2.)
f2 = lambda x: 1 + ((3. * x**3  - 5. * x**2.) / 4.)
tolerance = 10. ** - 6

# Target first solution
print("Function i")
ans = fixedPoint(f1, 0.7, tolerance, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))

# Target second solution
print("Function ii")
ans = fixedPoint_iterations(f2, 0.7, 5, details = True)
print("Answer: " + str(ans[0]))
print("Number of iterations: " + str(ans[1]))
