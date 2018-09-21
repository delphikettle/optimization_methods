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


if __name__ == '__main__':
    eps = 0.000001
    print(dihiotomia(f, a, b, eps))
