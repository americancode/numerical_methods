import numpy as np
import guass as g
import jacobi as jb
import seidal as sd
import re

s = []

for x in range(1,7):
    for z in range(1,6):
        s.append("P" + str(x) + "," + str(z))
        
print(s)

# Empty matrix
A = np.zeros((30,30))

def pv_0(i,j):
    return "P" + str(i) + "," + str(j)
def pv0(i,j):
    return "P" + str(i-1) + "," + str(j)
def pv1(i,j):
    return "P" + str(i+1) + "," + str(j)
def pv2(i,j):
    return "P" + str(i) + "," + str(j-1)
def pv3(i,j):
    return "P" + str(i) + "," + str(j+1)

def getPos(str):
    return s.index(str)

count = 0
for x in range(1,7): # iterate over the rows
    for z in range(1,6): # iterate over the column
        p_0 = pv_0(x,z)
        p0 = pv0(x,z)
        p1 = pv1(x,z)
        p2 = pv2(x,z)
        p3 = pv3(x,z)

        A[count,getPos(p_0)] = -1.
        if not re.findall("^P0,\d{1}", p0):
            A[count,getPos(p0)] = 0.25
        if not re.findall("^P7,\d{1}", p1):
            A[count,getPos(p1)] = 0.25
        if not re.findall("^P\d{1},0", p2):
            A[count,getPos(p2)] = 0.25
        if not re.findall("^P\d{1},6", p3):
            A[count,getPos(p3)] = 0.25
        count += 1


print(A)
b =  np.zeros((30))

# Adjust for known values (Move to right hand side of the equation)
b[0] = -1
b[5] = -1
b[10] = -1
b[15] = -1
b[20] = -1
b[25] = -1

D = np.diag(A)
print(b)

print("With Jacobi")
ans = jb.jacobi(A, b, 10.**-6)
print(ans)

print("With Seidal")
ans2 = sd.seidal(A, b, 10.**-6)
print(ans2)
