import math

def perimeter(r, h):
    # Check if the radius and height are positive
    if r <= 0 or h <= 0:
        return -1  # Indicating an invalid input
    else:
        # Calculate the perimeter using the formula: 2 * (2 * π * r + h)
        perimeter = 2 * (2 * math.pi * r + h)
        return perimeter