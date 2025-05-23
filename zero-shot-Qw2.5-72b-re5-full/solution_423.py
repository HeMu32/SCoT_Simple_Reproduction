def get_maxgold(gold, m, n):
    def max_gold_util(gold, m, n, i, j, dp):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        right = max_gold_util(gold, m, n, i, j + 1, dp)
        right_up = max_gold_util(gold, m, n, i - 1, j + 1, dp)
        right_down = max_gold_util(gold, m, n, i + 1, j + 1, dp)
        dp[i][j] = gold[i][j] + max(right, right_up, right_down)
        return dp[i][j]

    dp = [[-1 for _ in range(n)] for _ in range(m)]
    max_gold = 0
    for i in range(m):
        max_gold = max(max_gold, max_gold_util(gold, m, n, i, 0, dp))
    return max_gold