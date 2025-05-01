def list_to_float(test_list):
    result = []
    for item in test_list:
        try:
            converted_item = float(item)
            result.append(converted_item)
        except ValueError:
            result.append(item)
    return result