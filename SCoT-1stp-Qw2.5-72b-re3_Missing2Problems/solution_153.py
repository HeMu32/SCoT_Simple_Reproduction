def parabola_vertex(a, b, c):
    # Calculate the x-coordinate of the vertex
    x = -b / (2 * a)
    # Calculate the y-coordinate of the vertex
    y = a * x**2 + b * x + c
    # Return the vertex as a tuple
    return (x, y)