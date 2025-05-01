def gcd(x, y): 
    while y != 0:
        temp = y
        y = x % y
        x = temp
    return x