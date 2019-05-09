import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
#Diffusion gradient #constant  Aluminum
k = 205.0
pc = ((2.7*(10**3)) * 900)
def H(k, pc, dt, dx):
    return (k*dt) / (pc*(dx**2))


xSize = 25

xf = np.linspace(0, 5, xSize +1)   # mesh points in space

iFn= lambda x : np.sin(x) * np.sin(((np.pi)/5.) * x)
iFn2 = lambda x : np.sin(x) * np.sin(((2. * np.pi)/5.) * x)

beta1 = (2./5.) * scipy.integrate.quad(iFn, 0, 5)[0]
print("Beta1: " + str(beta1))
beta2 = (2./5.) * scipy.integrate.quad(iFn2, 0, 5)[0]
print("Beta2: " + str(beta1))

sin1 = np.sin((np.pi/5.) * xf) * np.exp(-(k/pc)**2 * (np.pi**2.) * (1**2) * (3./(5**2)))
print("Sin1: " + str(sin1))
sin2 = np.sin(((2. * np.pi)/5.) * xf) * np.exp(-(k/pc)**2 * (np.pi**2.) * (2**2) * (3./(5**2)))
print("Sin2: " + str(sin2))
term1 = beta1 * sin1
print("Term1: " + str(term1))
term2 = beta2 * sin2
print("Term2: " + str(term2))
answer = term1 + term2;
print("Answer" + str(answer))



def simple(I, a, L, Nx, F, T, iter):
    x = np.linspace(0, L, Nx+1)   # mesh points in space
    dx = x[1] - x[0]
    dt = (F*dx**2/a) * (2.**-iter)
    F = F * (dt/ (dx**2))
    Nt = int(round(T/float(dt)))
    t = np.linspace(0, T, Nt+1)   # mesh points in time
    u   = np.zeros(Nx+1)
    u_1 = np.zeros(Nx+1)

    def tVal (x):
        return (T / Nt) * x

    print("Delta X: " + str(dx))
    print("Delta T: " + str(dt))
    print("F_or_H: " + str(F))
    print("Size of Time Array " + str(len(t)))

    # Set initial condition u(x,0) = I(x)
    for i in range(0, Nx+1):
        u_1[i] = I(x[i])

    for n in range(0, Nt):
        # Compute u at inner mesh points
        for i in range(1, Nx):
            u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1]) + ((dt/pc) * 3 * np.exp(-2*tVal(n)))

        # Insert boundary conditions
        u[0] = 0;  u[Nx] = 0

        # Switch variables before next step
        u_1, u = u, u_1
        u_1, u = u, u_1

    return u, x, t,

approx = []
for i in range(1,10):
    res = simple(np.sin, 0.001, np.pi*2, xSize, k/pc, 3, i)
    approx.append(res[0])

norm = []
for a in range(0, len(approx) -1):
    n = np.linalg.norm(approx[a] - approx[a+1])
    norm.append(n)
#    print("Norm: " + str(n));
    if a !=0:
        print("Ratio: " + str(norm[a-1] / n))


#simple(I, a, L, Nx, F, T):
# Plot the points
plt.plot(approx[0])
plt.show()
