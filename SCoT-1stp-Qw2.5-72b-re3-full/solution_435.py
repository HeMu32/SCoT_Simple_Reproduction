def last_Digit(number):
    # Convert the number to a string
    num_str = str(number)
    
    # Check if the number is a float
    if '.' in num_str:
        # Split the string at the decimal point and take the part after the decimal
        decimal_part = num_str.split('.')[1]
        # The last digit is the last character of the decimal part
        last_digit = int(decimal_part[-1])
    else:
        # The number is an integer, the last digit is the last character of the string
        last_digit = int(num_str[-1])
    
    return last_digit