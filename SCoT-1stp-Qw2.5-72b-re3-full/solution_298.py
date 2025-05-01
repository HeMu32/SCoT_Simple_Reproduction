def intersection_nested_lists(l1, l2):
    def flatten(lst):
        """Flatten a nested list into a single list."""
        flat_list = []
        for item in lst:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    result = []
    flat_l1 = flatten(l1)
    for e in flat_l1:
        if e in l2 and e not in result:
            result.append(e)
    return result