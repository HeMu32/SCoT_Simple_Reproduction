def ascii_value_string(str1): 
    """
    Write a function to find the ascii value of total characters in a string. 
    """ 
    return sum(ord(char) for char in str1)