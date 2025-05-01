def ascii_value(k):
  if len(k) != 1:
    raise ValueError("Input must be a single character.")
  ascii_value = ord(k)
  return ascii_value