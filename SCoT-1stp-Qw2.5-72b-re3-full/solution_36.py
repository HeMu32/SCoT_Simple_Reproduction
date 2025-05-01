def find_Nth_Digit(num1, num2, n):
    # Compute the decimal part of the fraction
    decimal_part = str(num1 / num2).split('.')[1]
    
    # Check if the length of the decimal part is less than n
    if len(decimal_part) < n:
        return "Error: n is out of range for the decimal part of the fraction."
    else:
        # Return the nth digit from the decimal part
        return int(decimal_part[n-1])