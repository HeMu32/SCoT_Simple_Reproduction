def sum_Of_Series(n):
    # Initialize sum to 0
    sum = 0
    # Loop through each number from 1 to n
    for i in range(1, n + 1):
        # Calculate the cube of the current number and add it to the sum
        sum += i ** 3
    # Return the final sum
    return sum