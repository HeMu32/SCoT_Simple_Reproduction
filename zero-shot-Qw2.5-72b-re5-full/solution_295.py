def sum_div(number):
    """
    Write a function to return the sum of all divisors of a number.
    """
    if number == 1:
        return 1
    divisors_sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    return divisors_sum