import math

def area_polygon(s, l):
    # Calculate the apothem
    apothem = l / (2 * math.tan(math.pi / s))
    # Calculate the perimeter
    perimeter = s * l
    # Calculate the area
    area = (perimeter * apothem) / 2
    return area