def next_Power_Of_2(n):
    if n <= 0:
        return 1
    result = 1
    while result < n:
        result *= 2
    return result