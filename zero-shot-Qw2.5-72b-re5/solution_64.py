def subject_marks(subjectmarks): 
    """
    Write a function to sort a list of tuples using lambda. 
    """ 
    return sorted(subjectmarks, key=lambda x: x[1])