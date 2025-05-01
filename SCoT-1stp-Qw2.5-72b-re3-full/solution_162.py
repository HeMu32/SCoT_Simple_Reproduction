def sum_series(n):
    sum = 0
    current = n
    while current > 0:
        sum += current
        current -= 2
    return sum