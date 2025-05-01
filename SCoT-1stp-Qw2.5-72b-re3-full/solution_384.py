def frequency_Of_Smallest(n, arr):
    if n < 1 or not arr:
        return 0  # Return 0 if the array is empty or n is less than 1
    
    smallest_value = min(arr)  # Find the smallest value in the array
    frequency = 0  # Initialize the frequency counter
    
    for element in arr:
        if element == smallest_value:
            frequency += 1  # Increment the frequency counter if the element is the smallest value
    
    return frequency  # Return the frequency of the smallest value