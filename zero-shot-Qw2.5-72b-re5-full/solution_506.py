def permutation_coefficient(n, k): 
    """
    Write a function to calculate the permutation coefficient of given p(n, k). 
    """ 
    if k > n:
        return 0
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    return result