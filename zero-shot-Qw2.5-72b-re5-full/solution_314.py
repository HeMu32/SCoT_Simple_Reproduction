def max_sum_rectangular_grid(grid):
    """
    Write a function to find out the maximum sum such that no two chosen numbers are adjacent for the given rectangular grid of dimension 2 x n.
    """
    if not grid or not grid[0]:
        return 0

    n = len(grid[0])
    dp = [0] * (n + 1)
    
    dp[0] = 0
    dp[1] = max(grid[0][0], grid[1][0])

    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], dp[i-2] + max(grid[0][i-1], grid[1][i-1]))

    return dp[n]