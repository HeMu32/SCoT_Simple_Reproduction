def large_product(nums1, nums2, N):
    products = []
    for num1 in nums1:
        for num2 in nums2:
            products.append(num1 * num2)
    products.sort(reverse=True)
    return products[:N]