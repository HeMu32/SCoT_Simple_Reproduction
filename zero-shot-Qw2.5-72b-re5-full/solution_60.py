def max_len_sub(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) == 1:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)