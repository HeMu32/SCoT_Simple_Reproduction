def max_len_sub(arr, n):
    dp = {}
    max_len = 1
    for num in arr:
        if num - 1 in dp:
            dp[num] = dp[num - 1] + 1
        else:
            dp[num] = 1
        max_len = max(max_len, dp[num])
    return max_len