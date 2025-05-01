def check_last(arr, n, p):
    # Initialize the last element
    last_element = arr[-1]
    
    # Perform the operation p times
    for _ in range(p):
        for i in range(n):
            arr[i] += 1
    
    # Update the last element after p operations
    last_element = arr[-1]
    
    # Check if the last element is even
    return last_element % 2 == 0