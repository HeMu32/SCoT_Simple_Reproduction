def rotate_left(list1, m, n):
    # Validate the input
    if not (0 <= m < n) or n != len(list1):
        raise ValueError("Invalid input: m must be within the bounds of the list length and n must match the list length.")
    
    # If no rotation is needed, return the list as is
    if m == 0 or not list1:
        return list1
    
    # Reduce m to find the effective rotation
    m = m % n
    
    # Perform the rotation
    return list1[m:] + list1[:m]