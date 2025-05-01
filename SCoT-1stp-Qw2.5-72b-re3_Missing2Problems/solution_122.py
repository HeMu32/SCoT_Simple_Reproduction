def smartNumber(n):
    def is_smart_number(num):
        factors = set()
        # Check for each number from 2 to the square root of num
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                factors.add(i)
                num //= i
        if num > 1:
            factors.add(num)
        return len(factors) >= 3

    smart_numbers = []
    current_number = 2
    while len(smart_numbers) < n:
        if is_smart_number(current_number):
            smart_numbers.append(current_number)
        current_number += 1
    return smart_numbers[-1]