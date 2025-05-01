def does_Contain_B(a, b, c):
    # Calculate the difference between c and a
    diff = c - a
    
    # Check if b is zero
    if b == 0:
        return a == c
    
    # Check if diff is divisible by b
    if diff % b == 0:
        # Calculate k
        k = diff // b
        # Check if k is non-negative
        if k >= 0:
            return True
        else:
            return False
    else:
        return False