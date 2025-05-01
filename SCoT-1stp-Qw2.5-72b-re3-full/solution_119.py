def search(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if the middle element is the unique element
        if (mid == 0 or arr[mid] != arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] != arr[mid + 1]):
            return arr[mid]
        
        # Determine which side to search
        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            left = mid + 1
        else:
            right = mid
    
    # The unique element is at the left pointer
    return arr[left]