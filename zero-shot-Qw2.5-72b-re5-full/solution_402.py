def ncr_modp(n, r, p):
    if r > n:
        return 0
    if r == 0 or r == n:
        return 1
    r = min(r, n - r)  # Utilize the property C(n, r) = C(n, n-r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator = (numerator * (n - i)) % p
        denominator = (denominator * (i + 1)) % p
    return (numerator * pow(denominator, p - 2, p)) % p