def moddiv_list(nums1, nums2):
    # Check if the lengths of the lists are equal
    if len(nums1) != len(nums2):
        raise ValueError("Both lists must have the same length.")
    
    # Use map and lambda to apply modulo division to corresponding elements
    result = list(map(lambda x, y: x % y, nums1, nums2))
    
    return result