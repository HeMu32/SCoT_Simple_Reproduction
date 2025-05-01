def diameter_circle(r):
    """ 
    Write a function to find the diameter of a circle. 
    """
    if r > 0:
        d = 2 * r
        return d
    else:
        raise ValueError("Radius must be a positive number")