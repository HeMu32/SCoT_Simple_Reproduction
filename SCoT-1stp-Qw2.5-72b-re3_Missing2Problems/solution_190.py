def count_Intgral_Points(x1, y1, x2, y2):
    # Calculate the side length of the square
    side_length = abs(x2 - x1)
    
    # If the side length is less than or equal to 1, there are no points strictly inside the square
    if side_length <= 1:
        return 0
    
    # Calculate the number of integral points inside the square
    count = (side_length - 1) ** 2
    
    return count