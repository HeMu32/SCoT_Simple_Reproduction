def find_star_num(n):
    """
    Write a function to find the n'th star number.
    """
    # Calculate the n-th star number using the formula
    star_number = 6 * n * (n - 1) + 1
    return star_number