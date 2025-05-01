def find_Divisor(x, y):
    # Dictionary to store the count of each divisor
    divisor_count = {}
    
    # Loop through each number in the interval
    for num in range(x, y + 1):
        # Check each possible divisor
        for d in range(1, num + 1):
            if num % d == 0:
                if d in divisor_count:
                    divisor_count[d] += 1
                else:
                    divisor_count[d] = 1
    
    # Initialize variables to track the maximum occurring divisor
    max_divisor = None
    max_count = 0
    
    # Find the divisor with the maximum count
    for d, count in divisor_count.items():
        if count > max_count:
            max_divisor = d
            max_count = count
    
    return max_divisor