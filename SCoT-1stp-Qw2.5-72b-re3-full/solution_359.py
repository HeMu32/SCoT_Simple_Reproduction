import math

def Check_Solution(a, b, c):
    # Calculate the discriminant
    D = b**2 - 4*a*c
    
    # Check if the discriminant is negative (no real roots)
    if D < 0:
        return False
    
    # Calculate the roots
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    
    # Check if one root is twice the other
    if root1 == 2 * root2 or root2 == 2 * root1:
        return True
    else:
        return False