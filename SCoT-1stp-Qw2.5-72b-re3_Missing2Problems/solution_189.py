def first_Missing_Positive(arr, n):
    i = 0
    while i < n:
        correct_pos = arr[i] - 1
        if 1 <= arr[i] <= n and arr[i] != arr[correct_pos]:
            arr[i], arr[correct_pos] = arr[correct_pos], arr[i]
        else:
            i += 1
    
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    
    return n + 1