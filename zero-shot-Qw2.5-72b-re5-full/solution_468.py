def max_product(arr, n):
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] * arr[i])
    return max(dp)

# Example usage:
# arr = [3, 4, 5, 8]
# n = len(arr)
# print(max_product(arr, n))  # Output: 120