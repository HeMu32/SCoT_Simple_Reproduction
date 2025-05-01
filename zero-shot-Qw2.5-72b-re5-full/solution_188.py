def prod_Square(n):
    if n < 0:
        return False
    i = 0
    while i * i <= n:
        b = (n / (i * i)) ** 0.5
        if b.is_integer():
            return True
        i += 1
    return False