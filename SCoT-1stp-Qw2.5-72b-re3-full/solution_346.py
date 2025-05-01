def zigzag(n, k):
    if n < 0 or k < 0:
        return 0
    if n == 0 or k == 0:
        return 1
    result = 0
    for i in range(k + 1):
        result += zigzag(n - 1, i) + zigzag(n, i - 1)
    return result