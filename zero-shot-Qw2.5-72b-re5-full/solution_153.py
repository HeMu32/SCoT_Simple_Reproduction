def parabola_vertex(a, b, c): 
    """ 
    Write a function to find the vertex of a parabola. 
    """ 
    x_vertex = -b / (2 * a)
    y_vertex = c - b**2 / (4 * a)
    return (x_vertex, y_vertex)