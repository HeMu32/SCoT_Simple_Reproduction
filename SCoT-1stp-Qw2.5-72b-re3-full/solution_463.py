def max_subarray_product(arr):
    if not arr:
        return 0

    max_product = arr[0]
    current_max = arr[0]
    current_min = arr[0]

    for num in arr[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max
        
        current_max = max(num, current_max * num)
        current_min = min(num, current_min * num)
        
        max_product = max(max_product, current_max)

    return max_product