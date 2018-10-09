from math import cos, pi, sin

a, b = 0, pi


def f(x):
    return cos(x) + sin(x)


def f2(x1, x2):
    return (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def d_anal(x1, x2):
    return -4 * x1 * (-x1 ** 2 + x2) + 2 * x1 - 2, -2 * x1 ** 2 + 2 * x2
