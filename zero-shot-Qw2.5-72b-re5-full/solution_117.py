def list_to_float(test_list):
    """
    Write a function to convert all possible convertible elements in the list to float.
    """
    def convert_to_float(element):
        try:
            return float(element)
        except ValueError:
            return element

    return [convert_to_float(item) for item in test_list]