def max_profit(price, k):
    n = len(price)
    if n == 0:
        return 0

    # If k is greater than or equal to n/2, then we can make maximum n/2 transactions
    if k >= n // 2:
        max_prof = 0
        for i in range(1, n):
            if price[i] > price[i - 1]:
                max_prof += price[i] - price[i - 1]
        return max_prof

    # Initialize the profit table
    profit = [[0 for _ in range(k + 1)] for _ in range(n)]

    for i in range(1, n):
        for j in range(1, k + 1):
            max_so_far = 0
            for m in range(i):
                max_so_far = max(max_so_far, price[i] - price[m] + profit[m][j - 1])
            profit[i][j] = max(profit[i - 1][j], max_so_far)

    return profit[n - 1][k]