def ncr_modp(n, r, p):
    # If r is greater than n, it's not possible to choose more items than available
    if r > n:
        return 0
    # If r is 0 or r is equal to n, there is exactly one way to choose no items or all items
    if r == 0 or r == n:
        return 1
    
    # Initialize result to 1
    result = 1
    
    # Calculate nCr % p using a loop
    for i in range(1, r + 1):
        result = (result * (n - r + i)) % p
        result = (result * pow(i, p - 2, p)) % p  # Using Fermat's Little Theorem for modular inverse
    
    return result