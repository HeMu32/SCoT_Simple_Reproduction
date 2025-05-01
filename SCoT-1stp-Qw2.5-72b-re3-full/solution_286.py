def max_sub_array_sum_repeated(a, n, k):
    import sys
    max_sum = -sys.maxsize
    current_sum = 0
    prefix_sum = 0
    max_prefix_sum = 0
    suffix_sum = 0
    max_suffix_sum = 0
    
    # Calculate the maximum subarray sum for a single array
    for i in range(n):
        current_sum += a[i]
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0
        prefix_sum += a[i]
        max_prefix_sum = max(max_prefix_sum, prefix_sum)
    
    # Calculate the maximum suffix sum for a single array
    for i in range(n-1, -1, -1):
        suffix_sum += a[i]
        max_suffix_sum = max(max_suffix_sum, suffix_sum)
    
    # If k > 1, consider the case where the array is repeated
    if k > 1:
        total_sum = sum(a)
        if total_sum > 0:
            max_sum = max(max_sum, max_prefix_sum + (k-2) * total_sum + max_suffix_sum)
    
    return max_sum