import math

from lab1.main import golden_section, linear_search
from lab1.variant import f2


def d_num(x1, x2, f=f2, delta=0.0001):
    d_dx1 = (f(x1 + delta, x2) - f(x1, x2)) / delta
    d_dx2 = (f(x1, x2 + delta) - f(x1, x2)) / delta

    return d_dx1, d_dx2


def unit_vectors(x1, x2):
    length = (x1 ** 2 + x2 ** 2) ** 0.5

    if not length:
        return 0, 0

    single_x1 = x1 / length
    single_x2 = x2 / length

    return single_x1, single_x2


def get_func_by_lambda(x1, x2, s1, s2):
    def func(a):
        return f2(x1 + a * s1, x2 + a * s2)

    return func


def get_lambda(x1, x2, s1, s2):
    func = get_func_by_lambda(x1, x2, s1, s2)
    start, end = linear_search(func, 50)

    a = golden_section(func, start, end, 0.01)[0]
    return a


def grad_desc(eps):
    prev_value = math.inf

    x1 = 15
    x2 = 10

    value = f2(x1, x2)

    iteration = 0

    while math.fabs(value - prev_value) > eps:
        iteration += 1

        grad_x1, grad_x2 = d_num(x1, x2)
        s1, s2 = unit_vectors(grad_x1, grad_x2)
        a = get_lambda(x1, x2, s1, s2)

        x1 = x1 + a * s1
        x2 = x2 + a * s2

        prev_value = value
        value = f2(x1, x2)

    return x1, x2


x1, x2 = grad_desc(0.0001)
print(f'x1={x1}, x2={x2}')
print(f'f(x1, x2)={f2(x1, x2)}')
