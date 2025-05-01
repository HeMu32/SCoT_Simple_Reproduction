def count_Hexadecimal(start, end):
    """
    Write a python function to count hexadecimal numbers for a given range.
    """
    count = 0
    for num in range(start, end + 1):
        hex_num = hex(num)[2:]  # Convert to hex and remove the '0x' prefix
        if all(c in '0123456789abcdefABCDEF' for c in hex_num):
            count += 1
    return count