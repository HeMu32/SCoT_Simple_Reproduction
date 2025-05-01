import math

def largest_triangle(a, b):
    # Calculate the area of the largest triangle inscribed in the ellipse
    area = (3 * math.sqrt(3) * a * b) / 4
    return area