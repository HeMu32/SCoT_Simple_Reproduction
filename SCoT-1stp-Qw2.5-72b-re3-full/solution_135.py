def hexagonal_num(n):
    if n < 1:
        return "Error: n must be a positive integer."
    # Calculate the nth hexagonal number using the formula
    hex_num = n * (2 * n - 1)
    return hex_num