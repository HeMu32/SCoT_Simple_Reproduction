def odd_Days(N):
    # Initialize the number of odd days
    odd_days = 0
    
    # Check if the year is a leap year
    if (N % 400 == 0) or (N % 4 == 0 and N % 100 != 0):
        days_in_year = 366
    else:
        days_in_year = 365
    
    # Calculate the number of odd days
    odd_days = days_in_year % 7
    
    # Return the number of odd days
    return odd_days