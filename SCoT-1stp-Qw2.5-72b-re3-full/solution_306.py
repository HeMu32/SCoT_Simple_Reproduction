def max_sum_increasing_subseq(a, n, index, k):
    dp = [0] * n
    dp[k] = a[k]
    
    for i in range(index + 1):
        if i < k:
            for j in range(i):
                if a[j] < a[i]:
                    dp[i] = max(dp[i], dp[j] + a[i])
        elif i == k:
            continue
        else:
            break
    
    return dp[k]