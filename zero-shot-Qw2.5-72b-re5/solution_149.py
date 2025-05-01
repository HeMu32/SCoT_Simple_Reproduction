def longest_subseq_with_diff_one(arr, n):
    dp = [1] * n  # Initialize the dp array with 1 as the minimum length of subsequence is 1 (the element itself)
    
    # Sort the array to ensure that we can find the longest subsequence with difference one
    arr.sort()
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] - arr[j] == 1:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The length of the longest subsequence with difference one
    return max(dp)