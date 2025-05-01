def check_Triangle(x1, y1, x2, y2, x3, y3):
    # Function to calculate the distance between two points
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Calculate the lengths of the sides of the potential triangle
    side1 = distance(x1, y1, x2, y2)
    side2 = distance(x2, y2, x3, y3)
    side3 = distance(x3, y3, x1, y1)

    # Check the Triangle Inequality Theorem
    if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
        return True
    else:
        return False