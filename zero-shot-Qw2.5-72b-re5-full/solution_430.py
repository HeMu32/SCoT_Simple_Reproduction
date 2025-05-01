def parabola_directrix(a, b, c):
    """
    Write a function to find the directrix of a parabola.
    """
    directrix = c - (b**2 - 1) / (4 * a)
    return directrix