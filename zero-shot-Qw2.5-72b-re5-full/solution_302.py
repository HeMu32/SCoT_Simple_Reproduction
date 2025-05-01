def set_Bit_Number(n):
    if n == 0:
        return 0
    msb = 1
    while (n > 1):
        n >>= 1
        msb <<= 1
    return msb