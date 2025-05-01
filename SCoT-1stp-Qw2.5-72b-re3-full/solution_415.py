def max_Product(arr):
    # Check if the array has less than 2 elements
    if len(arr) < 2:
        return None
    
    # Initialize variables to store the maximum product and the pair
    max_product = arr[0] * arr[1]
    max_pair = (arr[0], arr[1])
    
    # Iterate through the array to find the pair with the highest product
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_pair = (arr[i], arr[j])
    
    # Return the pair with the highest product
    return max_pair