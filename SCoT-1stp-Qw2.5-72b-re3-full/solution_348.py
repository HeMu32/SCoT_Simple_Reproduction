def find_ways(M):
    # Initialize the dp table with zeros
    dp = [[0 for _ in range(M + 1)] for _ in range(M + 1)]
    
    # There is one way to have a prefix sum of 0 with 0 elements
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, M + 1):
        for j in range(i + 1):
            if j > 0:
                dp[i][j] += dp[i-1][j-1]  # Adding a 1 to the sequence
            if j < i:
                dp[i][j] += dp[i-1][j+1]  # Adding a -1 to the sequence
    
    # The result is the number of ways to have a prefix sum of 0 after M elements
    return dp[M][0]