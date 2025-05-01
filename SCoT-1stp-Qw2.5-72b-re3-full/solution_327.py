def check_isosceles(x, y, z):
    # Check if any two sides of the triangle are equal
    if x == y or y == z or x == z:
        return "The triangle is isosceles."
    else:
        return "The triangle is not isosceles."