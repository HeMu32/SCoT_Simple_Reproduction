def find(n, m):
    if m == 0:
        raise ValueError("Division by zero is not allowed.")
    quotient = n // m
    return quotient