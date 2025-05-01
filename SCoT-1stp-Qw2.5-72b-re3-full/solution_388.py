def highest_Power_of_2(n):
    highest_power = 1
    while highest_power * 2 <= n:
        highest_power *= 2
    return highest_power