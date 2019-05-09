import numpy as np
import scipy.integrate
from integrals import simpson, midpoint, trapezoid

def f(x):
    return np.exp(-(float(x)**2)/2)

T = 5 #seconds
t = np.linspace(0, 5, 11)
v = [0, 7.51, 8.1, 8.93, 9.32, 9.76, 10.22, 10.56, 11.01, 11.22, 11.22]

def f(x):
    index = int(round(2 * x))
    print("x is: " + str(x))
    print("The index is:  " + str(index) + "   " + str(v[index]))
    return v[index]

ans = trapezoid(f, 0, 5, 10)
print("Trapezoid")
print("The area under the curve is approximately:  " + str(ans))



# import numpy as np
# import scipy.integrate
# from integrals import simpson, midpoint, trapezoid
#
# T = 5 #seconds
# t = np.linspace(0, 5, 11)
# v = [0, 7.51, 8.1, 8.93, 9.32, 9.76, 10.22, 10.56, 11.01, 11.22, 11.22]
#
# def valu(x):
#     return 2 * x
#
# def trapez(data, a, b, n):
#     n = int(n)
#     h = 0.5
#     s = (data[valu(a)] + data[valu(b)]) / 2
#
#     for k in range(1, int(n)):
#         s += data[int(valu(a + k * h))]
#     return s*h
#
# ans = trapez(v, 0, 5, 10)
# print("Trapezoid")
# print("The area under the curve is approximately:  " + str(ans))
