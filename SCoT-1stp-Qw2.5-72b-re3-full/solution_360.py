def get_carol(n):
    if n < 1:
        raise ValueError("n must be a positive integer")
    
    k = 2
    count = 0
    
    while True:
        carol_number = (2**k - 1)**2 - 2
        count += 1
        if count == n:
            return carol_number
        k += 1