def search(arr):
    """
    Write a python function to find the element that appears only once in a sorted array.
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        # Check if the mid is on the correct half
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            left = mid + 1
        else:
            right = mid
    return arr[left]