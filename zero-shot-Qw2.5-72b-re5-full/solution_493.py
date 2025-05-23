import math

def calculate_polygons(startx, starty, endx, endy, radius):
    def hexagon_coords(x, y, radius):
        angles = [60 * i for i in range(6)]
        return [(x + radius * math.cos(math.radians(angle)), y + radius * math.sin(math.radians(angle))) for angle in angles]

    hexagons = []
    horizontal_distance = radius * 2
    vertical_distance = math.sqrt(3) * radius
    offset = radius * math.sqrt(3) / 2

    for i in range(starty, endy, int(vertical_distance)):
        for j in range(startx, endx, int(horizontal_distance)):
            if i % int(2 * offset) == 0:
                hexagons.append(hexagon_coords(j, i, radius))
            else:
                hexagons.append(hexagon_coords(j + radius, i, radius))

    return hexagons