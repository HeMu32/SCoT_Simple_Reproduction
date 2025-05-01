import re

def split_lowerstring(text): 
    """ 
    Write a function to split a string at lowercase letters. 
    """ 
    return re.split('([a-z])', text)

# Example usage:
# result = split_lowerstring("HelloWorld")
# print(result)  # Output: ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']