def sum_range_list(list1, m, n):
    # Check if m and n are valid indices
    if m < 0 or n >= len(list1) or m > n:
        raise ValueError("Invalid indices m and n for the list")
    
    # Initialize sum to 0
    sum = 0
    
    # Loop through the range from m to n (inclusive)
    for i in range(m, n + 1):
        sum += list1[i]
    
    # Return the sum
    return sum