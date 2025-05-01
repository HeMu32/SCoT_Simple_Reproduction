def frequency_Of_Largest(n, arr):
    if n < 1 or not arr:
        return 0  # Return 0 if the array is empty or n is less than 1
    
    max_value = arr[0]
    frequency = 1
    
    for i in range(1, n):
        if arr[i] > max_value:
            max_value = arr[i]
            frequency = 1
        elif arr[i] == max_value:
            frequency += 1
    
    return frequency