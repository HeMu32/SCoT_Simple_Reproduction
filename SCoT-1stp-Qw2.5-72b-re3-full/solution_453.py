def sumofFactors(n):
    sum_even_factors = 0
    for i in range(2, n + 1, 2):
        if n % i == 0:
            sum_even_factors += i
    return sum_even_factors