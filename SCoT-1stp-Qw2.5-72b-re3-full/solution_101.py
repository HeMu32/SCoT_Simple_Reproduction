def kth_element(arr, n, k):
    # Check if k is within the valid range
    if k < 1 or k > n:
        raise ValueError("k is out of bounds")
    # Return the (k-1)th element of the array
    return arr[k-1]