def first_Factorial_Divisible_Number(x):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    
    n = 1
    while True:
        if factorial(n) % x == 0:
            return n
        n += 1