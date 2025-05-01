def colon_tuplex(tuplex, m, n):
    # Check if m and n are within the bounds of the tuple length
    if m < 0 or n > len(tuplex) or m >= n:
        return "Error: Index out of bounds or invalid range"
    
    # Slice the tuple from index m to n
    sliced_tuple = tuplex[m:n]
    
    # Return the sliced tuple
    return sliced_tuple