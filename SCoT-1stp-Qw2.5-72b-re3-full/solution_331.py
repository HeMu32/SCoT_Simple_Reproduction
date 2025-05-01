def count_unset_bits(n):
    # Convert the number to its binary representation, excluding the '0b' prefix
    binary_representation = bin(n)[2:]
    # Initialize the count of unset bits
    count = 0
    # Loop through each bit in the binary representation
    for bit in binary_representation:
        # If the bit is '0', increment the count
        if bit == '0':
            count += 1
    # Return the count of unset bits
    return count