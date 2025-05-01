def test_duplicate(arraynums):
    # Create a set from the list to remove duplicates
    unique_nums = set(arraynums)
    
    # Compare the length of the original list with the set
    if len(arraynums) != len(unique_nums):
        return True  # Duplicates are present
    else:
        return False  # No duplicates