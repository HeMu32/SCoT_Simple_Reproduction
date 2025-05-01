def parabola_focus(a, b, c):
    # Calculate the x-coordinate of the vertex
    x_vertex = -b / (2 * a)
    
    # Calculate the y-coordinate of the vertex
    y_vertex = c - b**2 / (4 * a)
    
    # Calculate the distance from the vertex to the focus
    distance = 1 / (4 * a)
    
    # Calculate the y-coordinate of the focus
    y_focus = y_vertex + distance
    
    # Return the focus as a tuple
    return (x_vertex, y_focus)