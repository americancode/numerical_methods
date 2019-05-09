import numpy as np

x0 = np.pi / 4
iter = 0
h = 10.**-np.arange(1,7)
df = (np.sin(x0 + h) - (2 * np.sin(x0)) + np.sin(x0 - h))/ (h**2)
error= []
relDiff = []
ans = -np.cos(x0);

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1


iter = 0
print("Second derivative 3 point formula with h = 10^-n")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1


iter = 0;
h = 10.**-np.arange(1,7)
df = (-np.sin(x0 + (2*h)) + (16 * np.sin(x0 + h)) - (30 * np.sin(x0)) + (16 * np.sin(x0 - h)) - np.sin(x0 - (2*h)))/ (12 * (h**2))
error= []
relDiff = []

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1


iter = 0
print("Second derivative 5 point formula with h = 10^-n")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1

iter = 0
h = 2.**-np.arange(1,10)
df = (np.sin(x0 + h) - (2 * np.sin(x0)) + np.sin(x0 - h))/ (h**2)
error= []
relDiff = []

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1


iter = 0
print("Second derivative 3 point formula with h = 2^-n")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1


iter = 0;
h = 2.**-np.arange(1,10)
df = (-np.sin(x0 + (2*h)) + (16 * np.sin(x0 + h)) - (30 * np.sin(x0)) + (16 * np.sin(x0 - h)) - np.sin(x0 - (2*h)))/ (12 * (h**2))
error= []
relDiff = []

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1


iter = 0
print("Second derivative 5 point formula with h = 2^-n")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1
