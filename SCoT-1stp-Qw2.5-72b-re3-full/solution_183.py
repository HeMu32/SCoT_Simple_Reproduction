def count_pairs(arr, n, k):
    count = 0
    elements = set(arr)  # Convert list to set to remove duplicates and for O(1) look-up times.
    
    for x in elements:
        if (x + k) in elements:
            count += 1
    
    return count