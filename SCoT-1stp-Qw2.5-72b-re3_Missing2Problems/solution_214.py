import math

def degree_radian(radian):
    # Define the conversion factor
    conversion_factor = 180 / math.pi
    
    # Convert radian to degree
    degree = radian * conversion_factor
    
    # Return the degree value
    return degree