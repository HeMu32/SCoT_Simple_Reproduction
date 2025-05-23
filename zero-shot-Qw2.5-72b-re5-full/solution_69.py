def is_sublist(l, s):
    """ 
    Write a function to check whether a list contains the given sublist or not. 
    """ 
    if not s:  # An empty sublist is always a sublist
        return True
    if not l:  # A non-empty sublist cannot be found in an empty list
        return False

    for i in range(len(l) - len(s) + 1):
        if l[i:i+len(s)] == s:
            return True
    return False