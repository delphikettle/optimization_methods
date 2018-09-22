from math import sqrt

from lab1.fibo import fibo
from lab1.variant import f, a, b


def dihiotomia(f, a, b, eps):
    it_no = 0
    delta_factor = 0.1 * 16

    while b - a >= eps:
        it_no += 1

        delta = eps / (2 + delta_factor)
        x0 = (b + a) / 2 - delta
        x1 = (b + a) / 2 + delta

        if f(x0) < f(x1):
            b = x1
        else:
            a = x0

        if not it_no % 1000:
            print(f'{it_no} iterations: a={a}, b={b}, res={(b - a) / 2}')
            delta_factor *= 2

    return (b - a) / 2


k0, k1 = (3 - sqrt(5)) / 2, (sqrt(5) - 1) / 2


def golden_section(f, a, b, eps):
    while b - a >= eps:
        x0 = a + k0 * (b - a)
        x1 = a + k1 * (b - a)
        if f(x0) < f(x1):
            b = x1
        else:
            a = x0
    return (b - a) / 2


def meth_fibo(f, a, b, eps):
    a0, b0 = a, b
    # get n
    n = 0
    while (b0 - a0) / eps >= fibo(n + 2):
        n += 1

    x1 = a0 + fibo(n) / fibo(n + 2) * (b0 - a0)
    x2 = a0 + fibo(n + 1) / fibo(n + 2) * (b0 - a0)

    k = 1
    while k < n:
        k += 1

        x1 = a + fibo(n - k + 1) / fibo(n + 2) * (b0 - a0)
        x2 = a + fibo(n - k + 2) / fibo(n + 2) * (b0 - a0)

        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

    return a + fibo(1) / fibo(n + 2) * (b0 - a0)


if __name__ == '__main__':
    eps = 0.000001
    print(f'Метод дихотомии: x = {dihiotomia(f, a, b, eps)}')
    print(f'Метод золотого сечения: x = {golden_section(f, a, b, eps)}')
    print(f'Метод Фибоначчи: x = {meth_fibo(f, a, b, eps)}')
