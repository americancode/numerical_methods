
import numpy as np
import matplotlib.pyplot as plt
from inter import divdiff, lagrangec, eval_poly


f1 = lambda x: np.cos(x)

xValues = np.linspace(0, 0.8, 9)
yValues = f1(xValues)

gxValues = np.linspace(0, 0.8, 1000)
gyValues = f1(gxValues)

x = np.array([0.17, 0.45, 0.63])
ans1 = divdiff(xValues, yValues, x)
app = ans1[0]

print("cos(0.17) = " + str(np.cos(0.17)))
print("ddiff approximation = " + str(app[0]))
print("absolute error: " + str(abs(app[0] - np.cos(0.17))))

print("cos(0.45) = " + str(np.cos(0.45)))
print("ddiff approximation = " + str(app[1]))
print("absolute error: " + str(abs(app[1] - np.cos(0.45))))

print("cos(0.63) = " + str(np.cos(0.63)))
print("ddiff approximation = " + str(app[2]))
print("absolute error: " + str(abs(app[2] - np.cos(0.63))))

ans = divdiff(xValues, yValues, gxValues)
coes = lagrangec(xValues, yValues)
print("Coefficients")
print(coes)

print("Divided Difference Table")
print(ans[1])


# Graph the knots and the interpolating values
plt.plot(xValues, yValues, 'k*', gxValues, eval_poly(coes, gxValues), '--', x, app, 'ks')
# graph real function
plt.plot(gxValues, gyValues, 'k')
plt.show()
