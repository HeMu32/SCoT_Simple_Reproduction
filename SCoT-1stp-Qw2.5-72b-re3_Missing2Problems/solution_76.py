def count_Squares(m, n):
    count = 0
    min_dim = min(m, n)
    for i in range(1, min_dim + 1):
        horizontal_squares = m - i + 1
        vertical_squares = n - i + 1
        count += horizontal_squares * vertical_squares
    return count