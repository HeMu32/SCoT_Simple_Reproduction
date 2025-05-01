import cmath

def convert(numbers):
    """
    Write a python function to convert complex numbers to polar coordinates.
    """
    polar_coords = [cmath.polar(num) for num in numbers]
    return polar_coords