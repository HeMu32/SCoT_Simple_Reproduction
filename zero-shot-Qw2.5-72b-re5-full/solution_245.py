def max_sum(arr, n):
    # Initialize two arrays to store the maximum sum of increasing and decreasing subsequence
    inc = [0] * n
    dec = [0] * n

    # Initialize the first element of inc and the last element of dec
    inc[0] = arr[0]
    dec[n - 1] = arr[n - 1]

    # Fill inc[] such that inc[i] stores the maximum sum of increasing subsequence ending at index i
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]
        if inc[i] == 0:
            inc[i] = arr[i]

    # Fill dec[] such that dec[i] stores the maximum sum of decreasing subsequence starting at index i
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]
        if dec[i] == 0:
            dec[i] = arr[i]

    # Find the maximum value of inc[i] + dec[i] - arr[i]
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum