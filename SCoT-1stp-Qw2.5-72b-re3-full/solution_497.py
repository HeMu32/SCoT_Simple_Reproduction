import math

def surfacearea_cone(r, h):
    # Calculate the slant height of the cone
    l = math.sqrt(r**2 + h**2)
    
    # Calculate the surface area of the cone
    surface_area = math.pi * r * (r + l)
    
    return surface_area