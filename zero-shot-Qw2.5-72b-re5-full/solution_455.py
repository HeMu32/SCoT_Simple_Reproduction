def check_monthnumb_number(monthnum2):
    """
    Write a function to check whether the given month number contains 31 days or not.
    """
    if monthnum2 in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False