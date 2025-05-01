def count_Hexadecimal(start, end):
    count = 0
    for num in range(start, end + 1):
        hex_str = hex(num)[2:]  # Convert number to hexadecimal and remove the '0x' prefix
        if any(char in hex_str.upper() for char in 'ABCDEF'):
            count += 1
    return count