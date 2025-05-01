def breakSum(n):
    if n <= 0:
        return 0
    
    # Initialize the dp array with zeros
    dp = [0] * (n + 1)
    
    # Fill the dp array
    for i in range(1, n + 1):
        max_sum = 0
        for j in [i - 1, i - 2, i - 3]:
            if j >= 0:
                max_sum = max(max_sum, dp[j] + i - j)
        dp[i] = max_sum
    
    return dp[n]