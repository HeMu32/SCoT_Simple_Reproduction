def square_Sum(n):
    sum = 0
    counter = 1
    odd_number = 1
    while counter <= n:
        sum += odd_number ** 2
        odd_number += 2
        counter += 1
    return sum