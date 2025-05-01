def binary_search(item_list, item):
    low = 0
    high = len(item_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if item_list[mid] == item:
            return mid
        elif item_list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1