def solution(a, b, n):
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y

    gcd, x, y = extended_gcd(a, b)
    if n % gcd != 0:
        return None  # No solution exists
    x *= n // gcd
    y *= n // gcd
    return x, y