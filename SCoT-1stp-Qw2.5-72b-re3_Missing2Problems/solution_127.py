def multiply_int(x, y):
    # Initialize result to 0
    result = 0
    
    # Determine the sign of the result
    sign = -1 if (x < 0) ^ (y < 0) else 1
    
    # Convert x and y to their absolute values
    x, y = abs(x), abs(y)
    
    # Add x to result, y times
    for _ in range(y):
        result += x
    
    # If the sign is negative, negate the result
    if sign == -1:
        result = -result
    
    # Return the result
    return result