def add_nested_tuples(test_tup1, test_tup2):
    def add_elements(t1, t2):
        if isinstance(t1, tuple) and isinstance(t2, tuple):
            return tuple(add_elements(e1, e2) for e1, e2 in zip(t1, t2))
        else:
            return t1 + t2
    return add_elements(test_tup1, test_tup2)