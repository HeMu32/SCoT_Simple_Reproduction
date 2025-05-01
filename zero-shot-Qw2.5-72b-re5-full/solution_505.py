def re_order(A):
    """
    Write a function to move all zeroes to the end of the given array.
    """
    non_zero = [x for x in A if x != 0]
    zeros = [x for x in A if x == 0]
    return non_zero + zeros