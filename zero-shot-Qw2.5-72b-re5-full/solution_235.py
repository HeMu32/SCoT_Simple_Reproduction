def even_bit_set_number(n):
    """
    Write a python function to set all even bits of a given number.
    """
    if n == 0:
        return 0
    mask = 0xAAAAAAAA  # Binary: 10101010101010101010101010101010
    return n | mask