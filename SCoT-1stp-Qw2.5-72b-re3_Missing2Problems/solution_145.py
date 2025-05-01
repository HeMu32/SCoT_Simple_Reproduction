def max_Abs_Diff(arr, n):
    max_diff = 0
    for i in range(n):
        for j in range(i + 1, n):
            diff = abs(arr[i] - arr[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff