def re_arrange_array(arr, n): 
    """
    Write a function to re-arrange the elements of the given array so that all negative elements appear before positive ones.
    """
    return [x for x in arr if x < 0] + [x for x in arr if x >= 0]