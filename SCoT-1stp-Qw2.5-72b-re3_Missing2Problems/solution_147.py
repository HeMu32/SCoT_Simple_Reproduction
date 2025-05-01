def max_path_sum(tri, m, n):
    # Initialize the dp array with the same dimensions as tri
    dp = [[0 for _ in range(len(tri[row]))] for row in range(m)]
    
    # The starting point
    dp[0][0] = tri[0][0]
    
    # Fill the dp array
    for row in range(1, m):
        for col in range(len(tri[row])):
            if col == 0:
                # First element in the row can only come from the element directly above
                dp[row][col] = dp[row-1][col] + tri[row][col]
            elif col == len(tri[row]) - 1:
                # Last element in the row can only come from the element directly above and to the left
                dp[row][col] = dp[row-1][col-1] + tri[row][col]
            else:
                # Middle elements can come from either the element directly above or the element directly above and to the left
                dp[row][col] = max(dp[row-1][col-1], dp[row-1][col]) + tri[row][col]
    
    # The maximum path sum is the maximum value in the last row of dp
    max_sum = max(dp[m-1])
    
    return max_sum