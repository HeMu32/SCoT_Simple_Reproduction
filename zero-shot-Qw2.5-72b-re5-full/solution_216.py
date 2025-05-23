def check_subset_list(list1, list2):
    def flatten(lst):
        for el in lst:
            if isinstance(el, list):
                yield from flatten(el)
            else:
                yield el

    flat_list1 = set(flatten(list1))
    flat_list2 = set(flatten(list2))

    return flat_list2.issubset(flat_list1)