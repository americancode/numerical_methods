import numpy as np
import matplotlib.pyplot as plt
#Diffusion gradient
k = 205.0
#constant  Aluminum
pc = ((2.7*(10**3)) * 900)

def H(k, pc, dt, dx):
    return (k*dt) / (pc*(dx**2))

def simple(I, a, L, Nx, F, T):

    import time
    t0 = time.process_time()

    x = np.linspace(0, L, Nx+1)   # mesh points in space
    dx = x[1] - x[0]
    dt = F*dx**2/a
    Nt = int(round(T/float(dt)))
    t = np.linspace(0, T, Nt+1)   # mesh points in time
    u   = np.zeros(Nx+1)
    u_1 = np.zeros(Nx+1)

    print("Delta X: " + str(dx))
    print("Delta T: " + str(dt))
    print("F_or_H: " + str(F))

    # Set initial condition u(x,0) = I(x)
    for i in range(0, Nx+1):
        u_1[i] = I(x[i])

    for n in range(0, Nt):
        # Compute u at inner mesh points
        for i in range(1, Nx):
            u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])

        # Insert boundary conditions
        u[0] = 0;  u[Nx] = 0

        # Switch variables before next step
        u_1, u = u, u_1

    t1 = time.process_time()
    return u, x, t, t1-t0



#simple(I, a, L, Nx, F, T):
res = simple(np.sin, 0.2, np.pi*2, 50, k/pc, 3)
res2 = simple(np.sin, 0.2, np.pi*2, 50, k/pc, 0.01)

# Plot the points
plt.plot(res2[0])
plt.plot(res[0])
plt.show()
