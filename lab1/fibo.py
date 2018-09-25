_fibos = {
    1: 1,
    2: 1
}


def fibo(n):
    if n not in _fibos:
        i = n
        while not (i in _fibos):
            i -= 1

        while i < n:
            _fibos[i + 1] = _fibos[i] + _fibos[i - 1]
            i += 1
    return _fibos[n]
