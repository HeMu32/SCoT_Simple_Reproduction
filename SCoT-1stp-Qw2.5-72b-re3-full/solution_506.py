def permutation_coefficient(n, k):
    # Initialize the result to 1
    result = 1
    
    # Check if k is greater than n
    if k > n:
        return 0
    
    # Calculate the permutation coefficient P(n, k)
    for i in range(k):
        result *= (n - i)
    
    # Return the result
    return result