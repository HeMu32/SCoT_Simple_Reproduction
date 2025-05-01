def sum_gp(a, n, r):
    """
    Write a function to find the sum of geometric progression series.
    """
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) / (1 - r)