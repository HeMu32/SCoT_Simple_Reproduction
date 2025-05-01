import re

def text_match(text):
  """
  Write a function to find sequences of lowercase letters joined with an underscore using regex.
  """
  # Define the regex pattern
  pattern = r'\b[a-z]+_[a-z]+\b'
  
  # Find all matches in the text
  matches = re.findall(pattern, text)
  
  # Return the list of matches
  return matches