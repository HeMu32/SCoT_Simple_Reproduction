def min_Ops(arr, n, k):
    # If the array is empty or has only one element, no operations are needed
    if n <= 1:
        return 0
    
    # Sort the array to find the median
    arr.sort()
    
    # The median is the middle element in the sorted array
    median = arr[n // 2]
    
    # Calculate the total number of operations required to make all elements equal to the median
    total_ops = sum(abs(median - x) for x in arr)
    
    # If the total number of operations is less than or equal to k, return the total number of operations
    if total_ops <= k:
        return total_ops
    else:
        # Otherwise, return -1 as it's not possible to make all elements equal with the given number of operations
        return -1