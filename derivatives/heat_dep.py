import numpy as np
import matplotlib.pyplot as plt

size = 500
tSize = 10000
ans = np.zeros(shape=(tSize,size))

#Start interval
start = 0
#End interval
length = 5
#Time in some units
tLength = 3
#Diffusion gradient
K = 205.0
#constant  Aluminum
pc = ((2.7*(10**3)) * 900)

#the function
def u0(x):
    return np.sin(x)

#deltaX change in time
dT = ( tLength / tSize )
#deltaT change in space
dX = ( (length - start) / (size - 1) )

def T (x):
    return ( tLength / tSize ) * x

def X (x):
    return ((length - start) / (size - 1)) * x

# Seed the table with the first row of data or u(x, T=0) == u0(x)
for val in range(0, size):
    #print("iter " + str(val) + " sin(" + str(X(val)) + ") =  " + str(u0(X(val))) )
    ans[0,val] = u0(X(val))

print(ans)
def H(k, pc, dt, dx):
    return (k*dt) / (pc*(dx**2))

# Print information on the parameters
print("Delta X: " + str(dX))
print("Delta T: " + str(dT))
print("H: " + str(H(K, pc, dT, dX)))
test = 1 - (2 * H(K, pc, dT, dX))
print("Test: " + str(test))

for k in range(0, tSize-1):
    for i in range(1, size-1):
        value = (H(K, pc, dT, dX) * ans[k, i-1])
        - (((2 * H(K, pc, dT, dX)) -1) * ans[k, i])
        + (H(K, pc, dT, dX) * ans[k, i+1]) + (2 * np.exp(-2*T(k)))

        ans[k+1,i] = value


# Plot the points
plt.ylabel('Heat')
plt.xlabel('Space')
plt.plot(ans[0], label="T=0")
plt.plot(ans[1], label="T=dt*1")
plt.plot(ans[tSize-1], label="T=3")
plt.show()
