def num_comm_div(x, y):
    count = 0
    min_val = min(x, y)
    for i in range(1, min_val + 1):
        if (x % i == 0) and (y % i == 0):
            count += 1
    return count