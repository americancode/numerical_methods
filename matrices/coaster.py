import numpy as np
import matplotlib.pyplot as plt
from guass import GEPP, GENP



A = np.array(
[
[0.,0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,0.],
[1000.,100.,10.,1.,0.,0.,0.,0.,-100.,-10.,-1.,0.],

[0.,0.,0.,0.,90.**3,90.**2,90.,1.,-(90.**2),-90.,-1.,0.],
[0.,0.,0.,0.,1000000.,10000.,100.,1.,0.,0.,0.,-1.],

[0.,0.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[300.,20.,1.,0.,0.,0.,0.,0.,-20.,-1.,0.,0.],

[0.,0.,0.,0.,24300.,180.,1.,0.,-180.,-1.,0.,0.],
[0.,0.,0.,0.,30000.,200.,1.,0.,0.,0.,0.,0.],

[0.,2.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.],
[60.,2.,0.,0.,0.,0.,0.,0.,-2.,0.,0.,0.],

[0.,0.,0.,0.,540.,2.,0.,0.,-2.,0.,0.,0.],
[0.,0.,0.,0.,600.,2.,0.,0.,0.,0.,0.,0.],

]
)
b =  np.array([[0.],[0.],[0.],[-160.],[0.8],[0.],[0.],[-1.6],[0.],[0.],[0.],[0.]])

print(str(len(A)))
print("With Partial Pivoting")
ans = GEPP(A,b)
print("Answer with Pivoting")
print(ans)

tans = np.linalg.solve(A, b)

print("Real Answer")
print(tans)

def f1(x):
    return 0.8*x #left

def f2(x):
    return ans[0]*(x**3) + ans[1]*(x**2) + ans[2]*x + ans[3]

def f3(x):
    return ans[4]*(x**3) + ans[5]*(x**2) + ans[6]*x + ans[7]

def f4(x):
    return -1.6*x + ans[11] #right

def f5(x): #poly
    return ans[8]*(x**2) + ans[9]*x + ans[10]

values = []
for i in range(-10,0):
    values.append(f1(i))
for i in range(0,10):
    values.append(f2(i))
for i in range(10,90):
    values.append(f5(i))
for i in range(90,100):
    values.append(f3(i))
for i in range(100,150):
    values.append(f4(i))
xvals = np.arange(-10,150)

plt.plot(xvals,values)
plt.show()
