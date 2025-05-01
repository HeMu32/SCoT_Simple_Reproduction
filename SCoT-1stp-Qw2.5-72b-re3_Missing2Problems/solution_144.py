def sum_Pairs(arr, n):
    # Initialize sum to 0
    sum = 0
    
    # Sort the array to make the calculation of absolute differences easier
    arr.sort()
    
    # Loop through each element in the array
    for i in range(n):
        # For each subsequent element, calculate the absolute difference
        for j in range(i + 1, n):
            # Calculate the absolute difference and add it to the sum
            sum += abs(arr[j] - arr[i])
    
    # Return the total sum of absolute differences
    return sum