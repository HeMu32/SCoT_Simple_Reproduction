def intersection_array(array_nums1, array_nums2):
    # Use filter and lambda to find common elements
    result = list(filter(lambda x: x in array_nums2, array_nums1))
    return result