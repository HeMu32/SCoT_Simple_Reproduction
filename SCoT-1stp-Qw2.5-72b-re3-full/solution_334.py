def check_validity(a, b, c):
    # Check if any side is less than or equal to 0
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Check the triangle inequality theorem
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False