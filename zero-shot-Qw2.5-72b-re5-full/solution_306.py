def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    for i in range(n):
        dp[i] = a[i]
        for j in range(i):
            if a[j] < a[i] and dp[j] + a[i] > dp[i]:
                dp[i] = dp[j] + a[i]
    
    # Ensure the kth element is included in the subsequence
    max_sum = 0
    for i in range(index + 1):
        if a[i] < a[k]:
            max_sum = max(max_sum, dp[i])
    
    return max_sum + a[k]