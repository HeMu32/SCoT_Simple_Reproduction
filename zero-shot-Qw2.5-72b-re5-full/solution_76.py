def count_Squares(m, n):
    if m < n:
        m, n = n, m
    return (m * (m + 1) * (3 * n - m + 1)) // 6