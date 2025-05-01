def count_Squares(m, n):
    count = 0
    # Determine the smaller dimension to limit the size of the largest possible square
    min_dim = min(m, n)
    for s in range(1, min_dim + 1):
        # Calculate the number of s x s squares that can fit in the rectangle
        horizontal_fits = n - s + 1
        vertical_fits = m - s + 1
        count += horizontal_fits * vertical_fits
    return count