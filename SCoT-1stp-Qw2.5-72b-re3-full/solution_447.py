def cube_nums(nums):
    # Define a lambda function to cube a number
    cube = lambda x: x ** 3
    # Apply the lambda function to each element in the list using map
    cubes = map(cube, nums)
    # Convert the map object to a list and return it
    return list(cubes)