import numpy as np

x0 = 0.7
iter = 0;
h = 2.**-np.arange(1,8)
df = (np.cos(x0 + 2*h) - (2 * np.cos(x0 + h)) + (2 * np.cos(x0 - h)) - np.cos(x0 - 2*h)) / (2*(h**3))
error= []
relDiff = []
ans = np.sin(x0)
print(ans)

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1

iter = 0
print("Third Derivative")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1


iter = 0;
df = (np.cos(x0 + 2*h) - (4 * np.cos(x0 + h)) + (6 * np.cos(x0)) - (4 * np.cos(x0 - h)) + np.cos(x0 - 2*h)) / (h**4)
error= []
relDiff = []
ans = np.cos(x0)
print(ans)

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1

iter = 0
print("Fourth Derivative")
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1
