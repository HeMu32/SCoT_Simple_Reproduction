def remove_even(str1): 
    """ 
    Write a function to remove even characters in a string. 
    """ 
    return ''.join([str1[i] for i in range(len(str1)) if i % 2 != 0])