def insert_element(lst, element): 
    """ 
    Write a function to insert an element before each element of a list. 
    """ 
    result = []
    for item in lst:
        result.append(element)
        result.append(item)
    return result