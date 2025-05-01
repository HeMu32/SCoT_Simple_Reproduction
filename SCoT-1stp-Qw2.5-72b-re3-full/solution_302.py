def set_Bit_Number(n):
    msb = 0
    bit_position = 0
    while n > 0:
        if n & 1:  # Check if the least significant bit is 1
            msb = 2 ** bit_position
        n = n >> 1  # Right shift n by 1 bit
        bit_position += 1
    return msb