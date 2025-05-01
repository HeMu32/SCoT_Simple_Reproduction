def sum_of_proper_divisors(n):
    """Helper function to calculate the sum of proper divisors of a number."""
    return sum([i for i in range(1, n) if n % i == 0])

def amicable_numbers_sum(limit):
    sum_amicable = 0
    for n in range(2, limit + 1):
        sum_divisors_n = sum_of_proper_divisors(n)
        if sum_divisors_n != n and sum_divisors_n <= limit:
            sum_divisors_sum_divisors_n = sum_of_proper_divisors(sum_divisors_n)
            if sum_divisors_sum_divisors_n == n:
                sum_amicable += n
    return sum_amicable