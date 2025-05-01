def find_Average_Of_Cube(n):
    sum_of_cubes = 0
    for i in range(1, n + 1):
        sum_of_cubes += i ** 3
    average = sum_of_cubes / n
    return average