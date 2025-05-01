def tetrahedral_number(n):
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Calculate the nth tetrahedral number
    tetrahedral = n * (n + 1) * (n + 2) // 6
    
    # Return the result
    return tetrahedral