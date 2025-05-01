def check(n):
    # Convert the integer to a string
    str_n = str(n)
    
    # Reverse the string
    reversed_str_n = str_n[::-1]
    
    # Convert the reversed string back to an integer
    reversed_n = int(reversed_str_n)
    
    # Calculate twice the reversed integer and subtract one
    result = 2 * reversed_n - 1
    
    # Compare the result with the original number
    return result == n