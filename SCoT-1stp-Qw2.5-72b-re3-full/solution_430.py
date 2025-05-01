def parabola_directrix(a, b, c):
    # Calculate the x-coordinate of the vertex
    h = -b / (2 * a)
    # Calculate the y-coordinate of the vertex
    k = c - (b**2 - 1) / (4 * a)
    # Calculate the y-coordinate of the directrix
    directrix = k - 1 / (4 * a)
    # Return the y-coordinate of the directrix
    return directrix