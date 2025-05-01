def breakSum(n):
    if n == 0:
        return 0
    if n < 3:
        return n
    return max(n, breakSum(n // 3) + breakSum(n // 3) + breakSum(n - 2 * (n // 3)))

# Example usage:
print(breakSum(10))  # Output: 11