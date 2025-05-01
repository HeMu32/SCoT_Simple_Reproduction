def centered_hexagonal_number(n):
    # Calculate the nth centered hexagonal number using the formula
    res = 3 * n * (n - 1) + 1
    return res