import cmath

def angle_complex(a, b):
    # Create a complex number
    complex_num = complex(a, b)
    # Calculate the angle of the complex number
    angle = cmath.phase(complex_num)
    # Return the angle
    return angle