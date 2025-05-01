def max_sum(arr, n):
    # Initialize inc and dec arrays
    inc = [0] * n
    dec = [0] * n
    
    # Initialize the first element of inc
    inc[0] = arr[0]
    
    # Fill inc array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]
        if inc[i] == 0:
            inc[i] = arr[i]
    
    # Initialize the last element of dec
    dec[n - 1] = arr[n - 1]
    
    # Fill dec array
    for i in range(n - 2, -1, -1):
        for j in range(i + 1, n):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]
        if dec[i] == 0:
            dec[i] = arr[i]
    
    # Calculate the maximum sum of bi-tonic sub-sequence
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])
    
    return max_sum