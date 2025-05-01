def sum_of_divisors(n):
    sum_div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum_div += i
    return sum_div

def areEquivalent(num1, num2):
    sum1 = sum_of_divisors(num1)
    sum2 = sum_of_divisors(num2)
    return sum1 == sum2