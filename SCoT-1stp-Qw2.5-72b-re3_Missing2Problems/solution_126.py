def sum(a, b):
    # Initialize sum to 0
    sum = 0
    
    # Determine the smaller of the two numbers
    min_num = min(a, b)
    
    # Loop from 1 to min_num (inclusive)
    for i in range(1, min_num + 1):
        # Check if i is a divisor of both a and b
        if (a % i == 0) and (b % i == 0):
            # Add i to sum if it is a common divisor
            sum += i
    
    # Return the sum of common divisors
    return sum