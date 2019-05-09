import numpy as np
import guass as g
import matplotlib.pyplot as plt

A = np.array([[np.pi, np.pi**2/2, np.pi**3/3, np.pi**4/4],
[np.pi**2/2, np.pi**3/3, np.pi**4/4, np.pi**5/5],
[np.pi**3/3, np.pi**4/4, np.pi**5/5, np.pi**6/6],
[np.pi**4/4, np.pi**5/5, np.pi**6/6, np.pi**7/7]])
b =  np.array([[2.],[np.pi],[np.pi**2-4],[np.pi * (np.pi**2-6)]])

print("Starting Matrices")
print(A)
print(b)

print("With Partial Pivoting")
ans = g.GEPP(A,b)
print("Answer with Pivoting")
print(ans)


x = np.linspace(0,np.pi,1000)

y = ans[0,0] +  ans[1,0] * x  +  ans[2,0] * (x**2.)
y2 = np.sin(x)
error = []

for v in range(0, len(x)):
    error.append(abs(y[v]-y2[v]));

plt.plot(x,y, "b--")
plt.plot(x,y2)
plt.show()

plt.plot(x,error)
plt.show()
