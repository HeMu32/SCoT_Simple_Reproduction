import math

def largest_triangle(a, b):
    """
    Write a function to find the largest triangle that can be inscribed in an ellipse.
    """
    # The largest triangle inscribed in an ellipse is an equilateral triangle
    # with its centroid at the center of the ellipse.
    # The area of this triangle is given by the formula:
    # Area = (3 * sqrt(3) * a * b) / 4
    area = (3 * math.sqrt(3) * a * b) / 4
    return area