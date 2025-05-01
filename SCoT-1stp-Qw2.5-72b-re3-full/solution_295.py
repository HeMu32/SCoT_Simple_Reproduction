import math

def sum_div(number):
    sum_divisors = 0
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            sum_divisors += i
            if i != number // i:
                sum_divisors += number // i
    return sum_divisors