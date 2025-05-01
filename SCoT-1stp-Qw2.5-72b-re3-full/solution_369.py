def lateralsurface_cuboid(l, w, h):
    # Calculate the perimeter of the base
    perimeter = 2 * (l + w)
    # Calculate the lateral surface area
    lateral_surface_area = perimeter * h
    # Return the lateral surface area
    return lateral_surface_area