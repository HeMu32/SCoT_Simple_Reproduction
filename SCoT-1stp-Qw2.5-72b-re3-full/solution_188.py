import math

def prod_Square(n):
    i = 0
    while i * i <= n:
        j = math.sqrt(n / (i * i))
        if j.is_integer() and i * i * j * j == n:
            return True
        i += 1
    return False