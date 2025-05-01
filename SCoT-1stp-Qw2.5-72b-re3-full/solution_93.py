def power(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    result = 1
    for i in range(1, b + 1):
        result *= a
    return result