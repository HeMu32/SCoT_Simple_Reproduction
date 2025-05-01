def binomial_Coeff(n, k):
    # If k is 0 or equal to n, there is only one way to choose the items
    if k == 0 or k == n:
        return 1
    
    # Initialize the binomial coefficient
    binomial_coeff = 1
    
    # Calculate the binomial coefficient using the multiplicative formula
    for i in range(1, k + 1):
        binomial_coeff *= (n - i + 1)
        binomial_coeff //= i
    
    return binomial_coeff