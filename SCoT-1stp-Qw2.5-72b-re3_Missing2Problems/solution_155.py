def even_bit_toggle_number(num):
    mask = 0
    # Loop through each bit position
    for i in range(32):  # Assuming a 32-bit integer
        if i % 2 == 0:  # Check if the bit position is even
            mask |= (1 << i)  # Set the corresponding bit in the mask
    return num ^ mask  # Toggle the even bits using XOR

# Example usage:
result = even_bit_toggle_number(10)  # Binary 1010, toggling even bits results in 0101 (5)
print(result)  # Output: 5