def large_product(nums1, nums2, N):
    # Initialize an empty list to store the products
    products = []
    
    # Compute the product of each pair of elements from nums1 and nums2
    for x in nums1:
        for y in nums2:
            products.append(x * y)
    
    # Sort the products in descending order
    products.sort(reverse=True)
    
    # Return the first N elements from the sorted list
    return products[:N]