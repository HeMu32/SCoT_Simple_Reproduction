def eulerian_num(n, m):
    # Base cases
    if n == 0 or m == 0:
        return 0
    if m == 0 or m == n - 1:
        return 1

    # Initialize a 2D list dp with all elements set to 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Base case
    dp[0][0] = 1

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(0, m + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + (i - 1) * dp[i - 1][j]

    return dp[n][m]