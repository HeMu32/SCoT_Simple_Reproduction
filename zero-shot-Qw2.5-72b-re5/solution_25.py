def find_Product(arr, n): 
    product = 1
    seen = set()
    for i in range(n):
        if arr[i] not in seen:
            product *= arr[i]
            seen.add(arr[i])
    return product