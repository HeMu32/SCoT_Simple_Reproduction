def first_Digit(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Check if the number is negative
    if num_str[0] == '-':
        # Return the first digit, skipping the negative sign
        return int(num_str[1])
    else:
        # Return the first digit
        return int(num_str[0])