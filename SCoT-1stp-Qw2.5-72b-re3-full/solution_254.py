def words_ae(text):
  # Split the text into words
  words = text.split()
  # Initialize the result list
  result = []
  # Iterate over each word
  for word in words:
    # Check if the word starts with 'a' or 'e'
    if word.lower().startswith(('a', 'e')):
      # Add the word to the result list
      result.append(word)
  # Return the result list
  return result