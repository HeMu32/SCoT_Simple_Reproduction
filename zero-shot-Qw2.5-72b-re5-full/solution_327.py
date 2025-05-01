def check_isosceles(x, y, z):
    if x == y or y == z or x == z:
        print("The triangle is isosceles.")
    else:
        print("The triangle is not isosceles.")