def min_of_three(a, b, c):
    # First, find the minimum between a and b
    if a < b:
        min_val = a
    else:
        min_val = b
    # Then, compare the minimum of a and b with c
    if min_val > c:
        min_val = c
    return min_val