def sub_list(nums1, nums2):
    """
    Write a function to subtract two lists using map and lambda function.
    """
    return list(map(lambda x, y: x - y, nums1, nums2))