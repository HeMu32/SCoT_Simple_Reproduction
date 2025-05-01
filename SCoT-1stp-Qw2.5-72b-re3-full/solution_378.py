def move_first(test_list):
    if len(test_list) <= 1:
        return test_list
    else:
        last_element = test_list[-1]
        test_list.pop()
        test_list.insert(0, last_element)
        return test_list