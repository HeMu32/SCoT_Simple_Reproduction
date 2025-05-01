def gcd(x, y):
    """Helper function to calculate the greatest common divisor (GCD) of two numbers."""
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    """Helper function to calculate the least common multiple (LCM) of two numbers using their GCD."""
    return x * y // gcd(x, y)

def answer(L, R):
    found = False
    for a in range(L, R):
        for b in range(a + 1, R + 1):
            current_lcm = lcm(a, b)
            if L <= current_lcm <= R:
                found = True
                result = (a, b)
                break
        if found:
            break
    return result if found else None