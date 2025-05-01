import cmath

def convert(numbers):
    polar_coords = []
    for num in numbers:
        magnitude = abs(num)
        phase_angle = cmath.phase(num)
        polar_coords.append((magnitude, phase_angle))
    return polar_coords