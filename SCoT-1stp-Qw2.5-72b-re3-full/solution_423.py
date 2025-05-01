def get_maxgold(gold, m, n):
    # Initialize a 2D list dp with the same dimensions as gold
    dp = [[0 for _ in range(n)] for _ in range(m)]
    
    # Copy the first column of gold to dp
    for i in range(m):
        dp[i][0] = gold[i][0]
    
    # Iterate through each cell in the gold mine starting from the second column
    for j in range(1, n):
        for i in range(m):
            # Initialize the maximum gold collected from the previous column to 0
            max_gold = 0
            
            # Check the possible moves from the previous column
            if i > 0:
                max_gold = max(max_gold, dp[i-1][j-1])  # Move from the cell diagonally up to the left
            if i < m - 1:
                max_gold = max(max_gold, dp[i+1][j-1])  # Move from the cell diagonally down to the left
            max_gold = max(max_gold, dp[i][j-1])  # Move from the cell directly to the left
            
            # Update dp[i][j] with the maximum gold collected from the possible moves plus the gold in the current cell
            dp[i][j] = gold[i][j] + max_gold
    
    # Find the maximum value in the last column of dp
    max_gold_collected = max(dp[i][n-1] for i in range(m))
    
    # Return the maximum value
    return max_gold_collected