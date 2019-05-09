import numpy as np
import matplotlib.pyplot as plt
from inter import cspline, lagrangec, eval_poly

f1 = lambda x: np.sqrt(x) * np.exp(-x)

xValues = np.linspace(0, 8, 9)
gxValues = np.linspace(0, 8, 1000)

print(xValues)
gyValues = f1(gxValues)
yValues = f1(xValues)

ans = cspline(xValues, yValues, gxValues)
print(ans)

plt.plot(gxValues, gyValues, 'k')
plt.plot(xValues, yValues, 'k*', gxValues, ans, 'k--')
plt.show()
