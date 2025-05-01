def highest_Power_of_2(n):
    """
    Write a python function to find the highest power of 2 that is less than or equal to n.
    """
    power = 0
    while (1 << power) <= n:
        power += 1
    return 1 << (power - 1)