def find_lists(Input):
    """
    Write a function to find number of lists present in the given tuple.
    """
    def count_lists(item):
        if isinstance(item, list):
            return 1 + sum(count_lists(sub_item) for sub_item in item)
        elif isinstance(item, tuple):
            return sum(count_lists(sub_item) for sub_item in item)
        return 0
    
    return count_lists(Input)