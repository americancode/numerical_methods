import numpy as np

def trapezoid(fnc, a, b, n):
    n = int(n)
    h = (b-a) / n

    s = (fnc(a) + fnc(b)) / 2
    for k in range(1, int(n)):
        s += fnc(a + k * h)
    return s*h


def simpson(fnc, a, b, n):
    n = int(n)
    h = (b-a) / n
    s = (fnc(a) + fnc(b))
    for k in range(1, int(n), 2):
        s += 4 * fnc(a + k * h)
    for k in range(2, n-1, 2):
        s += 2 * fnc(a + k * h)
    return s*h/3


def midpoint(fnc, a, b, n):
    n = int(n)
    h = (b-a) / n
    s = 0.0
    x = a + h/2
    while (x < b):
        s += h * fnc(x)
        x += h

    return s
