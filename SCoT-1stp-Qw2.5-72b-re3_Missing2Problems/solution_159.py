def month_season(month, days):
    # Convert month to lowercase to ensure case insensitivity
    month = month.lower()
    
    # Initialize season as an empty string
    season = ""
    
    # Determine the season based on the month and day
    if month in ["january", "february"]:
        season = "Winter"
    elif month == "march":
        if days < 20:
            season = "Winter"
        else:
            season = "Spring"
    elif month in ["april", "may"]:
        season = "Spring"
    elif month == "june":
        if days < 21:
            season = "Spring"
        else:
            season = "Summer"
    elif month in ["july", "august"]:
        season = "Summer"
    elif month == "september":
        if days < 22:
            season = "Summer"
        else:
            season = "Fall"
    elif month in ["october", "november"]:
        season = "Fall"
    elif month == "december":
        if days < 21:
            season = "Fall"
        else:
            season = "Winter"
    
    # Return the determined season
    return season