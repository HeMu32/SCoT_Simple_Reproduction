def get_Min_Squares(n):
    # Initialize the dp array with infinity and set dp[0] to 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Fill the dp array
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1

    return dp[n]