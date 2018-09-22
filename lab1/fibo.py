_fibos = {
    1: 1,
    2: 1
}


def fibo(n):
    try:
        return _fibos[n]
    except KeyError:
        val = fibo(n - 1) + fibo(n - 2)
        _fibos[n] = val
        return val
