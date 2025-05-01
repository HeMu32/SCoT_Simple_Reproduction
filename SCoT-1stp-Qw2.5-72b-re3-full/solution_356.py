def find_angle(a, b):
    # Check if the input angles are valid
    if a <= 0 or b <= 0 or (a + b) >= 180:
        raise ValueError("Angles must be greater than 0 and their sum must be less than 180 degrees.")
    
    # Calculate the third angle
    third_angle = 180 - (a + b)
    
    return third_angle