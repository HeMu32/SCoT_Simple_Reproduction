import math

def area_pentagon(a):
    # Calculate the area using the formula for a regular pentagon
    area = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a**2
    return area