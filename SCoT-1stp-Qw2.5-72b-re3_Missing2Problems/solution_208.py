import re

def is_decimal(num):
  # Define the regex pattern for a decimal with a precision of 2
  pattern = r'^\d+(\.\d{2})?$'
  
  # Check if the input string matches the pattern
  if re.match(pattern, num):
    return True
  else:
    return False