def binary_to_decimal(binary):
    decimal = 0
    power = 0
    # Reverse the binary string to process from the least significant bit
    binary = binary[::-1]
    for bit in binary:
        if bit == '1':
            decimal += 2 ** power
        power += 1
    return decimal