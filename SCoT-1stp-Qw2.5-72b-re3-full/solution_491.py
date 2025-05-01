def sum_gp(a, n, r):
    if r == 1:
        # If the common ratio is 1, the series is a constant series.
        return a * n
    else:
        # Use the formula for the sum of a geometric series.
        return a * (1 - r**n) / (1 - r)