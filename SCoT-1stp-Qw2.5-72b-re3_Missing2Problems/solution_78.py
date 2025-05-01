def count_With_Odd_SetBits(n):
    count = 0
    for i in range(1, n + 1):
        # Convert the number to binary and count the number of 1s
        num_of_set_bits = bin(i).count('1')
        # Check if the number of set bits is odd
        if num_of_set_bits % 2 != 0:
            count += 1
    return count