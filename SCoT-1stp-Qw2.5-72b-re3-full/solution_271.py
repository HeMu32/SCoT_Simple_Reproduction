def even_Power_Sum(n):
    sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        fifth_power = even_number ** 5
        sum += fifth_power
    return sum