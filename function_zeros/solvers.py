import numpy as np


def bisection(fn, a, b, tol, details=False):
    fa = fn(a)
    fb = fn(b)
    iterations = 0
    history = []
    while abs(b - a) > tol: # 2 * tol:
        m = (a+b) / 2
        if details:
            print("M is: " + str(m))
        history.append(m)
        fm = fn(m)

        if fa * fm <= 0: # if f(a) * f(m) is negative move the right hand Interval
            b = m
        else:  # else move the left hand interval
            a = m
        iterations += 1
    if details:
        print("A is " + str(a))
        print("B is " + str(b))
        print("Interval Length :" + str(abs(b - a)))
    return (m, iterations, history)

def bisection_e(fn, a, b, tol, details=False):
    old = 500000
    fa = fn(a)
    fb = fn(b)
    iterations = 0
    history = []
    errors = []
    m = 0

    while abs(m - old) > tol:
        old = m
        m = (a+b) / 2
        if details:
            print("M is: " + str(m))
        history.append(m)
        fm = fn(m)

        if fa * fm <= 0:
            b = m
        else:
            a = m
        # add error to array
        if iterations != 0:
            errors.append(abs(m - old))

        iterations += 1
    if details:
        print("A is " + str(a))
        print("B is " + str(b))
        print("Interval Length :" + str(abs(b - a)))

    return (m, iterations, np.asarray(history), np.asarray(errors))

def newton(fn, df, g, tol, details = False):
    old = g + 1 # Ensure iteration starts
    iterations = 0
    history = []
    errors = []
    if details:
        print("Guess is: " + str(g))

    while abs(g - old) > tol:
        old = g
        g = old - fn(old) / df(old)
        if details:
            print("Approximation is: " + str(g))
        history.append(g)
        if iterations != 0:
            errors.append(abs(g - old))

        iterations += 1

    return (g, iterations, np.asarray(history), np.asarray(errors))



def newton_iterations(fn, df, g, its, details = False):
    old = g + 1 # Ensure iteration starts
    iterations = 0
    if details:
        print("Guess is: " + str(g))

    for i in range(0, its):
        old = g
        g = old - fn(old) / df(old)
        if details:
            print("Approximation is: " + str(g))
        iterations += 1
    return (g, iterations)



def fixedPoint(fn, g, tol, details = False):
    old = 500000
    iterations = 0
    history = []
    errors = []
    if details:
        print("Guess is: " + str(g))
    while abs(g - old) > tol:
        old = g
        g = fn(g)
        if details:
            print("Approximation is: " + str(g))
        history.append(g)
        # add error to array
        if iterations != 0:
            errors.append(abs(g - old))
        iterations += 1

    return (g, iterations, np.asarray(history), np.asarray(errors))


def fixedPoint_iterations(fn, g, its, details = False):
    old = 0
    iterations = 0
    if details:
        print("Guess is: " + str(g))
    for i in range(0, its):
        old = g
        g = fn(g)
        if details:
            print("Approximation is: " + str(g))
        iterations += 1

    return (g, iterations)



def secant_iterations(fn, g1, g2, its, details = False):
    iterations = 0
    if details:
        print("Guess 1 is: " + str(g1))
        print("Guess 2 is: " + str(g2))

    for i in range(0, its):
        s_g2 = g2 # save g2
        g2 =  g1 - ((fn(g1) * (g1 - g2)) / (fn(g1) - fn(g2)) )
        g1 = s_g2 # Set the old g2 to g1
        if details:
            print("Approximation is: " + str(g2))
        iterations += 1
    return (g2, iterations)

def secant(fn, g1, g2, tol, details = False):
    iterations = 0
    history = []
    errors = []
    if details:
        print("Guess 1 is: " + str(g1))
        print("Guess 2 is: " + str(g2))

    while abs(g2 - g1) > tol:
        s_g2 = g2 # save g2
        g2 =  g1 - ((fn(g1) * (g1 - g2)) / (fn(g1) - fn(g2)) )
        g1 = s_g2 # Set the old g2 to g1
        if details:
            print("Approximation is: " + str(g2))
        history.append(g2)
        # add error to array
        if iterations != 0:
            errors.append(abs(g2 - g1))
        iterations += 1

    return (g2, iterations, np.asarray(history), np.asarray(errors))

def newton2d(fcn, Jac, g, tol):
    old = np.zeros_like(g)
    old[0] = g[0] + 1
    while max(abs(g - old)) > tol:
        old = g
        f = fcn(old) 
        f1 = f[0]
        f2 = f[1]
        J = Jac(old)
        f1x = J[0,0] 
        f1y = J[0,1] 
        f2x = J[1,0] 
        f2y = J[1,1]
        D = f1x * f2y - f1y * f2x
        h = (f2 * f1y - f1 * f2y) / D 
        k = (f1 * f2x - f2 * f1x) / D 
        g = old + np.array((h, k))
        #print(g)
    return g