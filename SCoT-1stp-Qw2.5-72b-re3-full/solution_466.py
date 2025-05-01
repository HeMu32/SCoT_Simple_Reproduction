def find_peak(arr, n):
    # Check if the array is empty or has only one element
    if n == 1:
        return 0
    # Check if the first element is a peak
    if arr[0] >= arr[1]:
        return 0
    # Check if the last element is a peak
    if arr[n-1] >= arr[n-2]:
        return n-1
    # Iterate through the array to find a peak
    for i in range(1, n-1):
        if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]:
            return i
    # If no peak is found
    return -1