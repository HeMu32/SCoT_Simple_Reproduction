def all_Bits_Set_In_The_Given_Range(n, l, r):
    # Generate a mask with bits set in the range [l, r]
    mask = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
    
    # Perform a bitwise AND between n and the mask
    result = n & mask
    
    # If the result is 0, all bits in the range [l, r] are unset
    return result == 0