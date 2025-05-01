def check_monthnum(monthname1):
    # List of months that can have 28 days (only February)
    months_with_28_days = ["February"]
    
    # Check if the input month name is in the list
    if monthname1 in months_with_28_days:
        return True
    else:
        return False