import math

def calculate_polygons(startx, starty, endx, endy, radius):
    # Calculate the side length of the hexagon
    side_length = radius * math.sqrt(3)
    
    # Calculate the horizontal and vertical step sizes
    horizontal_step = 1.5 * side_length
    vertical_step = math.sqrt(3) * radius
    
    # Initialize the list to store hexagon coordinates
    hexagons = []
    
    # Loop through the grid
    for y in range(starty, endy, int(vertical_step)):
        for x in range(startx, endx, int(horizontal_step)):
            # Calculate the coordinates of the hexagon's vertices
            hexagon = [
                (x, y + radius),
                (x + 0.5 * side_length, y + 1.5 * radius),
                (x + 1.5 * side_length, y + 1.5 * radius),
                (x + 2 * side_length, y + radius),
                (x + 1.5 * side_length, y - 0.5 * radius),
                (x + 0.5 * side_length, y - 0.5 * radius)
            ]
            # Append the hexagon to the list
            hexagons.append(hexagon)
    
    return hexagons