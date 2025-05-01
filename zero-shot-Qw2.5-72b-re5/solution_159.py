def month_season(month, days):
    """
    Write a function to print the season for the given month and day.
    """
    if month in [12, 1, 2] or (month == 3 and days < 20) or (month == 11 and days >= 21):
        print("Winter")
    elif month in [3, 4, 5] or (month == 6 and days < 21) or (month == 2 and days >= 20):
        print("Spring")
    elif month in [6, 7, 8] or (month == 9 and days < 23) or (month == 5 and days >= 21):
        print("Summer")
    elif month in [9, 10, 11] or (month == 12 and days < 21) or (month == 8 and days >= 23):
        print("Autumn")
    else:
        print("Invalid date")