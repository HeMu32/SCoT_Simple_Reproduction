def perimeter_triangle(a, b, c):
    # Check if the inputs are valid
    if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
        # Calculate the perimeter
        perimeter = a + b + c
        return perimeter
    else:
        # Return an error message if the inputs do not form a valid triangle
        return "Invalid input: The sides do not form a valid triangle."