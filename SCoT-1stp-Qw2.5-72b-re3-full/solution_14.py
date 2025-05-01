def find_Volume(base, height, length):
    # Calculate the area of the triangular base
    base_area = (base * height) / 2
    
    # Calculate the volume of the triangular prism
    volume = base_area * length
    
    # Return the calculated volume
    return volume