def Sort(sub_li): 
    """ 
    Write a python function to sort a list according to the second element in sublist. 
    """ 
    return sorted(sub_li, key=lambda x: x[1])