def find_Average_Of_Cube(n):
    if n <= 0:
        return 0
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    return sum_of_cubes / n