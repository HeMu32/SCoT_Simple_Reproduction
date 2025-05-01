def round_num(n, m):
    remainder = n % m
    if remainder < m / 2:
        rounded_value = n - remainder
    else:
        rounded_value = n + (m - remainder)
    return rounded_value