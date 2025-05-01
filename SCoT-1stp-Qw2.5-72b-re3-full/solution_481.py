def is_subset_sum(set, n, sum):
    # Base cases
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    
    # Create a 2D array to store the subset sum solutions
    dp = [[False for x in range(sum+1)] for x in range(n+1)]
    
    # Initialize the first column as True
    for i in range(n+1):
        dp[i][0] = True
    
    # Initialize the first row as False (except dp[0][0])
    for j in range(1, sum+1):
        dp[0][j] = False
    
    # Fill the dp array
    for i in range(1, n+1):
        for j in range(1, sum+1):
            if set[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-set[i-1]]
    
    return dp[n][sum]