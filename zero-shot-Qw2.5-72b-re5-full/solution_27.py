def remove(lst): 
    """ 
    Write a python function to remove all digits from a list of strings. 
    """ 
    return [''.join(filter(lambda x: not x.isdigit(), s)) for s in lst]