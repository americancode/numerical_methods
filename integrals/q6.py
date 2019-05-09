import numpy as np
import scipy.integrate
from integrals import simpson, midpoint, trapezoid

def f(x):
    return np.exp(-(float(x)**2)/2)

s=0
e=2

ans = 1/2.0 + 1/ np.sqrt(2 * np.pi) * scipy.integrate.quad(f, s, e)[0]
print("Answer:  " + str(ans))

ns = [10]

print("   n:      trapezoid:    midpoint:     simpson:      E(t):         E(m):         E(s):")

for n in ns:
    trap = 1/2.0 + 1/ np.sqrt(2 * np.pi) * trapezoid(f, s, e, n)
    mid = 1/2.0 + 1/ np.sqrt(2 * np.pi) * midpoint(f, s, e, n)
    simp = 1/2.0 + 1/ np.sqrt(2 * np.pi) * simpson(f, s, e, n)
    abst = abs(ans - trap)
    absm = abs(ans - mid)
    abss = abs(ans - simp)
    print('%05s      %.6f      %.6f      %.6f      %.6f      %.6f      %.6f' % (str(n), trap, mid, simp , abst, absm, abss))
