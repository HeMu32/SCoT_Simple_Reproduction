def find_longest_repeating_subseq(s):
    def lcs(X, Y, n, m):
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if X[i - 1] == Y[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[n][m]

    n = len(s)
    return lcs(s, s, n, n)

# Example usage
# print(find_longest_repeating_subseq("AABEBCDD"))  # Output: 3