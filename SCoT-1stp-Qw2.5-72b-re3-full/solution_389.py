def find_lucas(n):
    # Base cases for the Lucas sequence
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    # Initialize the first two Lucas numbers
    lucas_prev2 = 2  # L(0)
    lucas_prev1 = 1  # L(1)
    
    # Compute the n'th Lucas number iteratively
    for _ in range(2, n + 1):
        lucas_current = lucas_prev1 + lucas_prev2
        # Update the previous two Lucas numbers
        lucas_prev2 = lucas_prev1
        lucas_prev1 = lucas_current
    
    return lucas_current