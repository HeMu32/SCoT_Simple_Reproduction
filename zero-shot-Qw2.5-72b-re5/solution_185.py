def parabola_focus(a, b, c): 
    """ 
    Write a function to find the focus of a parabola. 
    """
    x = -b / (2 * a)
    y = (1 - (b**2 - 4 * a * c)) / (4 * a)
    return (x, y)