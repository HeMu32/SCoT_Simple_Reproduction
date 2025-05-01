def longest_subseq_with_diff_one(arr, n):
    if n == 0:
        return 0  # If the array is empty, the longest subsequence is 0.
    
    max_length = 1  # Initialize the maximum length of the subsequence.
    current_length = 1  # Initialize the current length of the subsequence.
    
    for i in range(1, n):
        if abs(arr[i] - arr[i - 1]) == 1:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
        else:
            current_length = 1
    
    return max_length