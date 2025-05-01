def flatten(nested_list):
    """Flatten a nested list into a single list."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def check_subset_list(list1, list2):
    """Check if a nested list is a subset of another nested list."""
    flat_list1 = flatten(list1)
    flat_list2 = flatten(list2)
    
    set1 = set(flat_list1)
    set2 = set(flat_list2)
    
    return set1.issubset(set2)