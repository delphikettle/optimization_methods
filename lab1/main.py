from math import sqrt

from fibo import fibo
from variant import f, a, b


def dihiotomia(f, a, b, eps):
    it_no = 0


    while b - a >= eps:
        it_no += 2

        delta = eps / (2.2)
        x0 = (b + a) / 2 - delta
        x1 = (b + a) / 2 + delta

        if f(x0) < f(x1):
            b = x1
        else:
            a = x0

    return (b + a) / 2, it_no


phi = (1 + sqrt(5)) / 2


def golden_section(f, a, b, eps):
    it_no = 2
    t = 0.618
    x0 = a + (1 - t) * (b - a)
    x1 = a + t * (b - a)

    f0 = f(x0)
    f1 = f(x1)

    while ((b - a) >= eps):
        if (f0 > f1):
            a = x0
            x0 = x1
            f0 = f1
            x1 = a + t * (b - a)
            f1 = f(x1)
            it_no += 1
        else:
            b = x1
            x1 = x0
            f1 = f0
            x0 = a + (1 - t) * (b - a)
            f0 = f(x0)
            it_no += 1
    return (b + a) / 2, it_no


def meth_fibo(f, a, b, eps):
    it_no = 0
    a0, b0 = a, b
    # get n
    n = 3
    while (b0 - a0) / eps >= fibo(n):
        n += 1

    k = 0
    x1 = a + fibo(n - 2) / fibo(n) * (b - a)
    x2 = a + fibo(n - 1) / fibo(n) * (b - a)

    f1 = f(x1)
    f2 = f(x2)
    while (k != n - 2):

        if f(x1) > f(x2):
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + fibo(n - 1) / fibo(n) * (b - a)
            f2 = f(x2)
            it_no += 1


        else:
            b = x2
            x2 = x1
            x1 = a + fibo(n - 2) / fibo(n) * (b - a)
            f2 = f1
            f1 = f(x1)
            it_no += 1

        k += 1

    return (a + b) / 2, it_no


def linear_search(f, eps):
    x0 = 0
    x1 = 0
    h = 0

    if (f(x0) > f(x0 + eps)):
        x1 = x0 + eps
        h = eps
    elif (f(x0) < f(x0 - eps)):
        x1 = x0 - eps
        h = -eps
    h *= 2
    x2 = x1 + h
    while (f(x1) > f(x2)):
        h *= 2
        x0 = x1
        x1 = x2
        x2 += h
    return meth_fibo(f, x0, x2, eps)




if __name__ == '__main__':
    eps = 0.00001

    print(f'Метод дихотомии: x = {dihiotomia(f, a, b, eps)}')
    print(f'Метод золотого сечения: x = {golden_section(f, a, b, eps)}')
    print(f'Метод Фибоначчи: x = {meth_fibo(f, a, b, eps)}')
    print(f'Метод линейный: x = {linear_search(f, eps)}')
