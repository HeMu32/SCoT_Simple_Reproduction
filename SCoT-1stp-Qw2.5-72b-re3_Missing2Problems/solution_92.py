def is_undulating(n):
    # Convert the integer to a string
    s = str(n)
    
    # Check if the length of the string is less than 3
    if len(s) < 3:
        return False
    
    # Initialize the first and second digits
    a = s[0]
    b = s[1]
    
    # Check if the first and second digits are the same
    if a == b:
        return False
    
    # Iterate through the string from the third digit to the end
    for i in range(2, len(s)):
        if i % 2 == 0 and s[i] != a:
            return False
        if i % 2 == 1 and s[i] != b:
            return False
    
    # If all checks pass, the number is undulating
    return True