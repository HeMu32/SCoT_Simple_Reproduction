def max_Prime_Factors(n):
    largest_prime = -1
    
    # Handle the case where n is even
    while n % 2 == 0:
        largest_prime = 2
        n = n // 2
    
    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n = n // i
    
    # If n is a prime number greater than 2
    if n > 2:
        largest_prime = n
    
    return largest_prime