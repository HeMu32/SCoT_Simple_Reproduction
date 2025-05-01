def binary_to_integer(test_tup):
    # Convert the tuple to a string
    binary_str = ''.join(str(x) for x in test_tup)
    # Convert the binary string to an integer
    result = int(binary_str, 2)
    # Return the integer
    return result