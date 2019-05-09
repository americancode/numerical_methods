import numpy as np

x0 = 1.0
iter = 0;
# approximate the derivative
h = 10.**-np.arange(1,7)
df = (np.log(x0 + h) - np.log(x0))/h
error= []
relDiff = []
ans = 1 / x0;

for x in df:
    error.append(abs( (df[iter-1] - ans) / (x - ans) ) )
    relDiff.append(abs( (x - df[iter-1]) / (df[iter-1]) ) )
    iter += 1

iter = 0
print("i:      h:      Approximation:      Ratio Of Errors:      Relative Differences")
for x in df:
    print(str(iter + 1) +  "    " + str(h[iter]) +  "    "  + str(x) + "    " + str(error[iter]) +  "    " + str(relDiff[iter]))
    iter += 1
