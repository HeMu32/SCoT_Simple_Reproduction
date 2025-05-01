def find_exponentio(test_tup1, test_tup2):
    """
    Write a function to perform the exponentiation of the given two tuples.
    """
    if len(test_tup1) != len(test_tup2):
        raise ValueError("Tuples must be of the same length")
    
    result = tuple(x ** y for x, y in zip(test_tup1, test_tup2))
    return result