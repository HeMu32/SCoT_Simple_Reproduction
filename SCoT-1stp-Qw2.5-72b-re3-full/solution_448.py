def cal_sum(n):
    # Initialize the list to store the first n Perrin numbers
    perrin = [0] * n
    
    # Set the first three Perrin numbers
    perrin[0] = 3
    perrin[1] = 0
    perrin[2] = 2
    
    # If n is less than or equal to 2, return the sum of the first n elements
    if n <= 2:
        return sum(perrin[:n])
    
    # Calculate the remaining Perrin numbers
    for i in range(3, n):
        perrin[i] = perrin[i-2] + perrin[i-3]
    
    # Return the sum of all elements in the perrin list
    return sum(perrin)