def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def is_coprime(x, y):
    return gcd(x, y) == 1