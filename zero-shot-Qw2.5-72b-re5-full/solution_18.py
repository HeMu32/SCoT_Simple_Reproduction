def str_to_list(s1, s2): 
    """ 
    Write a function to remove characters from the first string which are present in the second string. 
    """ 
    result = ''.join([char for char in s1 if char not in s2])
    return result