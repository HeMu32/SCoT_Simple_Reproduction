def sub_list(nums1, nums2):
    # Use map and a lambda function to subtract elements of nums2 from nums1
    result = map(lambda x, y: x - y, nums1, nums2)
    # Convert the map object to a list and return it
    return list(result)