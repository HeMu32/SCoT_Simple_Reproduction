def sum_difference(n):
    sum_of_squares = 0
    square_of_sum = 0
    for i in range(1, n + 1):
        sum_of_squares += i ** 2
        square_of_sum += i
    square_of_sum = square_of_sum ** 2
    difference = square_of_sum - sum_of_squares
    return difference