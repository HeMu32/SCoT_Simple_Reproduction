def max_volume(s):
    """
    Write a python function to find the maximum volume of a cuboid with given sum of sides.
    """
    if s < 3:
        return 0
    a = s // 3
    b = (s - a) // 2
    c = s - a - b
    return a * b * c