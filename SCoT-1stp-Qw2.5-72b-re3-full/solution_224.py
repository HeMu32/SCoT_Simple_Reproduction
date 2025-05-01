def count_Set_Bits(n):
    count = 0
    while n > 0:
        if n & 1:  # Check if the last bit is 1
            count += 1
        n >>= 1  # Right shift n by 1 bit
    return count