def check_integer(text):
    """
    Write a function to check if a string represents an integer or not.
    """
    try:
        int(text)
        return True
    except ValueError:
        return False