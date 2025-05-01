import re

def split_lowerstring(text): 
    """ 
    Write a function to split a string at lowercase letters. 
    """ 
    return re.split('([a-z])', text)

# Example usage
# text = "HelloWorldThisIsATest"
# print(split_lowerstring(text))