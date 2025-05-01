def highest_Power_of_2(n):
    power = 1
    while power * 2 <= n:
        power *= 2
    return power