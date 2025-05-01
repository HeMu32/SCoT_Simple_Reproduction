def max_profit(price, k):
    n = len(price)
    if n == 0:
        return 0

    # Initialize dp array
    dp = [[0 for _ in range(2)] for _ in range(k + 1)]

    for transaction in range(1, k + 1):
        max_diff = -price[0]
        for day in range(1, n):
            # Update profit if selling on the current day
            dp[transaction][0] = max(dp[transaction][0], dp[transaction - 1][1] + price[day])
            # Update profit if buying on the current day
            dp[transaction][1] = max(dp[transaction][1], dp[transaction - 1][0] + max_diff)
            # Update the maximum difference for buying stock
            max_diff = max(max_diff, dp[transaction - 1][0] - price[day])

    # The maximum profit is the profit from the last transaction without holding any stock
    return dp[k][0]