def square_Sum(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        squared_value = even_number ** 2
        sum_of_squares += squared_value
    return sum_of_squares