def max_sub_array_sum_repeated(a, n, k):
    def kadane(arr):
        max_end_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_end_here = max(x, max_end_here + x)
            max_so_far = max(max_so_far, max_end_here)
        return max_so_far

    if k == 1:
        return kadane(a)
    
    prefix_sum = [0] * n
    suffix_sum = [0] * n
    prefix_sum[0] = a[0]
    suffix_sum[-1] = a[-1]
    
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + a[i]
        suffix_sum[-i - 1] = suffix_sum[-i] + a[-i - 1]
    
    max_kadane = kadane(a)
    max_prefix_sum = max(prefix_sum)
    max_suffix_sum = max(suffix_sum)
    total_sum = prefix_sum[-1]
    
    if total_sum < 0:
        return max(max_kadane, max_prefix_sum + max_suffix_sum)
    else:
        return max(max_kadane, max_prefix_sum + max_suffix_sum + (k - 2) * total_sum)