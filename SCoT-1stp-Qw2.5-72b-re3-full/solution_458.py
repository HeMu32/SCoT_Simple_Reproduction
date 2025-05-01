def rectangle_area(l, b):
    # Check if the inputs are valid (positive numbers)
    if l <= 0 or b <= 0:
        return -1  # Return -1 if either length or breadth is not positive
    
    # Calculate the area of the rectangle
    area = l * b
    
    # Return the calculated area
    return area