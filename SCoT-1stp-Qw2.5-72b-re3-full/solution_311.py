def set_left_most_unset_bit(n):
    # Step 1: Convert n to binary and check if all bits are set
    if n == 0:
        return 1  # Special case where n is 0, the result should be 1 (binary 1)
    
    # Step 2: Find the leftmost unset bit
    mask = 1
    while n & mask:
        mask <<= 1
    
    # Step 3: Set the leftmost unset bit
    result = n | mask
    
    return result