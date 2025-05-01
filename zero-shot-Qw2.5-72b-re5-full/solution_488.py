import math

def area_pentagon(a):
    """
    Write a function to find the area of a pentagon.
    """
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a**2
    return area