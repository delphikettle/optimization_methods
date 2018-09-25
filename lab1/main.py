from math import sqrt

from lab1.fibo import fibo
from lab1.variant import f, a, b


def dihiotomia(f, a, b, eps):
    it_no = 0

    while b - a >= eps:
        it_no += 2

        delta = eps / 2.25
        x0 = (b + a) / 2 - delta
        x1 = (b + a) / 2 + delta

        if f(x0) < f(x1):
            b = x1
        else:
            a = x0

    return ((b + a) / 2, it_no)


phi = (1 + sqrt(5)) / 2


def golden_section(f, a, b, eps):
    it_no = 0
    x1 = a
    x2 = b
    f1, f2 = f(x1), f(x2)
    while b - a > eps:
        t = (b - a) / phi
        if f1 < f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + t
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - t
            f1 = f(x1)
        it_no += 1

    return ((b + a) / 2, it_no)


def meth_fibo(f, a, b, eps):
    it_no = 0
    # get n
    n = 1
    while abs(b - a) / eps > fibo(n):
        n += 1

    k = 0

    x1 = a + fibo(n - k) / fibo(n - k + 2) * (b - a)
    x2 = a + fibo(n - k + 1) / fibo(n - k + 2) * (b - a)
    f1, f2 = f(x1), f(x2)
    while k < n:
        if f1 > f2:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + fibo(n - k + 1) / fibo(n - k + 2) * (b - a)
            f2 = f(x2)
        else:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + fibo(n - k + 1) / fibo(n - k + 2) * (b - a)
            f1 = f(x1)

        k += 1
        it_no += 1

    return (x1, it_no)


def linear_min(f, eps):
    x0 = 0
    prev = x0

    if f(x0) <= f(x0 + eps):
        h = eps
    else:
        h = -eps

    x1 = x0 + h
    f0, f1 = f(x0), f(x1)

    while f1 <= f0:
        h *= 2
        prev, x0, x1 = x0, x1, x0 + h
        f0, f1 = f1, f(x1)

    return meth_fibo(f, prev, x1, eps)[0]


if __name__ == '__main__':
    eps = 0.00001

    print(f'Метод дихотомии: x = {dihiotomia(f, a, b, eps)}')
    print(f'Метод золотого сечения: x = {golden_section(f, a, b, eps)}')
    print(f'Метод Фибоначчи: x = {meth_fibo(f,a, b, eps)}')
    print(f'Метод поиска на прямой: x = {linear_min(f, eps)}')
