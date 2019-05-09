import numpy as np
from integrals import simpson, midpoint, trapezoid

ans = np.log(5)
ns = 2.**np.arange(0,6)

def oneOverX(x): return 1/x

print("   n:    trapezoid:  midpoint:   simpson:    E(t):       E(m):       E(s):")

for n in ns:
    trap = trapezoid(oneOverX, 1, 5, n)
    mid = midpoint(oneOverX, 1, 5, n)
    simp = simpson(oneOverX, 1, 5, n)
    abst = abs(ans - trap)
    absm = abs(ans - mid)
    abss = abs(ans - simp)
    print('%05s    %.6f    %.6f    %.6f    %.6f    %.6f    %.6f' % (str(n), trap, mid, simp , abst, absm, abss))
    #print(str(n) + "        " + str(trap) + "        " + str(mid) + "        " + str(simp))
