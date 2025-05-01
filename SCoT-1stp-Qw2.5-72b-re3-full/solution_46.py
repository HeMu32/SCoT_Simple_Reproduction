def test_distinct(data):
    # Convert the list to a set to remove duplicates
    unique_data = set(data)
    
    # Compare the lengths
    if len(data) == len(unique_data):
        return True
    else:
        return False