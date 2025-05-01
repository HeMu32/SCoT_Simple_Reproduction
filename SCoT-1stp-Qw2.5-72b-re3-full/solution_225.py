def find_Min(arr, low, high):
    # If the array is not rotated, the first element is the minimum
    if arr[low] <= arr[high]:
        return arr[low]
    
    min_element = arr[low]
    
    while low <= high:
        mid = (low + high) // 2
        
        # Check if mid is the minimum element
        if mid < high and arr[mid] > arr[mid + 1]:
            return arr[mid + 1]
        elif mid > low and arr[mid] < arr[mid - 1]:
            return arr[mid]
        
        # Decide the side to continue the search
        if arr[mid] > arr[low]:
            low = mid + 1
        else:
            high = mid - 1
    
    return min_element