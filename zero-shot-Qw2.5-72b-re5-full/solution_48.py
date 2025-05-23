def odd_bit_set_number(n):
    """
    Write a python function to set all odd bits of a given number.
    """
    if n == 0:
        return 0
    
    result = 0
    bit_position = 0
    
    while n > 0:
        if bit_position % 2 == 0:
            result |= (1 << bit_position)
        n >>= 1
        bit_position += 1
    
    return result