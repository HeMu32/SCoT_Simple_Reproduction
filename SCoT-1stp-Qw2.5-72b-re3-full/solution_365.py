def count_Digit(n):
    count = 0
    if n == 0:
        return 1
    n = abs(n)  # Ensure n is positive to handle negative numbers correctly
    while n != 0:
        count += 1
        n //= 10
    return count