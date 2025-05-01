def bell_number(n):
    # Initialize a 2D list to store Bell numbers
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    # There is exactly one way to partition a set of size 0
    dp[0][0] = 1
    
    # Fill the dp table
    for i in range(1, n+1):
        # The number of ways to partition a set of size i into 0 subsets
        dp[i][0] = dp[i-1][i-1]
        
        # The number of ways to partition a set of size i into j subsets
        for j in range(1, i+1):
            dp[i][j] = dp[i-1][j-1] + j * dp[i-1][j]
    
    # The Bell number for a set of size n is dp[n][0]
    return dp[n][0]