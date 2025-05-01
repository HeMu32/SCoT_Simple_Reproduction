def find_missing(ar, N):
    low = 0
    high = N - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if ar[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    
    return low + 1