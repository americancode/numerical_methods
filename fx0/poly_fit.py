import numpy as np
import matplotlib.pyplot as plt


def plot_regression_line(x, y, coe, a, b, n):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)

    # predicted response vector
    xv = np.linspace(a,b,n)
    y_pred = np.zeros(len(xv))
    for i in range(0, len(coe)):
        if i == 0:
            y_pred = coe[i] + y_pred
        else:
            y_pred = coe[i] * (xv ** i) + y_pred

    # plotting the regression line
    plt.plot(xv, y_pred, color = "g", )

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def pfit(x, y, e):
    e +=1
    # Build A matrix
    A = np.zeros((e,e))
    total, power = 0, 1
    for i in range(0, len(A[0])):
        for j in range(0, len(A[0])):
            if total == 0:
                A[i,j] = len(x)
            else:
                powered = x ** power
                value = np.sum(powered)
                A[i,j] = value
                power += 1

            total += 1
        power = i + 1

    # Build b matrix
    b = np.zeros((e))
    for i in range(0, len(b)):
        if i == 0:
            b[i] = np.sum(y)
        else:
            poweredx = x ** i
            b[i] = np.sum(poweredx * y)

    return np.linalg.solve(A,b)


# plotting regression line
#plot_regression_line(x, y, my_ans, x[0],x[len(x)-1],1000)
