def sum_digits_twoparts(num):
    # Convert the number to a string to iterate over each digit
    num_str = str(num)
    
    # Initialize two parts as empty strings
    part1 = ""
    part2 = ""
    
    # Initialize the sum of digits for each part
    sum1 = 0
    sum2 = 0
    
    # Iterate over each digit in the string representation of the number
    for digit in num_str:
        digit_int = int(digit)
        
        # Decide which part to add the digit to based on the current sums
        if sum1 <= sum2:
            part1 += digit
            sum1 += digit_int
        else:
            part2 += digit
            sum2 += digit_int
    
    # Convert part1 and part2 back to integers
    part1 = int(part1) if part1 else 0
    part2 = int(part2) if part2 else 0
    
    # Return the tuple of the two parts
    return (part1, part2)