def check_subset_list(list1, list2):
    def to_set(lst):
        if isinstance(lst, list):
            return {to_set(item) for item in lst}
        return lst

    set1 = to_set(list1)
    set2 = to_set(list2)
    
    return set1.issubset(set2) or set2.issubset(set1)