def area_polygon(s, l): 
    """ 
    Write a function to calculate the area of a regular polygon. 
    """
    import math
    area = (s * l ** 2) / (4 * math.tan(math.pi / s))
    return area