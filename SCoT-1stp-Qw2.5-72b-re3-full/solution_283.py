def validate(n):
    # Convert the integer to a string to iterate over each digit
    str_n = str(n)
    
    # Initialize a dictionary to store the frequency of each digit
    digit_freq = {}
    
    # Count the frequency of each digit
    for char in str_n:
        digit = int(char)
        if digit not in digit_freq:
            digit_freq[digit] = 1
        else:
            digit_freq[digit] += 1
    
    # Check if the frequency of each digit is less than or equal to the digit itself
    for digit in digit_freq:
        if digit_freq[digit] > digit:
            return False
    
    return True