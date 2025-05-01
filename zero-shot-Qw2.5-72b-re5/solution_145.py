def max_Abs_Diff(arr, n):
    if n < 2:
        return 0
    min_element = arr[0]
    max_diff = arr[1] - arr[0]
    for i in range(1, n):
        if arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff