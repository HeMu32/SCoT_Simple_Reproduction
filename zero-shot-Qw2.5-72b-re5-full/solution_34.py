def find_missing(ar, N):
    """
    Write a python function to find the missing number in a sorted array.
    """
    low, high = 0, N - 1
    while low <= high:
        mid = (low + high) // 2
        if ar[mid] == mid:
            low = mid + 1
        else:
            high = mid - 1
    return low