def check_monthnumber(monthname3):
    # Convert the month name to lowercase
    monthname3 = monthname3.lower()
    
    # List of months with 30 days
    thirty_days_months = ['april', 'june', 'september', 'november']
    
    # Check if the month is in the list of 30-day months
    if monthname3 in thirty_days_months:
        return True
    else:
        return False