def max_path_sum(tri, m, n):
    # Initialize a DP table with the same dimensions as the triangle
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # Base case: the bottom row of the DP table is the same as the bottom row of the triangle
    for i in range(n):
        dp[m-1][i] = tri[m-1][i]
    
    # Fill the DP table from bottom to top
    for i in range(m-2, -1, -1):
        for j in range(i+1):
            # For each element, choose the maximum path sum from the two adjacent elements in the row below
            dp[i][j] = tri[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    # The top element of the DP table contains the maximum path sum
    return dp[0][0]