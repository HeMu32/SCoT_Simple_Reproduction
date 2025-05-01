import math

def surfacearea_cone(r, h):
    """
    Write a function to find the surface area of a cone.
    """
    l = math.sqrt(r**2 + h**2)
    surface_area = math.pi * r * (r + l)
    return surface_area