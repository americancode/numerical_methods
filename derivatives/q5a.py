import numpy as np

x0 = 4.0
iter = 0;
h = 10.**-np.arange(1,7)
df = (np.sqrt(x0 + h) - (2 * np.sqrt(x0)) + np.sqrt(x0 - h))/ (h**2)
error= []
relDiff = []
ans = -1/(4 * (x0**(3.0/2.0)))

# iterating over the approximation array
for x in df:
    # Add the absolute error.
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1


iter = 0
print("Second derivative 3 point formula with h = 10^-n")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1


iter = 0
h = 10.**-np.arange(1,7)
df = (-np.sqrt(x0 + (2*h)) + (16 * np.sqrt(x0 + h)) - (30 * np.sqrt(x0)) + (16 * np.sqrt(x0 - h)) - np.sqrt(x0 - (2*h)))/ (12 * (h**2))
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
df = (np.sqrt(x0 + h) - (2 * np.sqrt(x0)) + np.sqrt(x0 - h))/ (h**2)
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


# Using the five point formula
iter = 0;
h = 2.**-np.arange(1,10)
df = (-np.sqrt(x0 + (2*h)) + (16 * np.sqrt(x0 + h)) - (30 * np.sqrt(x0)) + (16 * np.sqrt(x0 - h)) - np.sqrt(x0 - (2*h)))/ (12 * (h**2))
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
