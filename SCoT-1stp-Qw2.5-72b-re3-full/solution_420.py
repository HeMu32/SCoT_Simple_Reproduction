def cube_Sum(n):
    sum = 0
    for i in range(1, n + 1):
        even_number = 2 * i
        cube = even_number ** 3
        sum += cube
    return sum