def adjacent_num_product(list_nums):
    # Initialize max_product with the product of the first two elements
    max_product = list_nums[0] * list_nums[1]
    
    # Iterate through the list starting from the second element
    for i in range(1, len(list_nums) - 1):
        # Calculate the product of the current element and the next element
        product = list_nums[i] * list_nums[i + 1]
        
        # Update max_product if the current product is greater
        if product > max_product:
            max_product = product
    
    # Return the maximum product found
    return max_product