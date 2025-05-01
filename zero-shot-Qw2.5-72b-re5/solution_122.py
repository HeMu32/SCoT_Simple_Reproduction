def smartNumber(n):
    def is_smart(num):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisor = num // i
                if i % 2 == 0 and divisor % 2 == 0:
                    return True
        return False

    count = 0
    num = 1
    while True:
        if is_smart(num):
            count += 1
            if count == n:
                return num
        num += 1

# Example usage:
# print(smartNumber(5))  # Output: 10