import numpy as np
import matplotlib.pyplot as plt

iterations = 1000
ti =200 # Time
br = 0.06   # Birth rate
Pm = 20000  # Max fish in pond
hr = 0.05888   # Harvest rate
p0 = 5000   # initial fish at time 0
dt = ((ti - 0) / (iterations - 1))
time = np.zeros(iterations)


# df = (np.sqrt(x0 + h) - np.sqrt(x0))/h
time[0] = p0
print("Delta t is: " + str(dt))


for t in range(0, len(time)-1):
    val = ((dt * br * (1 - (time[t] / Pm))) * time[t]) - (dt * hr * time[t]) + time[t]
    time[t+1] = val


plt.ylabel('Fish')
plt.xlabel(str(iterations) + ' iterations, dt=' + str(dt) + ' at ' + str(iterations) + ' t,tim=' + str(ti))
plt.plot(time)
plt.show()
