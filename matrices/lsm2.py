import numpy as np
import guass as g
import matplotlib.pyplot as plt

A = np.array([
[2., 0., 2./3., 0., 2./5.],
[0., 2./3., 0., 2./5., 0],
[2./3., 0., 2./5., 0, 2./7.],
[0., 2./5., 0, 2./7., 0],
[2./5., 0, 2./7., 0, 2./9]
])

b =  np.array([
[2. * np.sinh(1.)],
[2. * np.exp(-1.)],
[np.e-5. * np.exp(-1.)],
[16. * np.exp(-1.) - 2 * np.e],
[9 * np.e - 65 * np.exp(-1.)]
])

print("Starting Matrices")
print(A)
print(b)

print("With Partial Pivoting")
ans = g.GEPP(A,b)
print("Answer with Pivoting")
print(ans)


x = np.linspace(-1,1,1000)

y = ans[0,0] +  ans[1,0] * x  +  ans[2,0] * (x**2.) + ans[3,0] * (x**3.) + ans[4,0] * (x**4.)
y_real = np.exp(x)
error = []

for v in range(0, len(x)):
    error.append(abs(y[v]-y_real[v]));

norm = (np.linalg.norm(y - y_real))
print("L2 norm is: " + str(norm));

plt.plot(x,y, "b--")
plt.plot(x,y_real)
plt.show()

plt.plot(x,error)
plt.show()
