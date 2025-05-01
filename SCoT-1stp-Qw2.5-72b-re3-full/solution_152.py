def merge_sort(x):
    # Base case: if the list is of length 0 or 1, it is already sorted
    if len(x) <= 1:
        return x
    
    # Divide the list into two halves
    mid = len(x) // 2
    left = x[:mid]
    right = x[mid:]
    
    # Recursively sort both halves
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge the two lists while there are elements in both
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append any remaining elements from the left list
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Append any remaining elements from the right list
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged