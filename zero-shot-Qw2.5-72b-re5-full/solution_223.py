def is_majority(arr, n, x):
    first_occurrence = -1
    last_occurrence = -1
    
    # Find the first occurrence of x
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first_occurrence = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    # Find the last occurrence of x
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last_occurrence = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    
    # Check if the element x is a majority element
    if first_occurrence != -1 and last_occurrence != -1:
        count = last_occurrence - first_occurrence + 1
        return count > n // 2
    return False