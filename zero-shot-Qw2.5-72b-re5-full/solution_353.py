def remove_column(list1, n): 
    """ 
    Write a function to remove a specified column from a given nested list. 
    """ 
    return [row[:n] + row[n+1:] for row in list1]