def max_product(arr, n):
    # Initialize dp array with the values of arr
    dp = arr[:]
    # Initialize the result with the first element of arr
    res = arr[0]
    
    # Iterate over the array
    for j in range(1, n):
        for i in range(j):
            # Check if arr[j] is greater than arr[i]
            if arr[j] > arr[i]:
                # Update dp[j] to the maximum of dp[j] and dp[i] * arr[j]
                dp[j] = max(dp[j], dp[i] * arr[j])
            # Update res to the maximum of res and dp[j]
            res = max(res, dp[j])
    
    return res