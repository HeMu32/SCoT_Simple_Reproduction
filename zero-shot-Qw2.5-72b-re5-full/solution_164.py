def divSum(n):
    def sum_of_divisors(x):
        return sum(i for i in range(1, x) if x % i == 0)
    
    return sum_of_divisors(n) == n