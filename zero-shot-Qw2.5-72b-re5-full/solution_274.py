def even_binomial_Coeff_Sum(n):
    # Initialize a list to store binomial coefficients
    C = [0 for i in range(n+1)]
    C[0] = 1  # nC0 is 1

    # Calculate binomial coefficients and store them in C[]
    for i in range(1, n+1):
        # Compute next row of pascal triangle using the previous row
        j = min(i, n-i)
        while j > 0:
            C[j] = C[j] + C[j-1]
            j -= 1

    # Sum of even index binomial coefficients
    sum_even = sum(C[i] for i in range(0, n+1, 2))
    return sum_even