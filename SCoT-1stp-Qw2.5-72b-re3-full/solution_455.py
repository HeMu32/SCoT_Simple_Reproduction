def check_monthnumb_number(monthnum2):
    # List of months with 31 days
    months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    
    # Check if the given month number is in the list
    if monthnum2 in months_with_31_days:
        return True
    else:
        return False