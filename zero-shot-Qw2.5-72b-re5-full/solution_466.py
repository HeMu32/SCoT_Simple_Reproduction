def find_peak_util(arr, low, high, n): 
    mid = low + (high - low) // 2

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
        (mid == n - 1 or arr[mid + 1] <= arr[mid])):
        return mid
    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return find_peak_util(arr, low, mid - 1, n)
    else:
        return find_peak_util(arr, mid + 1, high, n)