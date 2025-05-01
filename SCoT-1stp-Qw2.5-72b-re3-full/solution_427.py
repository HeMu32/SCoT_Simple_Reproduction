import re

def change_date_format(dt):
    # Define the regex pattern for the date format "yyyy-mm-dd"
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    
    # Search for the pattern in the input date string
    match = re.search(pattern, dt)
    
    if match:
        # Extract the year, month, and day from the match
        year, month, day = match.groups()
        
        # Construct the new date string in the format "dd-mm-yyyy"
        new_date = f"{day}-{month}-{year}"
        
        # Return the new date string
        return new_date
    else:
        # Return an error message if the input date does not match the expected format
        return "Invalid date format"