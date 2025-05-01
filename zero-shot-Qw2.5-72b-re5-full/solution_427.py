import re

def change_date_format(dt):
    """
    Write a function to convert a date of yyyy-mm-dd format to dd-mm-yyyy format by using regex.
    """
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    return re.sub(pattern, r'\3-\2-\1', dt)